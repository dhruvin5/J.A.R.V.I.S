import tkinter as tk
from tkinter import *
import pyaudio
import subprocess
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
#https://www.youtube.com/watch?v=Lp9Ftuq2sVI
from googlesearch import search 
from bs4 import BeautifulSoup
import pyjokes
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os 
from time  import sleep
import winshell
import pylint
import smtplib
import getpass
import re
import sys
from random import randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image
import PIL
from tkinter import messagebox




# packing the scrollbar function 
global y
y=10
 

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")
	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir!") 
	else:
		speak("Good Evening Sir !") 
	assname =("Jarvis 1 point o")
	speak("I am your Assistant")
	speak(assname)	
def speakstory():
	number = random.randint(0,4)
	storyName = 'ShortStory-'+str(number)+'.txt'
	f = open(storyName,"r",encoding="utf8")
	string1=f.read()
	f.close()
	speak(string1)
def takeCommand():
    global y
    if y>700 :
        y=10
    y= y+20
    print(y)
    r = sr.Recognizer()
    #txt=tk.Label(window,text = "Listening....",font=("Georgia",16,"bold"))
    #txt.place(bordermode=INSIDE,x=10,y=y)
    #y=y+20
    with sr.Microphone() as source:
        print("listening..")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language ='en-in')
        print("reconizing....")
        txt2=tk.Label(window,text =f"You said..",font=("Georgia",8))
        txt2.place(bordermode=INSIDE,x=1100,y=y)
        y=y+20
        txt3=tk.Label(window,text =f"{query}",font=("Georgia",16,"bold"))
        txt3.place(bordermode=INSIDE,x=1100,y=y)
        y=y+40
    except Exception as e:
        print(e) 
        print("Unable to Recognize your voice.") 
        txt3=tk.Label(window,text = "Unable to Recognize your voice.",font=("Georgia",12,"bold"))
        txt3.place(bordermode=OUTSIDE,x=10,y=y)
        y=y+40
        return "None"
    return query
def sendEmail(to,content):
	smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
	smtp_obj.ehlo()
	smtp_obj.starttls()

	email = 'lilysingh081@gmail.com'
	password =input('Enter password: ')
	#iriggfbjuclgjdle
	smtp_obj.login(email,password)
	from_add = email
	to_add = to
	subject = 'Py'
	message = content
	print()
	msg = "Subject:"+ subject +'\n' + message
	smtp_obj.sendmail(from_add,to_add,msg)

def whatsapp(to,message):
	person =[to]
	string= message
	chrome_driver_binary = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
	driver=webdriver.Chrome(chrome_driver_binary)   # Selenium chromedriver path
	driver.get("https://web.whatsapp.com/")
	#wait = WebDriverWait(driver,10) 
	sleep(15)
	for name in person:
		print('IN')
		user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
		user.click()
		print(user)
		for _ in range(5):
			text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
			text_box.send_keys(string)
			sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
			sendbutton.click()
   
   
def submit(): 
  
    name=name_entry.get() 
    password=passw_var.get() 
      
    print("The name is : " + name) 
    print("The password is : " + password) 
      
    name_var.set("") 
    passw_var.set("")


def speaking():
    global y
    speak("How can I help you Sir")
    txt=tk.Label(window,text = "Listening....",font=("Georgia",16,"bold"))
    txt.place(bordermode=INSIDE,x=10,y=y)
    y=y+20
    while True :
        query=takeCommand().lower()
        print(query)
        if  'youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")   
        elif 'stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com") 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        elif 'search for' in query:
            x=re.search('search for',query)
            speak("This is what I found sir!")
            print(x)
            query=query[x.start()+10:]
            print(query)
            for j in search(query,tld="co.in",num=1, stop=1):
                print(j)
                webbrowser.open(j)
        elif 'news' in query:
            webbrowser.open("https://timesofindia.indiatimes.com/india") 
            speak('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ============'''+ '\n')
# STORY
        elif 'tell me a story' in query:
            speak("Reading a story book")
            content=takeCommand()
            speakstory()
# PLAY MOVIE
        elif 'play movie' in query:
            speak("Playing your playlist sir")
            music_dir = "D:\\User Data\\Movies\\Shaadi Mein Zaroor Aana 2017"
            songs = os.listdir(music_dir)
            print(songs) 
            random=os.startfile(os.path.join(music_dir, songs[0]))

# MAIL
        elif 'mail' in query or 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To whom should i send? Can you please type the email.")
                to = input("Enter the email here: ") 
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")   
# WHATSAPP
        elif 'whatsapp' in query:
            try:
                speak("To whom should i send? Can you please type in the name.")
                to = input('Name: ')
                speak("What should i send? Can you please type in the message.")
                content = input("Enter the message: ") 
                speak('You will have to scan for whatsapp web. ')
                whatsapp(to, content)
                speak("Message has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this message") 
# RANDOM Qs
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")

        elif "will you be my gf" in query or "will you be my bf" in query: 
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif 'the time' in query:
            strTime = datetime.datetime.now()
            speak(f"Sir, the time is {strTime}")

        elif 'jarvis' in query:
            speak("Jarvis 1 point o in your service Mister")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me Jarvis")

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Vaishnavi.")
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "who am I" in query:
            speak("If you talk then definately your human.")

        elif "why did you came to this world" in query:
            speak("Thanks to TLE. further It's a secret")
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
        elif "who are you" in query:
            speak("I am a virtual assistant created by Vaishnavi")
#EMPTY BIN
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
#DONT LISTEN
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            sleep(a)
            print(a)
# LOCATION
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/"+ location +"")
# NOTES
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now()
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)        
        elif "show the note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))
# EXIT      
        elif 'exit' in query or 'quit' in query:
            speak('Thank you for your time')
            return -1
        return 0

   

#Tkinter
window=tk.Tk()
window.geometry("1300x800")
name_var=tk.StringVar()
scrollbar = Scrollbar(window) 
window.configure(background='black')
img = PIL.Image.open('jarvis.png')
img = img.resize((400, 500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
lbl = Label(window, image = img ,highlightthickness = 0,bd=0)
lbl.pack()
btn_open = tk.Button(window, text="Speak", command=speaking,)
btn_open.place(bordermode=OUTSIDE, height=50, width=400,x=500,y=720)


#rollbar.config(command=text_info.yview) 
window.mainloop()
