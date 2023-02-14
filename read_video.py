# VIDEOS:
import cv2 as cv

capture = cv.VideoCapture('videos/animation.mp4') 

# we use a while loop, to read the video frame by frame:
while True:
    isTrue, frame = capture.read()      # reading a frame in every iteration
    cv.imshow('Video' , frame)  

    # if the letter d is pressed break the loop
    if cv.waitKey(20) & 0xFF==ord('d'):                 
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)                           # wait for key to continue