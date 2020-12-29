import wikipedia
from helpers.speak import talk


def summery( command ):
    look_for = command.replace('tell me about', '')
    info = wikipedia.summary(look_for, 1)
    print(info)
    talk(info)