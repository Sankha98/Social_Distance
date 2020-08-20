# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 05:43:48 2020

@author: Sankhasubhra Mandal
"""


import imutils
import cv2
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("download.jpg")

(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("My Image", image)
cv2.waitKey(0)
cv2.imwrite('OpenCV_Out.jpg', image)