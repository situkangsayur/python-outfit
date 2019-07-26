import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("pycloud/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Environment :: Plugins"
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Framework :: Flask",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

extra_opts = {
    "packages": find_packages(exclude=["tests", "tests.*"]),
    "tests_require": ["nose", "coverage==4.2", "blinker", "Pillow>=2.0.0"],
}

setup(
    name="pycloud",
    version=version,
    author="Hendri Karisma",
    author_email="situkangsayur@gmail.com",
    maintainer="Hendri Karisma",
    maintainer_email="situkangsayur@gmail.com",
    url="https://situkangsayur.wordpress.com",
    download_url="https://github.com/situkangsayur/python-cloud",
    license="MIT",
    include_package_data=True,
    description= "",
    long_description=readme,
    platforms=["any"],
    classifiers=CLASSIFIERS,
    #install_requires=["", ""],
    test_suite="nose.collector"
)
