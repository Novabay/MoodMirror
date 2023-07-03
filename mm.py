import time
import threading
from picamera2 import Picamera2, Preview
import cv2
from deepface import DeepFace


def main():
"""
setup camera, timer, calssifier and result datastructur and start loop 
"""
    #Setup Camera
    picam = Picamera2()
    config = picam.create_preview_configuration()
    picam.configure(config)
    
    #Setup cv2 classifier
    cascade = cv2.CascadeClassifier('/home/pi/magicmirror/haarcascade_frontalface_default.xml')
    #Parameter specifying how much the image size is reduced at each image scale
    global scaleFactor
    scaleFactor = 1.35
    #Parameter specifying how many neighbors each candidate rectangle should have to retain it
    global minNeighbors
    minNeighbors = 7
   
    #time to analyze the emotion
    analyzeTime = 5
    #time how fast should the loop iterate min= 0.1
    loopTime = 0.2
    #time after the person leaves the emotion is deleted from the file
    resetTime = 3
    
    #dict for emotions
    global emotions
    emotions = {'angry': 0,
                'disgust': 0,
                'fear': 0,
                'happy': 0,
                'sad': 0,
                'surprise': 0,
                'neutral': 0
        }
    #list of emotions to be excluded
    global notWantedEmotions
    notWantedEmotions = ['disgust','fear']
    #sum the output from deepface to emotions if True
    #else count the dominant emotion in emotions up
    global sumVals
    sumVals = True
    
    start_camera_stream(picam, cascade, analyzeTime, loopTime, resetTime)
   
    

def start_camera_stream(picam, cascade, analyzeTime, loopTime, resetTime):
    
    write_to_file('')
    picam.start()
    timer = None
    resetFile = None
    while True:
        loopStartTime = time.time()
        image=picam.capture_array()
        faceRecognized, faceImage = recognice_face(image, cascade)
        
# checks if face is in the picture starts 5 sec emotion 
# analyze while a face is there 
        if(faceRecognized):
            if(timer is None or not timer.is_alive()):
                timer= threading.Timer(analyzeTime, react_to_emotion)
                print('Start timer')
                reset_emotion()
                timer.start()
            else:
                analyze_emotion(image)
            if(resetFile is not None and resetFile.is_alive()):
                resetFile.cancel()
        else:
            if(timer is not None and timer.is_alive()):
                print('Stop timer')
                timer.cancel()
                resetFile = threading.Timer(resetTime,write_to_file,[''])
                resetFile.start()
                
        #show cam stream
        cv2.imshow('Camera Stream',cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
                            
        # exit loop if 'q' is pressed
        if (cv2.waitKey(1) == ord('q')):
            break;
        
        #adjusts iteration to equal run time
        loopTimeDiff = time.time()-loopStartTime
        if(loopTime > loopTimeDiff):
            time.sleep(loopTime-loopTimeDiff)
            
    cv2.destroyAllWindows()
    picam.close()


def recognice_face(image, cascade):
"""
returns True if a face is recogniced and a image of the face with a red frame around it
"""
    #converts image to grayscale image the calssifikator works better with it
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(imageGray,scaleFactor,minNeighbors)
    if len(faces) < 1:
        return False, None
    return True, _face_frame_(image, faces)
     

def _face_frame_(image, faces):
"""
Helper methode to indicate where the face is detected by drawing a red frame around the area
"""
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y),(x + width, y + height), color=(255,0,0), thickness=3)
    return True, image



def analyze_emotion(faceImage):
"""
analyze the emotion with Deepface and add the result depending on the strategie to the global emotion map
"""
    prediction = DeepFace.analyze(faceImage,actions='emotion',enforce_detection=False)
    prediction = cut_emotion(prediction,notWantedEmotions)
    if(sumVals):
        __sum_strat(prediction)
    else:
        __count_strat(prediction)
    

def __count_strat(prediction):
"""
counts the dominant emotion one up
"""
    dominantEmotion = list(prediction[0]['emotion'].keys())[0]
    for key in prediction[0]['emotion']:
        if(prediction[0]['emotion'][dominantEmotion] < prediction[0]['emotion'][key]):
            dominantEmotion = key
    emotions[dominantEmotion] += 1
    

def __sum_strat(prediction):
"""
sum the values for each emotion to global emotions dict
"""
    for key in prediction[0]['emotion']:
        emotions[key] += prediction[0]['emotion'][key]


def cut_emotion(prediction, values):
"""
delete not wanted emotion from dict
"""
    for cutEmotion in values:
        if cutEmotion in prediction[0]['emotion']:
            del prediction[0]['emotion'][cutEmotion]
    return prediction


def react_to_emotion():
"""
evaluate the emotion dict and write the result to result.txt file
"""
    print('Timer finish')
    dominantEmotion = max(emotions, key=emotions.get)
    print('Are you?',dominantEmotion)
    print(emotions)
    write_to_file(dominantEmotion)
    reset_emotion()
    

def reset_emotion():
"""
set all values in the global emotion map to 0
"""
    for key in emotions:
        emotions[key] = 0
        

def write_to_file(result):
"""
write the dominantEmotion into a txt file for the GUI
"""
    file = open('/home/pi/magicmirror/result.txt','w')
    file.write(result)
    file.close()


if __name__ == '__main__':
    main()
