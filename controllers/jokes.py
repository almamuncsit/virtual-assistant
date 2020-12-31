import pyjokes
from helpers.speak import talk


def tell_joke(command=''):
    joke = pyjokes.get_joke()
    print(joke)
    talk(joke)
