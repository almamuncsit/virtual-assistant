import pywhatkit


def search(command: str) -> None:
    topic = command.replace('search', '')
    pywhatkit.search(topic)
