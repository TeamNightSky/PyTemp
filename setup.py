from setuptools import setup


with open('README.md', 'r') as f:
    read = f.read()


dependencies = [
    x 
    for x in open("requirements.txt", 'r')
        .read()
        .split('\n') 
    if x
]

setup(
    name='PythonTemplates',
    description='A CLI tool for rendering python code using Jinja2.',
    long_description=read,
    long_description_content_type='text/markdown',
    version='0.0.0',
    url='https://github.com/TeamNightSky/PyTemp',
    author='FoxNerdSaysMoo, GrandMoff100',
    author_email='teamnightsky.gh@gmail.com',
    install_requires=dependencies,
    packages=['pytemp'],
    entry_points = {
        'console_scripts': ['pytemp=cli.py:cli'],
    }
)
