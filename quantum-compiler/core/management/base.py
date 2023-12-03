from utils.version import (
    PY36,
    PY37,
    PY38,
    PY39,
    PY310,
    PY311,
    PY312
)
import platform


class BaseCommand:
    # Metadata about this command.
    help = ""

    # Configuration shortcuts that alter various logic.
    _called_from_command_line = False
    _called_from_the_program_console = True
    requires_system_check = True
    requires_python_version_check = False

    def __init__(self):
        self.system = self.check_system()
        self.python_version = self.check_python_version()

    def check_system(self):
        if self.requires_system_check:
            system_info = platform.system()
            return system_info

    def check_python_version(self):
        if self.requires_python_version_check:
            py_versions = [(36, PY36), (37, PY37), (38, PY38), (39, PY39), (310, PY310), (311, PY311), (312, PY312)]
            for version, is_installed in py_versions:
                if not is_installed:
                    index = py_versions.index((version, is_installed))
                    python_version = py_versions[index - 1]
                    return python_version
                else:
                    continue

