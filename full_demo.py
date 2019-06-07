import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from playsound import playsound
import random

def TTS(text):
    print(text)
    r1 = random.randint(1,10000000)
    randfile = "Audio"+ str(r1) +".mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(randfile)
    playsound(randfile)
    os.remove(randfile)

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
    if "Who am I" in data:
        TTS("You are Satish")

    elif "how are you" in data:
        TTS("I am fine, Thank you")
    
    elif "Can you Dance" in data:
        TTS("No, its beyond my limit")

    elif "what time is it" in data:
        TTS(ctime())
    else:
        TTS("Sorry, I can't understand you")
    

# initialization
time.sleep(1)
TTS("Hi satish, what can I do for you?")
while 1:
    data = STT()
    COM(data)
