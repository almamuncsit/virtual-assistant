from helpers.speak import talk


def say_sorry(commands: str = '') -> None:
    message = "Sorry, I didn't I didn't know"
    print(message)
    talk(message)
