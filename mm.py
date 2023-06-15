import time
from picamera2 import Picamera2, Preview
import cv2
from deepface import DeepFace

picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)

#cap = cv2.VideoCapture(0) normaly used dosent work 

picam.start()
while True:
    frame=picam.capture_array()
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    try:
        prediction = DeepFace.analyze(rgb,actions='emotion',enforce_detection=False)
        print(prediction[0]['dominant_emotion'])
    except ValueError:
        print('Face could not be detected.')
    cv2.imshow('Cam0',rgb)
    if (cv2.waitKey(1) == ord('q')):
        break
cv2.destroyAllWindows()
picam.close()
