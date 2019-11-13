from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyttsx3
import time

engine = pyttsx3.init()

a = "Alright. Hold on, while I connect to Google."


def getweather():
    print(a)
    engine.say(a)
    engine.runAndWait()
    opts = Options()
    opts.headless = True
    print("Connecting to Google...")
    driver = webdriver.Chrome('C:\\Users\\aayus\\Documents\\chromedriver', options=opts)
    driver.get('https://www.google.com/search?q=google+weather')
    print("Getting details...")
    time.sleep(2)
    loc = driver.find_element_by_id("wob_loc")
    loc = loc.get_attribute('innerHTML')
    temp = driver.find_element_by_id("wob_tm")
    temp = temp.get_attribute('innerHTML')
    pp = driver.find_element_by_id("wob_pp")
    pp = pp.get_attribute('innerHTML')
    hm = driver.find_element_by_id("wob_hm")
    hm = hm.get_attribute('innerHTML')
    ws = driver.find_element_by_id("wob_ws")
    ws = ws.get_attribute('innerHTML')
    b = "In " + loc + ", the temperature currently is " + temp + " ℃"
    c = "Expected Precipitation today would be " + pp
    d = "Humidity is " + hm
    e = "Current wind speed is " + ws
    print(b)
    engine.say(b)
    engine.runAndWait()
    print(c)
    engine.say(c)
    engine.runAndWait()
    print(d)
    engine.say(d)
    engine.runAndWait()
    print(e)
    engine.say(e)
    engine.runAndWait()
    driver.quit()

