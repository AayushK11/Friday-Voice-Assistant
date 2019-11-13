from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyttsx3
from Record import *
import time

engine = pyttsx3.init()

a = "Okay. Which stock would you like to search?"
b = "I'm sorry, You weren't audible. Please try again"
c = "Alright. Hold On, while I connect to Google"


def getstocks():
    print(a)
    engine.say(a)
    engine.runAndWait()
    st = gstock()
    while st == 1:
        print(b)
        engine.say(b)
        engine.runAndWait()
        st = gstock()
    st = st + " Stocks"
    print(c)
    engine.say(c)
    engine.runAndWait()
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome('C:\\Users\\aayus\\Documents\\chromedriver', options=opts)
    print("Rerouting to Google Finance...")
    driver.get('https://www.google.com')
    time.sleep(2)
    se = driver.find_element_by_name("q")
    se.send_keys(st)
    se.submit()
    name = driver.find_element_by_class_name("oPhL2e")
    name = name.get_attribute('innerHTML')
    sm = driver.find_element_by_class_name("HfMth")
    sm = sm.get_attribute('innerHTML')
    sm = sm[0]+sm[1]+sm[2]
    cv = driver.find_element_by_class_name("knowledge-finance-wholepage-chart__hover-card-value")
    cv = cv.get_attribute('innerHTML')
    pc = driver.find_elements_by_class_name("iyjjgb")
    pc = pc[6].get_attribute('innerHTML')
    cval = ""
    count = 0
    pval = ""
    for i in cv:
        if i == ',':
            count = count+1
        elif i != ' ':
            cval = cval+i
        else:
            break
    cval = float(cval)
    for i in pc:
        if i == ',':
            count = count+1
        elif i != ' ':
            pval = pval+i
        else:
            break
    pval = float(pval)
    pl = cval-pval
    ppl = (pl/pval)*100
    if pl > 0:
        ud = "Up"
    else:
        ud = "Down"
    d = name + ", last closed at " + cv + ", according to " + sm
    e = "It went " + str(ud) + " by " + str(round(ppl, 2)) + "%, that is approximately " + str(round(pl, 2)) + " INR"
    print(d)
    engine.say(d)
    engine.runAndWait()
    print(e)
    engine.say(e)
    engine.runAndWait()
    driver.quit()
