import speech_recognition as sr
import pyttsx3
import random
from gtts import gTTS
from tkinter import *
from PIL import Image, ImageTk
import playsound
import webbrowser
import os
from time import ctime

print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice: ' + voice_data)
        except Exception as e:
            print('Oops something went wrong: ', str(e))
        return voice_data


def lee_voice(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


class Widget:
    def __init__(self):
        root = Tk()
        root.title('Lena')
        root.geometry('520x320')
        # img = ImageTk.PhotoImage(Image.open('lena_img.jpg'))
        panel = Label(root)
        panel.pack(side='right', fill='both', expand='no')

        userText = StringVar()
        userText.set('Your Virtual Assistant Lena')

        userFrame = LabelFrame(root, text='Lena', font=('Railways', 24, 'bold'))
        userFrame.pack(fill='both', expand='yes')

        top = Message(userFrame, textvariable=userText, bg='black', fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')

        Button(root, text='Speak', font=('Railways', 10, 'bold'), bg='red', fg='white', command=self.clicked).pack(
            fill='x', expand='no')
        Button(root, text='Close', font=('Railways', 10, 'bold'), bg='yellow', fg='black', command=root.destroy).pack(
            fill='x', expand='no')

        lee_voice('How can I help you?')
        root.mainloop()

    def clicked(self):
        print("Working...")
        voice_data = record_audio()
        voice_data = voice_data.lower()
        if 'who are you' in voice_data:
            lee_voice('My name is Lena')
        elif 'search' in voice_data:
            search = record_audio('What do you want to search for?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            lee_voice('Here is what I found for ' + search)
        elif 'find location' in voice_data:
            location = record_audio('What is the location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            lee_voice('Here is the location ' + location)
        elif 'what is the time' in voice_data:
            lee_voice("Sir, the time is: " + ctime())
        elif 'exit' in voice_data:
            lee_voice('Thanks, have a good day')
            exit()


if __name__ == '__main__':
    widget = Widget()
