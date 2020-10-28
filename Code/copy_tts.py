# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:32:58 2020

@author: Quico van den Berg
"""

import cv2
import matplotlib.pyplot as plt
import pytesseract as pt
from PIL import Image as Img
import pyttsx3 as pyt
from langdetect import detect
import numpy as np

class Image:
    def __init__(self, path):
        self._path = path
    
    @property
    def image_path(self):
        return self._path
    
    @property
    def image_shape(self):
        image = cv2.imread(self._path + ".jpg")
        return image.shape
    
    def show_image(self):
        image = cv2.imread(self._path + ".jpg")
        fixed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(fixed_image)
    
    def get_text(self):
        pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image = Img.open(self._path + ".jpg")
        pt.image_to_string(image)

    def clean_image(self):
        # filter noise out of image        
        pass

class Speech:
    def __init__(self, text):
        self._text = text
        
    @property
    def text(self):
        return self._text
    
    @property
    def rate(self):
        engine = pyt.init()
        rate = engine.getProperty('rate')
        return rate 
  
    @property
    def volume(self):
        engine = pyt.init()
        volume = engine.getProperty('volume')
        return volume
    
    @property
    def voice(self):
        engine = pyt.init()
        voices = engine.getProperty('voices')
        return voices
    
    def change_speech(self, rate = int, volume = float, voice = bool, lang = None):
        engine = pyt.init()
        voices = self.voice
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        if voice == True:
            engine.setProperty('voice', voices[1].id)
        else:
             engine.setProperty('voice', voices[0].id)
    
    def generate_speech(self, rate = int, volume = float, voice = bool):
        engine = pyt.init()
        self.change_speech(rate, volume, voice)
        engine.say(self._text)
        engine.runAndWait()
    
    def save_voice(self):
        engine = pyt.init()
        engine.save_to_file("Audio record", "../Output/Voice.mp3")
        engine.runAndWait()
           
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('../data/image1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_ERODE, kernel)
cv2.imshow('aaa',thresh)
cv2.imshow('aa',gray)
cv2.imshow('a', opening)
#cv2.waitKey(0)
text = pt.image_to_string(opening)

speech = Speech(text)
speech.generate_speech(150, 1.0, False)
    
    
path = "../Data/image1"
image = Image(path)
print(image.image_shape)
image.show_image()
print(image.get_text())

text = "I will speak this text"
speech = Speech(text)
print(speech.rate)
print(speech.volume)
print(speech.voice)
speech.generate_speech(150, 1.0, False)
speech.save_voice()

lang = detect("Dziewczyna")
print(lang)
cv2.waitKey(0)
cv2.destroyAllWindows()