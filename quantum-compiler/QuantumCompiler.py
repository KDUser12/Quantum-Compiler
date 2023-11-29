# Quantum Compiler is a free open-source compilation program.

# This program allows you to create executable files but also compile files for better security when publishing your
# program. It also allows you to create setups for your own program.

from utils.version import get_version
from apps import Apps

VERSION = (1, 0, 0, 'release', 0)

__version__ = get_version(VERSION)

if __name__ == '__main__':
    Apps(__version__)
