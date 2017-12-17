import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "blink",
    version = "0.1.0",
    author = "CaTaLiS",
    author_email = "sylwiusz.kosacz@gmail.com",
    description = ("blinking led"),
    license = "BSD",
    keywords = "blink led gpio",
    url = "https://github.com/CaTaLiS/blink",
    packages = ['blink', 'tests'],
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)