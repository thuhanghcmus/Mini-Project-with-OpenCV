#import the library
import argparse
import cv2
import imutils

#construct the argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i","--input", required=True, help="path to input image")
args = vars(ap.parse_args())

#read input into image variable
image = cv2.imread(args["input"])
#convert to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#detect thr threshold
thresh = cv2.threshold(image_gray,225,255, cv2.THRESH_BINARY_INV)[1]
#find the contours
cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
#drawing the contours
output=image.copy()
for c in cnts:
    cv2.drawContours(output, [c], -1, (0,0,255),3)
#display the result
Text = "I found {} objects!".format(len(cnts))
cv2.putText(output, Text, (10,25), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255,0,0),1)
cv2.imshow("Result",output)
cv2.waitKey(0)
# How to run the program
#Run -> Edit Configurations... ->Change Name to Count_TetrisBlocks_0x (if you have lots  of inputs) -> Choose the path of script -> fill parameters box by "-i <path to input image>"
# after that Shift+F10 to run