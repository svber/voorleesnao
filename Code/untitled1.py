# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:08:03 2020

@author: svber
"""
import cv2
from Text_to_speech import Speech
import pytesseract

def Update(value):
    global ImageBin
    print (value)
    ImageBin = cv2.threshold(Image,value,255,cv2.THRESH_BINARY)[1]
    cv2.imshow('Fenetre',ImageBin)

# window
cv2.namedWindow('Fenetre',cv2.WINDOW_GUI_NORMAL)

# Trackbar 
Slider = cv2.createTrackbar('Threshold','Fenetre',0,255,Update)

# Open image
Image = cv2.imread('../data/image1.jpg')

cv2.imshow('Fenetre',Image)

cv2.waitKey(0)
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(ImageBin)

speech = Speech(text)
speech.generate_speech(150, 1.0, False)

cv2.waitKey(0)
cv2.destroyAllWindows()


