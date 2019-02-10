"""A setuptools based setup module."""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

# Extract the tag from the system
from subimage import __version__

# Get the long description from the README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# For more details: https://github.com/pypa/sampleproject
setup(
    name="subimage",
    version=__version__,
    description="A sample Python project to detect image subsets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gist.github.com/jakebrinkmann/ff2e7d5dd0bc3f107ef2a22601b50c15",
    author="Jake Brinkmann",
    author_email="jake.brinkmann@gmail.com",
    packages=find_packages(exclude=["contrib", "docs", "test"]),
    entry_points={"console_scripts": ["subimage=subimage.cli:main"]},
)
