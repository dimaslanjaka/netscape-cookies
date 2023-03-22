from setuptools import setup, find_packages
import os

# Read the content of the README.md file
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as fh:
    long_description = fh.read()

setup(
    name="netscape-cookies",
    version="1.0.0",
    packages=find_packages(),
    author="R44CX",
    author_email="r44cx@proton.me",
    description="Convert Cookies to Netscape format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r44cx/netscape-cookies",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
