import pyttsx3
import datetime
import speech_recognition as sr
from time import sleep
import wikipedia as wp
import smtplib
import webbrowser as wb
import os
import random as rd
import pyautogui
import psutil
import pyjokes




assi_name="pandit ramakrishna"
mast_name="Master"
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
    
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The time is")
    speak(Time)
    
    
    
    
    
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("Todays date is")
    speak(day)
    speak(month)
    speak(year)
    
    
def wishme():
    
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        Speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    elif hour>=16 and hour<20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak(mast_name)
    speak("your assistance is at your service")
    time()
    date()
    
    
    
    
def takeCommand():
    r=sr.Recognizer()
    query=""
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(query)
        
    except Exception as e:
        print(e)
        speak("Unable to Recognize")
        #return query
    return query
       
    
    
    
    
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_GMAIL','YOUR_GMAIL_PASSWORD')  
    server.sendmail('YOUR_GMAIL',to,content)
    server.close()
    
    
    
def screenshot():
    img=pyautogui.screenshot()
    img_name=datetime.datetime.now().strftime('%I%M%S%d%m%Y')
    img_name=str(img_name)
    img.save(img_name+".jpg")
        
def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at"+usage+"percentage")
    battery=psutil.sensors_battery()
    speak("Battery is at"+str(battery.percent)+"percentage")
    
    
def jokes():
    a=pyjokes.get_joke()
    print(a)
    speak(a)
    
   
if __name__=='__main__':
    wishme()
    a_status=True
    while a_status:
        query=takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()
        
        

        
        
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            print("Searching Wikipedia...",end="")
            query=query.replace("wikipedia","")
            result=""
            while result=="":
                print(".",end="")
                try:
                    
                    result=wp.summary(query,sentences=2)
                except:
                    
                    speak("No results found")
                    break
            print()
            print(result)
            speak(result)
            
        
        
        elif 'send email' in query:
            try:
                speak("What should i send")
                content=takeCommand()
                to="RECIPIENT_EMAIL"
                sendEmail(to,content)
                speak("Email Was Sent Successfully")
            except Exception as e:
                print(e)
                speak("Could not send the email")
                
                
                
        elif "search in chrome" in query.lower():
                speak("What Should I search")
                chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                search=takeCommand()
                speak("Searching")
                speak(search)
                wb.get(chromepath).open_new_tab(search+'.com')
                
                
                
        elif 'logout' in query:
            os.system('shutdown -l')
            
            
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
            
            
        elif 'restart' in query:
            os.system('shutdown /r /t 1')
            
        
        
        elif 'play song' in query:
            songs_dir=("D:/Rahul Desai/Music/Hindi/HSilent")
            songs=os.listdir(songs_dir)
            a=rd.randrange(0,len(songs)+1)
            print(a)
            os.startfile(os.path.join(songs_dir,songs[a]))
            print("Playing....")
            print(songs[a])
                
                
        
        elif "offline" in query:
            speak("Going Offline") 
            speak("Have a Good time Professor See you soon")
            break
            
            
        elif "remember that" in query:
            speak("What should i remember?")
            rem_data=takeCommand()
            remember=open('data.txt','w')
            remember.write(rem_data+'\n')
            remember.close()
            
            
        elif "do you know anything" in query:
            remember=open('data.txt','r')
            speak("You said me to remember"+remember.read())
            remember.close()
            
            
            
        elif "screenshot" in query:
            screenshot()
            speak("Screenshot saved")
            
            
            
        elif 'cpu' in query:
            cpu()
            
            
        elif "joke" in query:
            jokes()
                         
