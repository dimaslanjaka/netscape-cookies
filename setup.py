from setuptools import setup, find_packages

setup(
    name="netscape-cookies",
    version="0.1.0",
    packages=find_packages(),
    author="R44CX",
    author_email="r44cx@proton.me",
    description="Convert Cookies to Netscape format",
    long_description="A simple package to convert cookies to Netscape format and save them to a file",
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
