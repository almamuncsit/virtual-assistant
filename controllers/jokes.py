import pyjokes
from helpers.speak import talk


def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    talk(joke)
