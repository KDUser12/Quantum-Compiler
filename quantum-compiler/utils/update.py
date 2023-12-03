import requests


def get_latest_version(current_version):
    """Get the latest version from the GitHub API."""
    url = 'https://api.github.com/repos/KDUser12/Quantum-Compiler/releases/latest'

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        latest_version = data['tag_name']

        update = check_for_update(current_version, latest_version)

        return update

    except requests.exceptions.RequestException:
        return None  # f"An error occurred while using the GitHub API: {error}"

def check_for_update(current_version, latest_version):
    """Check if there is an update available."""
    if current_version == latest_version:
        return False  # "You are using the latest version of Quantum Compiler !"
    else:
        return True  # ("Update available now! Click here to install the latest version of Quantum Compiler: https://github.com/KDUser12/Quantum-Compiler/releases")



