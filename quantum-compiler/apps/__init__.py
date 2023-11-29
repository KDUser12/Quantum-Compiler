from utils.update import get_latest_version


class Apps:
    def __init__(self, version):
        print(f'\033]2;Quantum Compiler - {version}\007')

        latest_version = get_latest_version(version)

        print(f"""============================================================

Quantum Compiler {version}
Create by KDUser12 on GitHub
        
{latest_version}       

============================================================
""")
