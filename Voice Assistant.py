#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
from googlesearch import search
engine = pyttsx3.init('sapi5') #driver for voices
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[random.randint(0,1)].id) #0 for male 1 for female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak(" Hello Jai Shree Krishna !")
    elif hour>12 and hour<18:
        speak(" Hello Good Afternoon!")
    else:
        speak(" Hello Good Evening!")
    speak("Let me know how can i help you!. What are you looking for?")

def takecommand():
    spoken_words = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bot Listening Active...")
        spoken_words.pause_threshold = 2
        audio = spoken_words.listen(source)
    try:
        print("Recognising Your Voice...")
        query  = spoken_words.recognize_google(audio, language = 'en-in')
    except Exception as E:
        speak("Sorry for the trouble. Can you speak again?")
        print("Say that again please...")
        return 'None'

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rishabh10011@gmail.com','Rishnat@69')
    server.sendmail('rishabh10011@gmail.com', to, content)
    serve.close()
    
if __name__ == '__main__':
    wishme()
#    history = open('history.txt',a+)
#    searches = open('g_search.txt',a+)
    while True:
        query = takecommand()
        query = query.lower() 
        if 'open wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia",'')
            results = wikipedia.summary(query,sentences=5)
            speak("According to wikipedia,")
            speak(results)
        elif 'search' in query:
            searches.write("Entry: "+str(datetime.datetime.now()))
            #--------------------------------------------------------------------------------------------------
            s_query = query.partition("search")[2]
            ind=1
            for i in search(s_query, tld="com", num=10, stop=10, pause=2):
                print(str(ind)+" " + i)
                searches.write(i)
                ind = ind+1
        elif 'open notepad' in query:
            npath = 'C:\Windows\system32\notepad.exe'
            os.startfile(npath)
        elif 'open paint' in query:
            npath = 'C:\\Windows\\System32\\mspaint.exe'
            os.startfile(npath)
        #elif 'open anaconda' in query:
           # npath = 'C:\Users\risha\anaconda3'
            #os.startfile(npath)
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'open student mail' in query:
            webbrowser.open('https://mail.google.com/mail/u/1/#inbox')
        elif 'open classroom' in query:
            webbrowser.open('https://classroom.google.com/u/1/h?pli=1')
        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M"%S')
            speak(f"The current time is {strTime}")
        elif 'python tutorial' in query:
            webbrowser.open('https://www.youtube.com/channel/UCaNJxOXoFYhkEJ5hu69lx7g')
        #elif 'open whatsapp' in query:
            #npath = 'C:\\Users\\LENOVO\\Desktop\\WhatsApp Desktop.exe'
            #os.startfile(npath)
          # Error che bcoz e loko third party applications allow karvanu bandh kari didhu
          # less secure app access
        elif 'email to rishabh' in query:
            try:
                speak("What should i send?")
                content = takecommand()
                to = '20dit009@charusat.edu.in'
                sendEmail(to,content)
                speak("Email Sent Successfully!")
            except Exception as E:
                print(E)
                speak("There has been an error sending the email!")
        #elif 'open logs' or 'open history' in query:
   #         speak(history.write('Entry log: '+str(datetime.datetime.now())+"\t "+str(query)))            
        elif 'shutdown' and 'bot' in query:
            speak("Goodbye Rishabh")
            os._exit(0)
        elif 'shutdown' and 'this' and 'device' in query:
            os.system('shutdown /s /t 1')
        elif 'restart' and 'this' and 'device' in query:
            os.system('shutdown /r /t 1')
        elif 'logout' and 'this' and 'device' in query:
            os.system('shutdown -l')
#    history.close()
#    searches.close()


# In[ ]:





# In[ ]:




