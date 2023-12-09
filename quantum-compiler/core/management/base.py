import platform
from utils.version import (
    PY36,
    PY37,
    PY38,
    PY39,
    PY310,
    PY311,
    PY312
)


class BaseCommand:
    # Metadata about this command.
    help = ""
    command = ""

    # Configuration shortcuts that alter various logic.
    _called_from_command_line = False
    _called_from_the_program_console = True
    requires_system_check = False
    requires_python_version_check = False

    PYTHON_VERSIONS = {
        36: PY36,
        37: PY37,
        38: PY38,
        39: PY39,
        310: PY310,
        311: PY311,
        312: PY312
    }

    def __init__(self):
        self.system = self.check_system()
        self.python_version = self.check_python_version()

    def check_system(self):
        if self.requires_system_check:
            return platform.system()

    def check_python_version(self):
        if self.requires_python_version_check:
            for version, is_installed in self.PYTHON_VERSIONS.items():
                if not is_installed:
                    return self.PYTHON_VERSIONS.get(version - 1, is_installed)
        return None


