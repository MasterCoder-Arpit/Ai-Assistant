import webbrowser
import os
from datetime import date
import smtplib
import time
import datetime
import pyautogui
import pyjokes                    #pip install pyjokes
from GoogleNews import GoogleNews #pip install Googlnews
import pyttsx3                    #pip install pyttsx3
import speech_recognition as sr   #pip install SpeechRecognition
import wikipedia                  #pip install wikipedia
from googlesearch import search   #pip install googlesearch-python
import psutil                     #pip install psutil





#voice of assistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your assistant  Sir")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_threshold= 1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query= r.recognize_google(audio, key=None, language="en-pk", show_all=False)
           
            print(f"user said:{query}\n")

        except Exception as e:
            speak(" please say that again")
            return "None"
        return query


    
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU Is at "+usage)
    battery = psutil.sensors_battery()
    speak(" and Battery is at")
    speak(battery.percent)
    speak("How may I help You")

    
if __name__ == "__main__":
    
    clear = lambda: os.system('cls') #To clear all previous commands
    clear()
    wishMe()
    cpu()
   
    while True:

        #search commands

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikiepdia")
            speak(results)


        elif "open a website" in query:
            speak ("what should i search")
            query = str(input())
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  
            webbrowser.get(chromepath).open_new_tab(query+".com")

        elif "search a query"in query:
            speak("What Should I Search")
            searchterm = takeCommand().lower()
            speak("searching")
            webbrowser.open("https://www.google.com/search?q="+searchterm)

        
        elif "search Youtube"in query:
            speak("What To Search")
            youtubesearch=takeCommand()
            speak("Here we go to youtube")
            webbrowser.open("https://www.youtube.com/results?search_query="+youtubesearch)
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location)

        elif 'news' in query:
           
            googlenews = GoogleNews()
            googlenews = GoogleNews (lang='en')
            speak("what would you like to know about")
            topic= takeCommand()
            googlenews.search(topic)
            googlenews.get_page(1)
            link = googlenews.get_links()
            webbrowser.open(link)


                
        #open command
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            

        elif 'open chrome' in query:
            speak("opening Google Chrome")
            chromePath ="/C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            os.startfile(chromePath)
            
        elif 'open vscode' in query:
            speak("opening VS Code")
            codepath="C:/Users/LENOVO/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code"
            os.startfile(codepath)
            


        #comman work for assistant
        elif 'take screenshot' in query:
         img = pyautogui.screenshot()
         img.save("path to save image")


        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('your assistant .txt', 'w')
            file.write(" :- ")
            file.write(note)
            file.write(note)
            speak("file saved ")
        elif "show note" in query:
            speak("Showing Notes")
            file = open("your assistant .txt", "r") 
            print(file.read())
            speak(file.read(6))
            print("Invalid input")

        elif 'send email' in query:
            speak("what Should I say")
            content = takeCommand()
            speak("Who is the Receiver")
            receiver = input("Please Enter the name of the Receiver : ")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
     
            # Enable low security in gmail
            server.login("Your Email Id", "Your Password")
            server.sendmail("Your Email",receiver, content)
            server.close()
            try:
                 print("Succesfully Sent")
                 speak("Succesfully Sent")
                 

            except:
                 print ("Message not sent")
                 speak("Message Not Sent")
         #basic questions forassistant


        elif 'the date' in query:
            today = date.today()
            strdate =  today.year, today.month, today.day
            speak(f"Sir, the date is {strdate}")
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "change my name" in query:
            speak("What would you lme to call you, Sir ")
            takeCommand()
            speak("name set")
        
        elif "change your name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)


        elif 'I am bored' in query:
            speak(pyjokes.get_joke(language='en',category=all))
            print(pyjokes.get_joke())


        elif "who i am" in query:
            speak("If you talk then definately your human.")


        elif "who are you" in query:
            speak("I am your virtual assistant")

        elif "don't listen" in query or "stop listening" in query:
            print("your assistant  will not listen for 60 seconds")
            time.sleep(60)

        elif 'hello' in query:
            speak("hii Sir, how are you")

        elif 'fine' in query:
            speak("okay sir whats the work for me")

        elif 'exit' in query:
            speak("have a nice day sir")
            exit()

        elif 'change your voice' in query:
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            speak("voice changed")

        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = takeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()
        
        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
        
        
        

        