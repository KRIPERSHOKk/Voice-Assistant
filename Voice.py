import pyttsx3

def say(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 175)
    engine.setProperty('volume', 0.9)

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    engine.say(text)

    engine.runAndWait()