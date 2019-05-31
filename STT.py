import speech_recognition as sr

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print ('Say Something!')
#     audio = r.listen(source)
#     print ('Done!')
 
# try:
#     text = r.recognize_google(audio)
#     print('Google thinks you said:\n' + text)
    
# except Exception as e:
#     print (e)
r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

text = r.recognize_google(audio)
print('you said:\n' + text)