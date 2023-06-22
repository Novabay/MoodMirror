import cv2


emotions = {0 : 'angry',
            1 : 'disgust',
            2 : 'fear',
            3 : 'happy',
            4 : 'sad',
            5 : 'surprise',
            6 : 'neutral'}

while True:
    
    key = int(input('Number 0-6'))
    
    if key < 0 or 6 < key:
        frameName = '#####'
    else:
        frameName = emotions[key]
        
    image = cv2.imread('../Pictures/' + frameName + '.png')
    print(frameName, image)
    cv2.imshow(frameName,image)
    
    if (cv2.waitKey(1) == ord('q')):
            break;
        
cv2.destroyAllWindows()