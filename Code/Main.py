# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:40:32 2020

@author: Quico van den Berg
"""

import sys
from PyQt5 import QtWidgets, uic, QtGui
from Text_to_speech import Image, Speech

Ui_MainWindow, QtBaseClass = uic.loadUiType("../Data/Main.ui")

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)   
        self.ui.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        photo = str(self.ui.cbImage.currentText())
        if photo == "Image1":
            path = "../Data/image1"
        elif photo == "Image2":
            path = "../Data/image2"
        elif photo == "Image3":
            path = "../Data/image3"

        pixmap = QtGui.QPixmap(path)
        self.ui.lblPhoto.setPixmap(pixmap)
        self.ui.lblPhoto.setScaledContents(True) 
        QtWidgets.QApplication.processEvents()
        
        image = Image(path)
        text = image.get_text()
        speech = Speech(text)
        
        voice = str(self.ui.cbVoice.currentText())
        if voice == "Female":
            gender = 1
        else:
            gender = 0
                
        volume = int(self.ui.sbVolume.value())
        scaled_volume = 1 / 20 * volume
           
        speed = int(self.ui.sbSpeed.value()) 
        scaled_speed = speed * 10
        
        speech.generate_speech(gender, scaled_volume, scaled_speed)
        image.create_pdf()
        speech.save_voice()

if __name__ == "__main__":
    app = 0
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())