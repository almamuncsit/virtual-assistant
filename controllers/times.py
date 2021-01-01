import datetime
from helpers.speak import talk


def tell_current_time(command: str = '') -> None:
    time = datetime.datetime.now().strftime('%I:%M %p')
    print('Current time is ' + time)
    talk('Current time is ' + time)
