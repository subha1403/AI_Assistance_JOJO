import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import json
from ecapture import ecapture as ec
import time
import subprocess
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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

    speak("I am Jojo Sir. Please tell me how may I help you")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak(date)
    speak(month)
    speak(year)


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("pardon me!Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('msubhajit105@gmail.com', 'bumba8013manu1506')
    server.sendmail('msubhajit105@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:

        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if "good bye" in query or "ok bye" in query or "stop" in query:
            speak('I am going to Shut down, good bye')
            break

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'date' in query:
            speak("Sir the date is")
            date()

        elif 'open youtube' in query:
            webbrowser.open_new_tab("youtube.com")

        elif 'open google' in query:
            webbrowser.open_new_tab("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open_new_tab("stackoverflow.com")

        elif 'play music' in query or 'make my mood' in query or 'music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Here is your Vs Code Editor')
            os.startfile(codePath)

        elif 'news' in query:
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/")
            speak('Here are some headlines from Times of India, happy reading')
            time.sleep(6)

        elif 'camera' in query or 'take a pahoto' in query:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(6)

       
        elif 'hello' in query:
            speak("yes sir!")

        

        elif 'turn off' in query:

            speak('do you really want to Shut down your system?')

            reply = takeCommand()

            if 'Yes' in reply:
                subprocess. call(["shutdown", "/1"])

            else:
                break

        elif 'restart' in query:

            speak('do you really want to restart your system?')
            reply = takeCommand()

            if 'Yes' in reply:
                os.system("shutdown /r /t 1")

            else:
                break

        elif 'log out' in query:

            speak('do you really want to log out?')
            reply = takeCommand()

            if 'Yes' in reply:
                os.system("shutdown -1")

            else:
                break

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Subhajit")
            print("I was built by Subhajit")

        elif "weather" in query:
            api_key = "7f788ffd95e56b2bd3d670dcba07da04 "
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x['main']
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'email to manu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "oindrilamandal789@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Subha. I am not able to send this email")

        elif 'email to maa' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "tanimamandal7884@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Subha. I am not able to send this email")
