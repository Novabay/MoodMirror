import time
import threading
from picamera2 import Picamera2, Preview
import cv2
from deepface import DeepFace
import pygame
from pygame.locals import *




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
    #is True if a face is currently is detected
    global faceRecognized
    faceRecognized = False
    #time to analyze the emotion
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
        
def display_emotion():
    #set up display
    pygame.init()
    screenInfo = pygame.display.Info()
    screenWidth = screenInfo.current_w
    screenHeight = screenInfo.current_h
    screenSize = (screenWidth, screenHeight)
    
    bgc = (0,0,0)
    textColor = (255,255,255)
    textSize = int(screenHeight / 10)
    
    screen = pygame.display.set_mode(screenSize, RESIZABLE)
    pygame.display.set_caption('Emotion Display')
    
    font= pygame.font.SysFont(None, textSize)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(screenSize, RESIZABLE)
                
        screen.fill(bgc)
        textSurface = font.render(dominantEmotion, True, textColor)
        textRect = textSurface.get_rect(center=(screenWidth // 2, screenHeight // 2))
        screen.blit(textSurface, textRect)
        
        pygame.display.flip()
 
 
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
                reset_emotion()
                timer.start()
            else:
                analyze_emotion(image)
        else:
            if(timer is not None and timer.is_alive()):
                print('Stop timer')
                timer.cancel()
                timer = None
                
        #show cam stream
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
    global dominantEmotion
    dominantEmotion = max(emotions, key=emotions.get)
    print('Are you?',dominantEmotion)
    display_emotion()
    reset_emotion()

def reset_emotion():
    for key in emotions:
        emotions[key] = 0


if __name__ == '__main__':
    emotion_thread = threading.Thread(target=display_emotion)
    emotion_thread.start()
    main()
