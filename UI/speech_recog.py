import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from playsound import playsound
import random
import pandas as pd

POS_DIC =(pd.read_csv("DIC/positive_DIC.csv")).dropna()
NEG_DIC =(pd.read_csv("DIC/negative_DIC.csv")).dropna()
POS_DIC = POS_DIC["words"].str.lower().tolist()
NEG_DIC = NEG_DIC["words"].str.lower().tolist()

def TTS(text):
    print(text)
    r1 = random.randint(1,10000000)
    randfile = "Audio"+ str(r1) +".mp3"
    tts = gTTS(text=text, lang="id") #id for Indonesia
    tts.save(randfile)
    playsound(randfile)
    os.remove(randfile)

def STT():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio, language="id-ID") #Default is English, language="id-ID"
        print("You said: " + data)
    except sr.UnknownValueError:
        print("System could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def COM(data):
    
    for word in data.split(' '):
        if word in POS_DIC:
            result = 'YES'
            return result 
        elif word in NEG_DIC:
            result = 'NO'
            return result     
        else:
            result = 'Not Confirmed'
            return result
    

# initialization
# time.sleep(1)
# cust_name = 'Hafidz'
# #amount = '20000'
# brr_id = '1 2 3 4'
# address = 'India'
# contact_no = '9 8 5 9 8 1 7 4 5 1'
# message = 'hello '+ cust_name +' saya anastasia dari pinbee ingin mengonfirmasi tentang data anda. mohon dengarkan secara baik-baik. jadi, saya sedang bicara dengan '+ cust_name +' dengan ID peminjam ' + brr_id + ' anda tinggal di ' + address + ' dengan nomor handphone ' + contact_no
mess = ['Your name is satish', 'You are from Asssam', 'Your mobile number is 9 8 5 9 8 1 7 5 6 4']
result = []
for item in mess:
    TTS(item)
    #while 1:
    data = STT()
    user_resp = COM(data)
    result.append(user_resp)

print(result)