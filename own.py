import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import subprocess
import socket
import winshell
import psutil
import autopy

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('757748-E2HVPXRATX')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')  

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your Virtual Assistant!')
speak('How may I help you?')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print('User: ' + query + '\n')
        except:
            speak('Sorry sir! I didn\'t get that! Try typing the command!')
            query = input()
            print('User: ' + query + '\n')
    return query        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
                    a=input('username:')
                    b=input('password:')
                    c=input('receipient:')
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(a, b)
                    server.sendmail(a, c, content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
            else:
                speak('say a name')

           
        elif 'hello' in query:
            speak('Hello Sir')
                                    
        elif 'play music' in query:
            music_folder = r'F:\\music\\'
            music = ['Edison', 'bensound-actionable', 'bensound-buddy', 'Micro', 'Lucid_Dreamer']
            music = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')

        elif 'shutdown' in query:
            speak('understood sir')
            speak('connecting to command prompt')
            speak('shutting down your computer')
            os.system('shutdown -s')

        elif 'log off' in query or 'sign out' in query:
            speak('understood sir')
            speak('connecting to command prompt')
            speak(query+'your computer')
            os.system('shutdown -l')

        elif 'vlc' in query or 'open vlc' in query:
            speak('opening vlc media player...')
            subprocess.call(r'C:\Program Files\VideoLAN\VLC\vlc.exe')

        elif 'ip' in query or 'my ip' in query or 'show ip' in query or 'show my ip' in query:
            hostname = socket.gethostname()  
            IP = socket.gethostbyname(hostname) 
            speak('your ip address is:'+IP)

        elif 'pc name' in query or 'computer name' in query:
            hostname = socket.gethostname()
            speak('your '+query+' is:'+hostname)

        elif 'disconnect' in query or 'disconnect wifi' in query or 'offline' in query or 'go offline' in query:
            speak('disconnecting from internet sir..')
            os.system('netsh wlan disconnect')

        elif 'what is my battery percentage' or 'show my battery percentage' or 'battery percentage' or 'battery status' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            if plugged==False:
                plugged="Not Plugged In"
            else:
                plugged="Plugged In"
            speak(percent+'% | '+plugged)s

        elif 'screenshot' or 'take screenahot' in query:
            bitmap=autopy.bitmap.capture_screen().save('screengrab.jpeg')

        elif 'nothing' in query or 'abort' in query or 'stop' or 'bye' or 'exit' or 'close' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()


        elif 'clean temp' in query or 'empty temp' in query or 'clean temp files' in query or 'empty temp files' or 'clear cache' in query:
            file_size = os.path.getsize('C:\Windows\Temp')
            print(str(file_size) + "kb of data will be removed")
            del_dir = r'c:\windows\temp'
            pObj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = 
            subprocess.PIPE, stderr= subprocess.PIPE)
            rTup = pObj.communicate()
            rCod = pObj.returncode
            if rCod == 0:
                print('Success: Cleaned Windows Temp Folder')
            else:
                print('Fail: Unable to Clean Windows Temp Folder')

        elif 'nothing' in query or 'abort' in query or 'stop' or 'bye' or 'exit' or 'close' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
            
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        

