from helpers.commands import take_command
from provides.route import run_command
from helpers.speak import talk


def start() -> None:
    while True:
        start_command = take_command()

        if 'quit' in start_command or 'stop' in start_command:
            break

        if not start_command or 'linux' not in start_command:
            continue

        talk('I am here. How can I help you?')

        command = take_command()

        if 'quit' in start_command or 'stop' in start_command:
            break

        run_command(command)
