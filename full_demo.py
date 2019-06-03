import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from playsound import playsound

def TTS(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    tts.save("audio.mp3")
    playsound("audio.mp3")

def STT():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("System could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def COM(data):
    if "Do you know me" in data:
        TTS('Yes, You are my boss')

    if "how are you" in data:
        TTS("I am fine")

    if "what time is it" in data:
        TTS(ctime())
    

# initialization
time.sleep(2)
TTS("Hi satish, what can I do for you?")
while 1:
    data = STT()
    COM(data)
