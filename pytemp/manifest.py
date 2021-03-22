from .conffile import conf


def manifest(tdir: str = None):
    if tdir:
        config = conf(tdir)
    else:
        config = conf()

    if "manifest" not in config:
        print("Manifest not listed. Aborting.")
        return

    print("Template manifest:")
    for name, val in config["manifest"].items():
        print(f"    - {name} : {val}")
