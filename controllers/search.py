import pywhatkit


def search(command):
    topic = command.replace('search', '')
    pywhatkit.search(topic)