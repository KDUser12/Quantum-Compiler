from .config import AppConfig

class Apps:
    def __init__(self, __version__):
        self._name = "Quantum Compiler"
        self._version = __version__
        self._update = AppConfig.get_latest_version(self._version)

        print(f"""=====================================================================
{self._name} {self._version}
Create by KDUser12 on GitHub.

{self._update}
=====================================================================

        """)
        
