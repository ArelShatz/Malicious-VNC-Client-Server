"""import cv2
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
(thresh, blackAndWhiteImage) = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(blackAndWhiteImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img1, contours, -1, (0,255,0), 3)

#for image in images[2:]:
#    result = cv2.bitwise_and(result, image)

cv2.imshow('r', blackAndWhiteImage)
#cv2.imshow('result', blackAndWhiteImage)
cv2.waitKey(0)"""

from skimage.metrics import structural_similarity
import cv2
import numpy as np

before = cv2.imread('first.png')
after = cv2.imread('second.png')

# Convert images to grayscale
before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

# Compute SSIM between two images
(score, diff) = structural_similarity(before_gray, after_gray, full=True)
print("Image similarity", score)

# The diff image contains the actual image differences between the two images
# and is represented as a floating point data type in the range [0,1] 
# so we must convert the array to 8-bit unsigned integers in the range
# [0,255] before we can use it with OpenCV
diff = (diff * 255).astype("uint8")

# Threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

mask = np.zeros(before.shape, dtype='uint8')
filled_after = after.copy()

for c in contours:
    area = cv2.contourArea(c)
    if area > 40:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(before, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.rectangle(after, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.drawContours(mask, [c], 0, (0,255,0), -1)
        cv2.drawContours(filled_after, [c], 0, (0,255,0), -1)

#cv2.imshow('before', before)
#cv2.imshow('after', after)
#cv2.imshow('diff',diff)
cv2.imshow('mask',mask)
#cv2.imshow('filled after',filled_after)
cv2.waitKey(0)

