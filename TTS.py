#This module conver text to speech
from gtts import gTTS
from playsound import playsound
import os

def TTS():    
    cust_name = 'Hafidz'
    amount = '20000'
    brr_id = '1 2 3 4'
    address = 'India'
    contact_no = '9 8 5 9 8 1 7 4 5 1'

    eng_message= "hello I am anastasia from PinBee wants to confirm about your data. please listen carefully. so am I speaking with." + cust_name + "with borrower ID," + brr_id + ", you are living in," + address + "with phone number," + contact_no + "Please confirm your response with yes or no"
    tts = gTTS(eng_message, lang='en', slow=False)
    tts.save('hello.mp3')
    playsound('hello.mp3')
    #os.system("hello.mp3")

TTS()








# indo_message= 'hello'+ cust_name +'saya anastasia dari pinbee ingin mengonfirmasi tentang data anda. mohon dengarkan secara baik-baik. jadi, saya sedang bicara dengan'+ cust_name +'dengan ID peminjam' + brr_id
# tts = gTTS(indo_message, lang='id', slow=False)
# tts.save('indo_hello.mp3')
