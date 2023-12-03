import datetime
from utils.error_handling.manager import error_code


def _output_file(format_output, file):
    """Display error in a log file."""
    with open(file, 'a') as file:
        file.write(format_output)
    return None


def _find_element(target_code):
    """Find the element corresponding to the error code."""
    for entry in error_code:
        for category, errors in entry.items():
            if target_code in errors:
                description = errors[target_code]
                return description
        else:
            continue


def output(code, message=None):
    """Display error message in the console."""
    current_time = datetime.datetime.now()
    log_file = 'logs.txt'

    if message is None:
        description = _find_element(code)
        format_output = f'\n[{current_time}] : ERROR {code} - {description}\n'
    else:
        format_output = f'\n[{current_time}] : {code} {message}\n'
    _output_file(format_output, log_file)
    print(format_output)
