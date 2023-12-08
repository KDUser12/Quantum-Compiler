error_code = [
    {
        "Basic error": {
            "requests.exceptions.RequestException": "An error occurred while using the GitHub API.",
            "Exception": "An error occurred.",
        }
    },
    {
        "Error 1xx": {  # quantum-compiler/app/
            "101": """Version of Python not supported.
The Quantum Compiler requires a specific version of Python to ensure optimal and reliable operation.
Please update your Python installation to version 3.6 or later.
You can download the recommended version from the official Python website: https://www.python.org/downloads/"""
        },
        "Error 2xx": {  # quantum-compiler/core/management/commands/
            "201": "The argument you entered is invalid."
        },
        "Error 3xx": {  # quantum-compiler/core/management/
            "301": "The command you entered does not exist or is invalid."
        }
    }
]
