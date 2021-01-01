import wikipedia
from helpers.speak import talk


def summery(command: str) -> None:
    looking_for = command.replace('tell me about', '')
    information = wikipedia.summary(looking_for, 1)
    print(information)
    talk(information)
