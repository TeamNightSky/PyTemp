from .select import tempdir
import toml
from pathlib import Path


def read(path):
    return toml.loads(open(path, "r").read())

def conf(path: str = None):
    return read(Path(path if path else tempdir())/"pytemp.toml")
