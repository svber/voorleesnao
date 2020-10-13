# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:40:32 2020

@author: Quico van den Berg
"""

import sys
from PyQt5 import QtWidgets, uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("../Data/Main.ui")

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = 0 # lost Kernal died probeem op bij herhaald opstarten
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())