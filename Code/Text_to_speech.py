# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:32:58 2020

@author: Quico van den Berg
"""

import cv2
import matplotlib.pyplot as plt
import pytesseract as pt
import pyttsx3 as pyt
from fpdf import FPDF

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
        image = cv2.imread(self._path + ".jpg")
        text = pt.image_to_string(image)
        return text

    def create_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        pdf.cell(200, 10, txt = self.get_text(), ln = 1, align = "C")
        pdf.output("../Output/Text.pdf")

class Speech:
    def __init__(self, text):
        self._text = text
        
    @property
    def text(self):
        return self._text
    
    @property
    def voice(self):
        engine = pyt.init()
        voices = engine.getProperty('voices')
        return voices
    
    @property
    def volume(self):
        engine = pyt.init()
        volume = engine.getProperty('volume')
        return volume
    
    @property
    def speed(self):
        engine = pyt.init()
        rate = engine.getProperty('rate')
        return rate 
        
    def change_speech(self, voice = bool, volume = float, speed = int):
        engine = pyt.init()
        voices = self.voice
        if voice == True:
            engine.setProperty('voice', voices[1].id)
        else:
             engine.setProperty('voice', voices[0].id) 
        engine.setProperty('volume', volume)
        engine.setProperty('rate', speed)
    
    def generate_speech(self, voice = bool, volume = float, speed = int):
        engine = pyt.init()
        self.change_speech(voice, volume, speed)
        engine.say(self._text)
        engine.runAndWait()
        
    def save_voice(self):
        engine = pyt.init()
        engine.save_to_file(self._text, "../Output/Voice.mp3")
        engine.runAndWait()