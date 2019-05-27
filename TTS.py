#This module conver text to speech
from gtts import gTTS

customer = 'Hafidz'
amount = 20000
tts = gTTS('hello' + customer + 'have you applied for loan of amount' + str(amount), lang='en')
tts.save('hello.mp3')