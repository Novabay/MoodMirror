import time
import threading
from picamera2 import Picamera2, Preview
import cv2
from deepface import DeepFace


def main():
    setup()
    picam.start()
    start_camera_stream()
    picam.close()



def setup():
    #Setup Camera
    global picam
    picam = Picamera2()
    config = picam.create_preview_configuration()
    picam.configure(config)
    #Setup cv2 classifier
    global cascade
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # is True if a face is currently is detected
    global faceRecognized
    faceRecognized = False
    # time to analyze the emotion
    global analyzeTime
    analyzeTime = 5
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
 
 
def start_camera_stream():
    timer = None
    while True:
        image=picam.capture_array()
        faceRecognized, faceImage = recognice_face(image)
        #print('facrec',faceRecognized)
        
        if(faceRecognized):
            if(timer is None or not timer.is_alive()):
                timer= threading.Timer(analyzeTime, react_to_emotion)
                print('Start timer')
                timer.start()
            else:
                analyze_emotion(image)
        else:
            if(timer is not None and timer.is_alive()):
                print('Stop timer')
                timer.cancel()
                
        cv2.imshow('Camera Stream',cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
                            

        if (cv2.waitKey(1) == ord('q')):
            break;
    cv2.destroyAllWindows()


#returns True if a face is recogniced and a cropped image of the face
def recognice_face(image):
    #convert image to grayscale classifier works better with it
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(imageGray)
    if len(faces) < 1:
        return False, None
    #return True, _face_frame_(image, faces)
    
    #Cropping the image that only the face is on the image 
    x,y,w,h = faces[0]
    faceImage = image[y:y+h,x:x+w] 
    return True, faceImage
    
# Helper methode to indicate where the face is detected by drawing a red frame around the area
def _face_frame_(image, faces):
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255,0,0), thickness=3)
    return image



def analyze_emotion(faceImage):
    prediction = DeepFace.analyze(faceImage,actions='emotion',enforce_detection=False)
    #print(prediction[0]['emotion'].keys())
    #print(prediction[0]['dominant_emotion'])
    for key in prediction[0]['emotion']:
        emotions[key] += prediction[0]['emotion'][key]


def react_to_emotion():
    print('Timer finish')
    print('Are you?',max(emotions, key=emotions.get))
    print(emotions)
    reset_emotion()

def reset_emotion():
    for key in emotions:
        emotions[key] = 0

if __name__ == '__main__':
    main()
