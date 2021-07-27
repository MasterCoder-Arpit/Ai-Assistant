import datetime
import os
import smtplib
import time
import webbrowser
import wolframalpha
import psutil
import pyautogui
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit as kit
from GoogleNews import GoogleNews
from googlesearch import search

#voice of assistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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
    
def takecommand():
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

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    speak("the current time is")
    speak(Time)


def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wikipedia_search():
    query = "wikipedia java"
    speak('searching wikipedia')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikiepdia")
    speak(results)


def sendemail():
    speak("what Should I say")
    content = takecommand()
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
                 

    except Exception as e:
        print(e)
        print ("Message not sent")
        speak("Message Not Sent")


def screenshot():
    img = pyautogui.screenshot()
    img.save("path to save image")


def Introduction():
    speak("I am JARVIS 2.0 , Personal AI assistant , "
    "I am created by Arpit, "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")



def Creator():
    speak("Arpit is an extra-ordinary person ,"
    "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
    "He is very co-operative ,"
    "If you are facing any problem regarding the 'Jarvis', He will be glad to help you ")







if __name__ == "__main__":
    
    clear = lambda: os.system('cls') #To clear all previous commands
    clear()
    wishMe()
    cpu()
   
    while True:
        # All commands by user are stored in 'query'

        query = takecommand().lower()

        #search commands

        if 'wikipedia' in query:
            wikipedia_search()

        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            webbrowser.get(chromepath).open_new_tab(search+'.com')


        elif "search a query"in query:
            speak("What Should I Search")
            searchterm = takecommand().lower()
            speak("searching")
            webbrowser.open("https://www.google.com/search?q="+searchterm)

        
        elif "search Youtube"in query:
            speak("What To Search")
            youtubesearch=takecommand().lower()
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
            topic= takecommand().lower()
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
            codepath=r"C:/Users/LENOVO/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code"
            os.startfile(codepath)
            
        elif 'Open Ms Word'in query:
            speak("opening MS Word")
            word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010.ink'
            os.startfile(word)


        #comman commands

        elif "what is" in query or "who is" in query: 
			
            client = wolframalpha.Client("EWWWE2-RXR554LY7X")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")


        elif "calculate" in query:
            try :
                 app_id = "EWWWE2-RXR554LY7X"
                 client = wolframalpha.Client(app_id)
                 indx = query.lower().split().index('calculate')
                 query = query.split()[indx + 1:]
                 res = client.query(' '.join(query))
                 answer = next(res.results).text
                 print("The answer is " + answer)
                 speak("The answer is " + answer) 
            except Exception as e:
                print(e)

        elif 'send a whatsapp message' in query:
            speak('Whom do you want to contact?')
            user = int(input("Enter the Number \n"))
            speak("What do you want to say?")
            message = takecommand().lower()
            speak("When to send?")
            s_time = takecommand().lower()
            if 'later' in s_time:
                speak("Tell me about the hour?")
                hour__ = int(takecommand().lower())
                speak("Tell me about the minutes?")
                minute__ = int(takecommand().lower())
            elif 'now' in s_time:
                hour__ = datetime.datetime.now().hour
                if (datetime.datetime.now().second) < 30:
                    minute__ = (datetime.datetime.now().minute) + 1
                else:
                    minute__ = (datetime.datetime.now().minute) + 2
            speak("Sending Message.")
            kit.sendwhatmsg(user,message,hour__,minute__)   


        elif 'take screenshot' in query:
         img = pyautogui.screenshot()
         img.save("/")


        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
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

        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = takecommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()
        
        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read()) 


        elif 'time' in query:
            time_()
        elif 'date' in query:
            date()

        elif 'tell me about yourself'in query:
            Introduction()

        elif 'tell me about Arpit' and 'creator' in query:
            Creator()    
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")


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


        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        # elif 'empty recycle bin' in query:
        #     winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        #     speak("Recycle Bin Recycled")
            