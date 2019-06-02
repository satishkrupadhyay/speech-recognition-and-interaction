import pyttsx3
engine = pyttsx3.init() # object creation

cust_name = 'Hafidz'
amount = '20000'
brr_id = '1 2 3 4'
address = 'India'
contact_no = '9 8 5 9 8 1 7 4 5 1'
eng_message= "hello I am anastasia from PinBee wants to confirm about your data. please listen carefully. so am I speaking with." + cust_name + "with borrower ID," + brr_id + ", you are living in," + address + "with phone number," + contact_no + "Please confirm your response with yes or no"


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say(eng_message)
engine.runAndWait()
engine.stop()