# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:48:06 2020

@author: Tomatobox
"""


import speech_recognition as sr
r = sr.Recognizer()
print(sr.__version__)
#r.recognize_google()
harvard = sr.AudioFile('CantinaBand3.wav')
with harvard as source:
    r.adjust_for_ambient_noise(source, duration=10)
    audio = r.record(source, duration=4)
print(r.recognize_google(audio, show_all=True))