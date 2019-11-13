import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()


def gchoice():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        aa = r.listen(source)
    try:
        print("Recognizing...")
        choice = r.recognize_google(aa)
        return choice
    except sr.UnknownValueError:
        return 1


def gmusic():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        aa = r.listen(source)
    try:
        print("Recognizing...")
        music = r.recognize_google(aa)
        return music
    except sr.UnknownValueError:
        return 1


def gagain():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        aa = r.listen(source)
    try:
        print("Recognizing...")
        ag = r.recognize_google(aa)
        if 'yes' in ag:
            print("Yes")
            return 1
    except sr.UnknownValueError:
        return 2


def gmsg():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        aa = r.listen(source)
    try:
        print("Recognizing...")
        mg = r.recognize_google(aa)
        print(mg)
        return mg
    except sr.UnknownValueError:
        return 1


def gstock():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        aa = r.listen(source)
    try:
        print("Recognizing...")
        s = r.recognize_google(aa)
        return s
    except sr.UnknownValueError:
        return 1


def gnote():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        aa = r.listen(source)
    try:
        print("Recognizing...")
        note = r.recognize_google(aa)
        return note
    except sr.UnknownValueError:
        return 1


def gtitle():
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        aa = r.listen(source)
    try:
        print("Recognizing...")
        title = r.recognize_google(aa)
        return title
    except sr.UnknownValueError:
        return 1
