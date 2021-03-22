import os


PATH = "/tmp/pytempwd"


def tempdir():
    return open(PATH, "r").read() if os.path.isfile(PATH) else os.getcwd()


def setdir(path):
    open(PATH, "w").write(path)


def select(path: str = None):
    if path is None:
        path = os.getcwd()
    setdir(path)
