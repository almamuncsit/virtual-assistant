from controllers import play, times, wiki, jokes, search, sorry
from routes import apps

routes = {
    'open': apps.open_application,
    'search': search.search,
    'time': times.tell_current_time,
    'joke': jokes.tell_joke,
    'play': play.play_song,
    'tell me about': wiki.summery,
    'sorry': sorry.say_sorry,
}