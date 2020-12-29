import datetime
from helpers.speak import talk


def tell_current_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    talk('Current time is ' + time)