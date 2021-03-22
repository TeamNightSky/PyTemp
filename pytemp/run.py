from .select import tempdir
from .conffile import conf, read

import jinja2
import os
import shutil
import imp

def run(vals: dict = None, path: str = None, tdir: str = None):
    config = conf(tdir) if tdir else conf()

    if vals is None:
        vals = read(path)

    if ".pytemp" in os.listdir():
        shutil.rmtree(".pytemp")

    shutil.copytree(tempdir() if not tdir else tdir, ".pytemp")

    for root, dirs, files in os.walk(".pytemp"):
        for file in files:
            if file not in (config["blacklist"] if "blacklist" in config else []):
                path = os.path.join(root, file)
                try:
                    contents = open(path, "r").read()
                except UnicodeDecodeError:
                    continue

                template = jinja2.Template(contents)
                with open(path, "w") as wfile:
                    wfile.write(template.render(vals))

    with open(f".pytemp/{config['run']}", "rb") as rf:
        _ = imp.load_module("PYTEMP RUN", rf, config['run'], ('.py', 'rb', imp.PY_SOURCE))

    shutil.rmtree(".pytemp")

