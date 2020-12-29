import pyttsx3

mama = pyttsx3.init()
voices = mama.getProperty('voices')
mama.setProperty('voice', voices[1].id)


def talk(text):
    mama.say(text)
    mama.runAndWait()
