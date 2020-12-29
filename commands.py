from controllers import play, times, wiki, jokes, search, open, sorry

routes_without_param = {
    'time': times.tell_current_time,
    'joke': jokes.tell_joke,
    'sorry': sorry.say_sorry,
}

routes_has_param = {
    'play': play.play_song,
    'tell me about': wiki.summery,
    'search': search.search,
    'open': open.open_application,
}


def run_command(command):
    for key, route in routes_without_param.items():
        if key in command:
            route()

    for key, route in routes_has_param.items():
        if key in command:
            command = command.replace(key, '')
            route(command)
