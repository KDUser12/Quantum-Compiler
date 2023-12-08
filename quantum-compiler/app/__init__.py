import sys
from utils.update import get_latest_version
from utils.version import PY36
import utils.error_handling
from core.management import CommandManagement


class QuantumCompilerApp:
    def __init__(self, version):
        self.version = version
        self.run()
        CommandManagement()

    def run(self):
        try:
            if not PY36:
                utils.error_handling.output('101')
                input('Press enter to exit the program.')
                sys.exit(101)

            menu = self.create_menu()
            print(menu)

            update = get_latest_version(self.version)

            if update is not None:
                print(f"\n{get_latest_version(self.version)}")

        except Exception as error:
            utils.error_handling.output("Exception", error)

    def create_menu(self):
        return f'''Quantum Compiler - {self.version}
Made by KDUser12 on GitHub'''
