import requests


class AppConfig:
    """Class representing a Quantum Compiler application and its configuration."""
        # self._name = "Quantum Compiler"
        # self._version = __version__

    @staticmethod
    def get_latest_version(current_version):
        """Get the latest version from the GitHub API."""
        url = 'https://api.github.com/repos/KDUser12/Quantum-Compiler/releases/latest'

        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            latest_version = data['tag_name']

            result = check_for_update(current_version, latest_version)

            return result

        except requests.exceptions.RequestException as error:
            return f"An error occurred while using the GitHub API: {error}"

    @staticmethod
    def check_for_update(current_version, latest_version):
        """Check if there is an update available."""
        if current_version == latest_version:
            return "You are using the latest version of Quantum Compiler !"
        else:
            return ("Update available now! Click here to install the latest version of Quantum Compiler: "
                    "https://github.com/KDUser12/Quantum-Compiler/releases")
