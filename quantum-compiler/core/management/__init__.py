from pathlib import Path
import core.management.manager
import utils.error_handling
from core.management.commands.basic_commands import (
    helpCommand,
    aboutCommand,
    licenseCommand,
    exitCommand
)


class CommandManagement:
    def __init__(self, user_path=str(Path.home())):
        self.user_path = user_path
        self.console = True
        self.prompt = None

        self.call_command()

    def call_command(self):
        while self.console:
            self.prompt = input(f'[{self.user_path}] : ')
            self.process_command()

    def process_command(self):
        command, category = self.find_command()
        if category == 'basic.commands':
            structure = str(command + 'Command')
            basic_commands = [
                {
                    'helpCommand': lambda: print(helpCommand()),
                    'aboutCommand': lambda: print(aboutCommand()),
                    'licenseCommand': lambda: print(licenseCommand()),
                    'exitCommand': lambda: exitCommand()
                }
            ]

            for command_factory in basic_commands:
                for command_name, command_function in command_factory.items():
                    if command_name == structure:
                        command_function()
                        break
                else:
                    utils.error_handling.output('302')
                    break

    def find_command(self):
        for entry in core.management.manager.commands:
            for category, cmd in entry.items():
                if self.prompt in cmd:
                    return self.prompt, category
        else:
            utils.error_handling.output('301')
            return None, None
