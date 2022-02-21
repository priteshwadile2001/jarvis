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
engine.setProperty('voice', voices[1].id)

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


def takecommad():
    # it takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again plese...")
        return "None"
    return query


    '''def sendEmail(to, content):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo
    server.starttls()
    server.login('priteshwadile6830@gmail.com', 'My-password here')
    server.sendmail('priteshwadile6830@gmail.com', to, content)
    server.close()'''

    if __name__ == "__main__" :
        wishMe()
    # while True:
    if 1:
        query = takecommad().lower()

    # logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('searching wikipedia....')
        query = query.replace("wikipedia", "  ")
        results = wikipedia.summary(query, sentence=2)
        speak("Accourding to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("Youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'C:\\download'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strtime("%H:%M:%S")
        speak(f"sir,the time is{strTime}")

    elif 'open code ' in query:
        codepath = "C:\\Users\\prite\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'email to pritesh' in query:
        try:
            speak("What should i say?")
            content = takecommad
            to = "prieshwadile6830@gmail.com"
            sendEmail(to, content)
            speak("Email has been send")
        except Exception as e:
            print(e)
            speak("sorry my friend harry bhai . I am not able to send a email at the movement")
            
