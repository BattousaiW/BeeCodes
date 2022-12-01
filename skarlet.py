import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import sys

class Skarlet():
    def __init__(self, filename):
        self.filename = filename
        
    def speak(self,text):
        tts = gTTS(text=text,lang = 'en')
        tts.save(self.filename)
        playsound.playsound(self.filename)

    def get_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception: " + str(e))

        return said

sk = Skarlet("greetb.mp3")
sk2 = Skarlet("altg.mp3")
start_up = Skarlet("start.mp3")
gaming = Skarlet("gaming.mp3")
mortal = Skarlet("mortal.mp3")

run = True

while run:
    start_up.speak("Good day Brandon,will we be gaming or programming")

   
    start_up.text = start_up.get_audio()
    
    if "gaming" in start_up.text:
        gaming.speak("Alright, I will open all game launchers for you, anything specific you would like to play")
        os.startfile("D:\Program Files (x86)\Steam\steam.exe")
        os.startfile("C:\Program Files (x86)\Battle.net\Battle.net.exe")
        gaming.text = gaming.get_audio()
        if "Mortal kombat" in gaming.text:
            mortal.speak("opening mortal combat")
            os.startfile("D:\Program Files (x86)\Steam\steamapps\common\Mortal Kombat 11\Binaries\Retail\MK11.exe")
            

    if "hello Scarlet" in sk.text:
        sk.speak("Hello Brandon, how are you?")

    else:
        sk2.speak("Hello, my name is Skarlet. Brandon's personal assistant")




