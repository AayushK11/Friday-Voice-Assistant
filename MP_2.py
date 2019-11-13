from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyttsx3
from Record import *
import time

engine = pyttsx3.init()

a = "Okay. I would need a few details from you. Let's start with the receivers email id. Please type it in the terminal"
b = "I'm sorry, You weren't audible. Please try again"
c = "Please enter a valid Email ID"
d = "Alright. What would you want the message to be?"
e = "Your Email was Successfully sent"
f = "Okay. Please hold on while I connect to Gmail."

sid = "xxxxxxxx@gmail.com"
spw = "xxxxxxx"


def sendemail():
    print(a)
    engine.say(a)
    engine.runAndWait()
    rid = input()
    ab = 0
    while ab == 0:
        if "@gmail.com" in rid:
            break
        else:
            print(c)
            engine.say(c)
            engine.runAndWait()
            rid = input()
            ab = 0
    print(d)
    engine.say(d)
    engine.runAndWait()
    msg = gmsg()
    while msg == 1:
        print(b)
        engine.say(b)
        engine.runAndWait()
        msg = gmsg()
    print(f)
    engine.say(f)
    engine.runAndWait()
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome('C:\\Users\\aayus\\Documents\\chromedriver', options=opts)
    print("Rerouting to Gmail...")
    driver.get('https://www.gmail.com/')
    time.sleep(2)
    driver.find_element_by_name('Email').send_keys(sid)
    driver.find_element_by_name('signIn').click()
    time.sleep(2)
    driver.find_element_by_name('Passwd').send_keys(spw)
    driver.find_element_by_name('signIn').click()
    time.sleep(2)
    print("Composing Email...")
    driver.find_element_by_link_text("Compose Mail").click()
    driver.find_element_by_id("to").send_keys(rid)
    driver.find_element_by_name("subject").send_keys("Auto-Generated Email via Python")
    driver.find_element_by_name("body").send_keys(msg)
    driver.find_element_by_name("nvp_bu_send").click()
    print(e)
    engine.say(e)
    engine.runAndWait()
    driver.quit()
