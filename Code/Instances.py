# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:01:01 2020

@author: Quico van den Berg
"""

from Text_to_speech import Image, Speech
   
path = "../Data/image1"
image = Image(path)
print(image.image_shape)
image.show_image()
print(image.get_text())
image.create_pdf()

text = image.get_text()
speech = Speech(text)
print(speech.speed)
print(speech.volume)
print(speech.voice)
#speech.change_speed(150)
#speech.change_volume(1.0)
#speech.change_voice(True)
speech.generate_speech(False, 1.0, 200)
speech.save_voice()
