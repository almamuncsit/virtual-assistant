import pywhatkit
from helpers.speak import talk


def play_song(command):
    song = command.replace('play', '')
    talk('playing ' + song)
    print('playing ' + song)
    pywhatkit.playonyt(song)