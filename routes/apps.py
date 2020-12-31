import os
from helpers.speak import talk
from controllers.application import sublime, vscode, chrome

routes = {
    'sublime': sublime.sublime,
    'code': vscode.vscode,
    'vs code': vscode.vscode,
    'chrome': chrome.chrome,
    'browser': chrome.chrome,
}


def open_application(command):
    talk('Opening ' + command)

    for app_name, function in routes.items():
        if app_name in command:
            command = command.replace(app_name, '')
            function()
