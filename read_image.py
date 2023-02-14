import cv2 as cv


# Reading Images:

img = cv.imread('images/pawn.png')      
cv.imshow('Pawn', img)                  


cv.waitKey(0)  # waiting for an key 0 = infinite time, when key is pressed the img window is closed