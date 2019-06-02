import speech_recognition as sr
def SST():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something! Listening........')
        audio = r.listen(source)
        print ('Recorded.....')
    
    try:
        text = r.recognize_google(audio)
        print('You said:\n' + text)
        
    except Exception as e:
        print (e)

SST()
    
# r = sr.Recognizer()
# harvard = sr.AudioFile('harvard.wav')
# with harvard as source:
#     audio = r.record(source)

# text = r.recognize_google(audio)
# print('you said:\n' + text)