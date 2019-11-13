from tkinter import *
import pyttsx3
from Record import *
from MP_1 import *
from MP_2 import *
from MP_3 import *
from MP_4 import *
#CREATED BY AAYUSH KUMARIA
r = Tk()
r.title("Friday")
r.geometry('500x350')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

frame = Frame(r, width=500, height=350, bg="white")
frame.place(x=0, y=0)
img = PhotoImage(file='Micro.gif')

a = "Hey! I'm Your personal assistant, Friday. Click the mic when you're ready to give me a command"
b = "How can I Assist you?"
c = "I'm sorry, You weren't audible. Please try again"
d = "Would you need any other assistance?"
e = "Alright, see you later"


def start():
    again = 1
    while again == 1:
        print(b)
        engine.say(b)
        engine.runAndWait()
        choice = gchoice()
        while choice == 1:
            print(c)
            engine.say(c)
            engine.runAndWait()
            choice = gchoice()
        if 'music' in choice:
            print("Music")
            startmusic()
        elif 'email' in choice:
            print("Email")
            sendemail()
        elif 'weather' in choice:
            print("Weather")
            getweather()
        elif 'stocks' in choice or 'stock' in choice:
            print("Stocks")
            getstocks()
        else:
            print(choice)
            print("Invalid Choice")
            engine.say("I cannot execute that currently")
            engine.runAndWait()
        print(d)
        engine.say(d)
        engine.runAndWait()
        again = gagain()
        while again == 2:
            print(c)
            engine.say(c)
            engine.runAndWait()
            again = gagain()
    print("No")
    print(e)
    engine.say(e)
    engine.runAndWait()
    engine.stop()
    quit()

#CREATED BY AAYUSH KUMARIA

def MGUI():
    Label(frame, bg="Coral1", width=500, height=350).place(x=0, y=0)
    Button(frame, image=img, bg="SkyBlue1", width=400, height=250, command=start, bd=5).pack(padx=45, pady=45)
    print(a)
    engine.say(a)
    engine.runAndWait()
    r.mainloop()


if __name__ == '__main__':
    MGUI()
