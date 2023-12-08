from pathlib import Path
import core.management.manager
import utils.error_handling
from core.management.commands.basic_commands import (
    helpCommand,
    aboutCommand,
    licenseCommand,
    exitCommand
)
from QuantumCompiler import __version__


class CommandManagement:
    def __init__(self, user_path=str(Path.home())):
        self.user_path = user_path
        self.console = True
        self.prompt = None

        self.call_command()

    def call_command(self):
        while self.console:
            self.prompt = input(f'[{self.user_path}] : ')
            self.get_command()

    def get_command(self):
        command, category = self.find_command()
        if category == 'basic.commands':
            helpCommand(command)
            aboutCommand(command, __version__)
            licenseCommand(command)
            exitCommand(command)

    def find_command(self):
        for entry in core.management.manager.commands:
            for category, cmd in entry.items():
                if self.prompt in cmd:
                    return self.prompt, category
                else:
                    utils.error_handling.output('301')
                    return None, None
            else:
                continue


