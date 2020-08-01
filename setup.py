import setuptools
import sys
import os.path


NAME = 'gpt-scrolls'

# Don't import module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scrolls'))

from version import VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    author="Manuel Araoz",
    author_email="gpt-scrolls@maraoz.com",
    description="A collaborative collection of open-source safe GPT-3 prompts that work well",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maraoz/gpt-scrolls",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "openai>=0.2.4,<1.0.0"
    ],
    package_data={
        "": ["*.txt", "*.json"],
    },
)
