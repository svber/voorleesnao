# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:08:03 2020

@author: svber
"""
import matplotlib.pyplot as plt
import pytesseract
import cv2
import pyttsx3 as tts

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('../data/image1.jpg')
text = pytesseract.image_to_string(img)
speech = Speech(text)
speech.generate_speech(150, 1.0, False)
plt.imshow(img)
print(text)
