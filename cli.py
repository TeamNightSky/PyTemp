from pytemp import select as s, run as r, manifest as m

import click


@click.group()
def cli():
    ...

@cli.command()
@click.argument("dir", default=".")
def select(dir):
    """Select template directory"""
    return s(dir)

@cli.command()
@click.argument("arg_path")
@click.option("--dir", default='', help="template directory to run")
def run(arg_path, dir):
    """Run template"""
    return r(path=arg_path, tdir=dir)

@cli.command()
@click.option("--dir", default='', help="template directory to inspect")
def manifest(dir):
    """Inspect values for template"""
    return m(dir)

if __name__ == "__main__":
    cli()
