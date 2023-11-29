import subprocess
import sys
import os
import functools
import datetime

# Private, stable API for detecting the Python implementation.
PYPY = sys.implementation.name == "pypy"

# Private and stable API to detect Python version. PYXY means "Python X.Y". For third-party applications to use these
# values, each constant must remain supported by Quantum Compiler versions
PY36 = sys.version_info >= (3, 6)
PY37 = sys.version_info >= (3, 7)
PY38 = sys.version_info >= (3, 8)
PY39 = sys.version_info >= (3, 9)
PY310 = sys.version_info >= (3, 10)
PY311 = sys.version_info >= (3, 11)
PY312 = sys.version_info >= (3, 12)


def get_version(version=None):
    """Return a PEP 440-compliant version number from VERSION."""
    version = get_complete_version(version)

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #   | {a|b|rc}N - for alpha, beta and rc releases

    main = get_main_version(version)

    sub = ""
    if version[3] == "alpha" and version[4] == 0:
        git_changeset = get_git_changeset()
        if git_changeset:
            sub = ".dev%s" % git_changeset

    elif version[3] != "release":
        mapping = {"alpha": "a", "beta": "b", "rc": "rc"}
        sub = mapping[version[3]] + str(version[4])

    return main + sub


def get_main_version(version=None):
    """Return main version (X.Y[.Z]) from VERSION."""
    version = get_complete_version(version)
    parts = 2 if version[2] == 0 else 3
    return ".".join(str(x) for x in version[:parts])


def get_complete_version(version=None):
    """Return a tuple of the Quantum Compiler version. If version argument is non-empty,
    check for correctness of the tuple provided.
    """
    if version is None:
        from QuantumCompiler import VERSION
    else:
        assert len(version) == 5
        assert version[3] in ('alpha', 'beta', 'rc', 'release')

    return version


@functools.lru_cache
def get_git_changeset():
    """Return a numeric identifier of the latest git changeset.

    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    # Repository may not be found if __file__ is undefined, e.g. in a frozen module.
    if "__file__" not in globals():
        return None
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    git_log = subprocess.run(
        "git log --pretty=format:%ct -- quiet -1 HEAD",
        capture_output=True,
        shell=True,
        cwd=repo_dir,
        text=True
    )
    timestamp = git_log.stdout
    tz = datetime.timezone.utc

    try:
        timestamp = datetime.datetime.fromtimestamp(int(timestamp), tz=tz)
    except ValueError:
        return None
    return timestamp.strftime("%Y%m%d%H%M%S")


