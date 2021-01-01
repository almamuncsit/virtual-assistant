from routes.commands import routes


def run_command(command: str) -> None:
    for key, route in routes.items():
        if key in command:
            command = command.replace(key, '')
            route(command)
