import cv2
import numpy as np
import timeit


def GetChangedAreas(currentFrame, prevFrame):
    currentFrameGray = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
    prevFrameGray = cv2.cvtColor(prevFrame, cv2.COLOR_BGR2GRAY)

    #images = [cv2.imread(image, 0) for image in glob.glob("*.png")]
    result = cv2.bitwise_xor(currentFrameGray, prevFrameGray)

    #(thresh, blackAndWhiteImage) = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY)
    #contours, hierarchy = cv2.findContours(blackAndWhiteImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    mask = cv2.inRange(result, 1, 255)
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    rects = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        rects.append((x, y, w, h))
        rectImg = currentFrame[y:y+h, x:x+w]
        #cv2.rectangle(currentFrame, (x, y), (x+w, y+h), 255)

    #cv2.imshow('g', currentFrame)

    for rect in rects:
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        rectImg = currentFrame[y:y+h, x:x+w]
        #cv2.imshow('g', rectImg)
        #cv2.waitKey(0)

        #res = cv2.matchTemplate(img2, rectImg, cv2.TM_CCOEFF)
        #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #top_left = max_loc
        #bottom_right = (top_left[0] + w, top_left[1] + h)
        #cv2.rectangle(img1, top_left, bottom_right, 255, 2)

        #cv2.imshow('g', rectImg)
        #cv2.imshow('b', img1)
        #cv2.waitKey(0)


    #cv2.imshow('r', blackAndWhiteImage)
    #cv2.imshow('result', blackAndWhiteImage)
    #cv2.waitKey(0)

a = GetChangedAreas
