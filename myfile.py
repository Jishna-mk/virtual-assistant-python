import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import webbrowser
import os
import sys
import random
import time
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia

# Function to start the virtual assistant program
def start_program():
    # Initialize pyttsx3 engine
    engine = pyttsx3.init('sapi5')
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')
    volume = engine.getProperty('volume')
    engine.setProperty('rate', 180)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', 0.8)

    def update_text(new_text):
        text_box.config(state=tk.NORMAL)
        text_box.insert(tk.END, new_text + '\n')
        text_box.see(tk.END)
        text_box.config(state=tk.DISABLED)

    def speak(text):
        engine.say(text)
        engine.runAndWait()
        update_text("Panda: " + text)

    def wish(text):
        speak(text)

    def wishme():
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            wish('good morning sir. how are you')
        elif 12 <= hour < 16:
            wish('good afternoon sir. how are you')
        else:
            wish('good evening sir. how are you')

    # Rest of the code remains the same

# Rest of the code remains the same

    # Taking voice input
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            update_text("Listening...")
            audio = r.listen(source)
            r.energy_threshold = 800
            r.dynamic_energy_threshold = True
            r.dynamic_energy_adjustment_damping = 0.2
            try:
                text1 = r.recognize_google(audio)
                text = text1.lower()
                update_text("You: " + text)
            except:
                return ""
            return text

    def sleep():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            update_text("Listening...")
            audio = r.listen(source)
            r.energy_threshold = 500
            try:
                text1 = r.recognize_google(audio)
                text = text1.lower()
                update_text("You: " + text)
            except:
                return "none"
            return text

    # Logic of the program
    text = ''
    question = ''
    type_sentence = ''
    running = True
    time.sleep(5)
    wishme()

    # Operating according to input voice
    while running:
        text = takecommand()
        question = text
        type_sentence = ''
        if 'good evening' in text or 'good morning' in text or 'good afternoon' in text:
            speak('how may i help you sir?')
        if 'search' in text and 'in wikipedia' in text or 'search about' in text and 'in wikipedia' in text or 'wikipedia' in text:
            query1 = text.replace('wikipedia', '')
            query3 = query1.replace('about', '')
            query4 = query3.replace('in', '')
            query5 = query4.replace('for', '')
            query2 = query5.replace('search', '')
            query6 = query2
            speak('do you want me to narrate or open webpage sir?')
            answer = takecommand()
            if 'narrate' in answer or 'direct' in answer:
                results = wikipedia.summary(query6, sentences=1, auto_suggest=False)
                speak('according to wikipedia ' + results)
            elif 'web page' in answer or 'website' in answer or 'webpage' in answer:
                page1 = wikipedia.page(query2, auto_suggest=False)
                print(page1)
                page2 = page1.url
                print(page2)
                speak('redirecting to webpage')
                webbrowser.get().open_new_tab(page2)
                print(page2)
        elif text == '':
            speak('sorry sir. can you say that again?')
        elif 'search' in text and 'in google' in text:
            query1 = text.replace('in google', '')
            query2 = query1.replace('search', '')
            speak('searching ' + query2 + ' in google')
            webbrowser.get().open_new_tab('www.google.com/search?gx&q=' + query2)
        elif 'search' in text and 'in youtube' in text:
            query1 = text.replace('in youtube', '')
            query2 = query1.replace('search for', '')
            speak('searching ' + query2 + ' in youtube')
            webbrowser.get().open_new_tab('https://www.youtube.com/results?search_query=' + query2)
        elif 'search' in text:
            abc1 = text.replace('search', '')
            abc2 = abc1.replace('about', '')
            abc3 = abc2.replace('for', '')
            speak('do you want me to search in google, wikipedia or youtube sir?')
            answer3 = takecommand()
            if 'google' in answer3:
                speak('searching for ' + abc3 + ' in google')
                webbrowser.get().open_new_tab('www.google.com/search?gx&q=' + abc3)

            elif 'wikipedia' in answer3:
                speak('do you want me to narrate or open webpage sir?')
                answer2 = takecommand()
                if 'narrate' in answer2 or 'direct' in answer2:
                    results = wikipedia.summary(abc3, sentences=1, auto_suggest=False)
                    speak('according to wikipedia ' + results)
                elif 'web page' in answer2 or 'website' in answer2 or 'webpage' in answer2:
                    page1 = wikipedia.page(abc3, auto_suggest=False)
                    print(page1)
                    page2 = page1.url
                    print(page2)
                    speak('redirecting to webpage')
                    webbrowser.get().open_new_tab(page2)
                    print(page2)
            elif 'youtube' in answer3:
                speak('searching for ' + abc3 + 'in youtube')
                webbrowser.get().open_new_tab('https://www.youtube.com/results?search_query=' + abc3)

        elif 'your name' in text or text == 'what is the name':
            speak('My name is Panda')
        elif text == 'hi' or text == 'hello' or text == 'hai' or text == 'hello hai' or text == 'hello hi':
            speak('Hello sir. how can I help you?')
        elif text == 'i am fine what about you' or text == "i'm fine what about you" or 'how are you' in text or 'what about you' in text:
            speak('I am great. do you need any help sir?')
        elif text == 'i am fine' or text == "i'm fine":
            speak('Great! do you need any help sir?')
        elif 'who created you' in text:
            speak('I was created by zion')
        elif text == 'introduce yourself' or text == 'who are you' or text == 'tell me something about yourself' or 'introduce yourself' in text:
            speak(
                'I am Panda. You can know me as personal computer and virtual assistant. I was created by using python. I am 1 month old. currently, I am in development stage.')

        elif 'thank you' in text or 'thanks' in text:
            speak('You are welcome! enything else sir?')
        elif 'roll' in text and 'dice' in text:
            r = random.randint(1, 6)
            dice = str(r)
            speak('you got ' + dice)
        elif 'open instagram' in text:
            speak('ok. opening instagram')
            webbrowser.get().open_new_tab('https://instagram.com')
        elif text == 'quit' or text == 'panda bye' or text == 'panda quit' or text == 'bye' or 'bye' in text or 'quit' in text:
            speak('bye bye sir. thanks for your time')
            running = False
            sys.exit()
        elif 'open youtube' in text:
            speak('ok. opening youtube')
            webbrowser.get().open_new_tab('https://www.youtube.com')
        elif 'open facebook' in text:
            speak('ok. opening facebook')
            webbrowser.get().open_new_tab('https://www.facebook.com')
        elif 'open spotify' in text:
            speak('ok. opening spotify')
            webbrowser.get().open_new_tab('https://open.spotify.com/')
        elif text == 'sing a song' or text == 'sing me a song' or 'sing a song' in text:
            speak(
                'I am not a good singer but I hope you will like this. Goin out tonight, changes into something red, Her mother, doesnt like that kind of dress, Everything she never had, she showin off')
        elif 'open chrome' in text or 'open google chrome' in text:
            speak('ok. opening google chrome')
            os.startfile(r'"C:\Users\Jishna M\Desktop\Person 1 - Chrome.lnk"')

        elif 'open excel' in text or 'open excel' in text:
            speak('ok. opening excel')
            os.startfile(r'"C:\Users\Jishna M\Desktop\Excel.lnk"')
        elif 'open vs code' in text or 'open vs code' in text:
            speak('ok. opening vs code')
            os.startfile(r'"C:\Users\Jishna M\Desktop\Visual Studio Code.lnk"')

        elif 'yes' in text:
            speak('how can I help you sir?')

        elif 'shut down the computer' in text or 'shutdown the computer' in text or 'shot down the computer' in text:
            speak('ok shutting down the computer')
            os.system('shutdown /s /f')
            running = False
            sys.exit()

        elif 'time' in text:
            h = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"sir, the time is{h}")

        elif 'close youtube' in text:
            speak('ok. closing youtube')
            webbrowser.get().open_new_tab('https://youtube.com')
        elif 'close facebook' in text:
            speak('ok. closing facebook')
            webbrowser.get().open_new_tab('https://facebook.com')

        elif 'repeat' in text:
            speak('ok sir. say stop repeating if i have to stop')
            repeating = ''
            while repeating != 'stop repeating':
                repeating = takecommand()
                if repeating != 'stop repeating':
                    speak(repeating)
                elif repeating == 'stop repeating':
                    speak('ok sir. repeating stopped.')
        elif 'sleep' in text:
            speak('ok sir goodnight')
            sl_cr = ''
            while not 'wake up' in sl_cr:
                sl_cr = sleep()
                if sl_cr == 'quit':
                    speak('bye bye sir. have a great day')
            speak('hello again sir')
        elif 'show' in text and 'mirror' in text or 'open camera' in text:
            speak('ok. opening camera')
            os.system('start microsoft.windows.camera:')
        elif 'close' in text and 'camera' in text:
            speak('ok. closing camera')
            os.system('TASKKILL /F /IM WindowsCamera.exe')
        elif 'search' in text and 'in youtube' in text:
            search_text1 = text.replace('search', '')
            search_text2 = search_text1.replace('in youtube', '')
            speak('searching for ' + search_text2 + ' in youtube')
            webbrowser.get().open_new_tab('https://www.youtube.com/results?search_query=' + search_text2)
        elif 'play' in text and 'music' in text or 'playlist' in text:
            speak('ok sir enjoy your music')
            os.system('spotify.exe')
            time.sleep(1)
            webbrowser.get().open_new_tab('https://open.spotify.com/')
            while True:
                wakeup_txt = takecommand()
                if 'quit' in wakeup_txt:
                    speak('bye bye sir. have a great day')
                    running = False
                    sys.exit()
                elif 'pause' in wakeup_txt or 'play' in wakeup_txt:
                    webbrowser.get().open_new_tab('https://open.spotify.com/')
                elif 'close spotify' in wakeup_txt:
                    os.system('TASKKILL /F /IM Spotify.exe')
                    break
            speak('hello again sir')
        elif 'open wikipedia' in text:
            speak('ok. opening wikipedia')
            webbrowser.get().open_new_tab('https://www.wikipedia.org')
        else:
            speak('sorry sir that is not assigned. do you want to search for ' + text + '?')
            confirmation = takecommand()
            if confirmation == 'yes':
                speak('searching for ' + text)
                webbrowser.get().open_new_tab('https://www.google.com/search?q=' + text)
            elif confirmation == 'no':
                speak('ok sir. anything else?')

    engine.stop()

# GUI
root = tk.Tk()
root.title("Virtual Assistant")
root.geometry("800x600")
root.resizable(False, False)

# Background Image
bg_img = Image.open("robot.jpg")
bg_img = bg_img.resize((800, 600), Image.BICUBIC)
bg_img = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0)

# Text Box
text_box = tk.Text(root, bg="black", fg="white", state=tk.DISABLED, font=("Arial", 12))
text_box.place(relx=0.5, rely=0.5, anchor="center")

# Thread to start the program
thread = threading.Thread(target=start_program)
thread.start()

# Event handler for closing the window
def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
