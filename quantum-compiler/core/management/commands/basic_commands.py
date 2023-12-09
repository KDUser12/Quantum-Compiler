import sys
from core.management.base import BaseCommand
import datetime
from QuantumCompiler import __version__


class helpCommand(BaseCommand):
    help = "This allows the user to learn more about the commands."
    command = "help"

    def __str__(self):
        commands = [self, aboutCommand, licenseCommand, exitCommand]
        printer = 'BASIC COMMANDS\n'

        for cmd in commands:
            printer += f'{cmd.command} : {cmd.help}\n'

        return printer


class aboutCommand(BaseCommand):
    help = "This allow you to learn more about Quantum Compiler."
    command = "about"

    def __str__(self):
        current_version = __version__
        current_years = datetime.datetime.now().year
        about = f'''Welcome to Quantum Compiler v{current_version}

Quantum Compiler is a powerful solution designed to simplify the process of compiling, creating installers, and obfuscating files in your Python projects.
Developed by KDUser12 on GitHub.

Main features :
- Fast and efficient compilation of Python files.
- Create installers to distribute your applications with ease.
- Advanced obfuscation to secure your source code.

Our commitment to quality:
Quantum Compiler has been carefully crafted to ensure reliable performance, robust error handling, and enhanced srcurity.
Each line of code has been written to the highest industry standards, ensuring a strong and sustainable IT solution.

© 2023-{current_years} Quantum Compiler. All right reserved.'''

        return about


class licenseCommand(BaseCommand):
    help = "Displays the official license of the programs."
    command = "license"

    def __str__(self):
        return '''MIT License
Copyright (c) 2023 KDUser

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''


class exitCommand(BaseCommand):
    help = "Allows the user to exit the program."
    command = "exit"

    def __init__(self):
        super().__init__()
        sys.exit(0)
