import speech_recognition as sr

listener = sr.Recognizer()


def take_command() -> str:
    command = ''
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
    except:
        pass

    return command
