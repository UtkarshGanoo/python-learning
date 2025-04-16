"""speechrecognization module ki help se microphone se audio input lene ke liye and pyttsx3 text to speech ke liye pyttsx3 pocketsphnix ke use se 
without internet ke spech recognition ke liye 


"""



import speech_recognition as sp
import webbrowser
import pyttsx3
import os 
import subprocess
import music

recognizer=sp.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')

def speak(text):
    engine.say(text)
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()



"""def openapp(a):
    if "open vscode"in a.lower():
        os.startfile("C:\\vs code\\Microsoft VS Code\\Code.exe")
    elif "open notepad"in a.lower():
        os.startfile("notepad.exe")"""


def processcommand(c):
   if "open google" in c.lower():
       webbrowser.open("https://google.com")

   elif"open youtube" in c.lower():
       webbrowser.open("https://youtube.com")

   elif "open instagram" in c.lower():
       webbrowser.open("https://instagram.com")

   elif "open Linkedin" in c.lower():
       webbrowser.open("https://Linkedin.com")

   elif "open chatgpt" in c.lower():
       webbrowser.open("https://chatgpt.com")
   elif c.lower().startswith("play"):
       song=c.lower().split(" ")[1]
       link=music.Music_Library[song]
       webbrowser.open(link)


if __name__=="__main__":
    speak("Hello Utkarsh what you want.... ")
    while True:
        r=sp.Recognizer()
        #listening for wake word "UG"
        print("recognizing......")
        try:
        #in with block obtain audio from microphone 
            with sp.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print(" wait i am listening")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
                command = r.recognize_google(audio).strip().lower()
        #in this speech recognize using google
            word=r.recognize_google(audio)
            if word.lower()=="jarvis":
                speak("ya...")
                with sp.Microphone() as source:
                    print("jarvis active....")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)


                    processcommand(command)
                    # openapp(command)


        except Exception as e:
            print("error; {0}".format(e))