import tkinter as tk
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from playsound import playsound
import random
import pandas as pd
import tkinter.scrolledtext as tkscrolled

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("PinBee")
        self.start_btn = tk.Button(self)
        self.start_btn["text"] = "START"
        self.start_btn["command"] = self.INTR
        self.start_btn.grid(column=0,row=0)
        self.start_btn.config( height = 2, width = 30)    
        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.grid(column=1,row=0, padx=20, pady=20)
        self.quit.config( height = 2, width = 30 )
        # self.text = tk.Text(self, width=60, height=25)
        # self.text.grid(row=1, columnspan=2)
        self.text = tkscrolled.ScrolledText(self, width=70, height=30, font=("Helvetica", 11))
        self.text.grid(row=1, columnspan=2)
        self.text.tag_config('red', foreground="red")
        self.text.tag_config('blue', foreground="blue")
    
    def TTS(self,text):
        #print('PinBee: ' + text)
        r1 = random.randint(1,10000000)
        randfile = "Audio"+ str(r1) +".mp3"
        tts = gTTS(text=text, lang="id") #id for Indonesia
        tts.save(randfile)
        playsound(randfile)
        os.remove(randfile)

    def STT(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source, duration=0.5)
            #print("Please Respond.......")
            audio = r.listen(source)

        data = ""
        try:
            data = r.recognize_google(audio, language="id-ID") #Default is English, language="id-ID"
            #print("USER: " + data)
        except sr.UnknownValueError:
            data = ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return data


    def INTR(self):
        mess = ['Hallo saya anastasia dari Pinbee, aplikasi pinjam meminjam', 'Sehubungan dengan aplikasi pinjaman anda, saya mau melakukan konfirmasi data-data dari aplikasi anda', 'Apakah benar nama anda adalah hafidz?','Apakah benar anda mengajukan pinjaman kepada aplikasi pinbee?','Apakah benar anda mengajukan pinjaman darurat dengan jumlah pinjaman sebesar 5000000?']
        result = []
        for item in mess:
            p=0
            self.text.insert(tk.END, 'PinBee: '+item+'\n', 'blue')
            root.update()
            self.TTS(item)
            self.text.insert(tk.END, 'Please Respond... \n', 'red')
            root.update()
            data = self.STT()
            # self.text.insert(tk.END, 'USER: '+data+'\n')
            # root.update()
            if data == "":
                p = 1
            else:
                self.text.insert(tk.END, 'USER: '+data+'\n')
                root.update()
            while (p == 1):
                self.text.insert(tk.END, 'Please Respond again... \n', 'red')
                root.update()
                data = self.STT()
                if data !="":                
                    self.text.insert(tk.END, 'USER: '+data+'\n')
                    root.update()
                    p = 0
            # user_resp = self.COM(data)
            # result.append(user_resp)
            # root.update()

        #print(result)
        self.text.insert(tk.END, 'PinBee: Terima kasih atas kepercayaan Anda pada pinbee, proses selesai\n','blue')
        root.update()
        self.TTS('Terima kasih atas kepercayaan Anda pada pinbee, proses selesai')
        
root = tk.Tk(screenName='PinBee')
root.geometry("600x600")
app = Application(master=root)
app.mainloop()