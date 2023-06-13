import time
from picamera2 import Picamera2, Preview
import cv2
from deepface import DeepFace

picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)

#cap = cv2.VideoCapture(0)

picam.start()
while True:
    frame=picam.capture_array()
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('Cam0',rgb)
    if (cv2.waitKey(1) == ord('q')):
        break
cv2.destroyAllWindows()
picam.close()