# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:05:17 2020

@author: Quico van den Berg
"""

#import os
#from gtts import gTTs
import cv2
import pytesseract as pt
import matplotlib.pyplot as plt

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#myText = "Text To Speech Conversion Using Python"
#language = "en"
#output = gTTs(text = myText, lang = language, slow = False)
#output.save("Output.mp3")
#os.system("Start output.mp3")

file = "../Data/image3.jpg"
image3 = cv2.imread(file)
plt.imshow(image3)
#text = pt.image_to_string(image3)
#print(text)


