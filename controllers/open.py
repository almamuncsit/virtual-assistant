import os
from helpers.speak import talk


def open_application(command):
    talk('Opening ' + command)
    if 'sublime' in command:
        os.system('subl')
    elif 'code' in command or 'vs code' in command:
        os.system('code')
    elif 'chrome' in command or 'browser' in command:
        os.system('google-chrome')
