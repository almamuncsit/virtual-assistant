import speech_recognition as sr

listener = sr.Recognizer()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass

    return command
