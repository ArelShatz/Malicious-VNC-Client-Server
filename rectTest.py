import cv2
from mss import mss
import numpy as np
import time
import glob

sct = mss()
img1 = cv2.imread("first.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("second.png", cv2.IMREAD_COLOR)

imgGray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#images = [cv2.imread(image, 0) for image in glob.glob("*.png")]

result = cv2.bitwise_xor(imgGray1, imgGray2)
#(thresh, blackAndWhiteImage) = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY)
#contours, hierarchy = cv2.findContours(blackAndWhiteImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = cv2.inRange(result, 1, 255)

contours = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

cv2.imshow('b', img1)
#cv2.imshow('r', blackAndWhiteImage)
#cv2.imshow('result', blackAndWhiteImage)
cv2.waitKey(0)