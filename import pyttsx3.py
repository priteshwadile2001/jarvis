from datetime import datetime
from http import server
from importlib.resources import contents
#from lib2to3.pytree import _Results
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning..!")

    elif hour >= 12 and hour < 12:
        speak("Good Afternoon")

    else:
        speak("Good Evening..!")

    speak("I am Devil sir. Plese tell mee how may I help you ")



 
            
