# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:40:32 2020

@author: Quico van den Berg
"""

import sys
from PyQt5 import QtWidgets, uic
import cv2
import pytesseract
from Text_to_speech import Speech

Ui_MainWindow, QtBaseClass = uic.loadUiType("../Data/Main.ui")


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Start.clicked.connect(startReading)
        self.ui.Thresh_slider.valueChanged.connect(threshhold_img)
        self.ui.Voice_choice.currentIndexChanged.connect()
        global Image
        Image = cv2.imread('../data/image1.jpg')

def startReading(self):
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(thresh)
    speech = Speech(text)
    speech.generate_speech(150, 1.0, False)
    
def threshhold_img(value):
     global thresh
     thresh = cv2.threshold(Image,value,255,cv2.THRESH_BINARY)[1]
     
def voice_changed(value):
    global voice_int
    voice_int = value
    
def volume_changed(self):
    global volume
    
def speed_changed(self):
    global speed


if __name__ == "__main__":
    app = 0
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())