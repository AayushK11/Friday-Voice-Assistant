from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyttsx3
from Record import *

engine = pyttsx3.init()

a = "Okay. What would you like me to play?"
b = "I'm sorry, You weren't audible. Please try again"
c = "Okay. To exit the music player, press Enter in the terminal twice"
d = "Press anything to exit or press the mic to go again"


def startmusic():
    print(a)
    engine.say(a)
    engine.runAndWait()
    sname = gmusic()
    while sname == 1:
        print(b)
        engine.say(b)
        engine.runAndWait()
        sname = gmusic()
    print(c)
    engine.say(c)
    engine.runAndWait()
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome('C:\\Users\\aayus\\Documents\\chromedriver', options=opts)
    print("Rerouting to Youtube Music...")
    driver.get('https://www.youtube.com/')
    search = driver.find_element_by_id('search')
    search.send_keys(sname)
    print("Searching...")
    sbutton = driver.find_element_by_id('search-icon-legacy')
    sbutton.submit()
    vids = driver.find_elements_by_id('video-title')
    np = "Now Playing: " + vids[0].text
    print(np)
    vids[0].click()
    input()
    input()
    driver.quit()