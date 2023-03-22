# Netscape Cookies

[![Python Version](https://img.shields.io/pypi/pyversions/netscape-cookies.svg)](https://pypi.org/project/netscape-cookies/)
[![PyPI Version](https://img.shields.io/pypi/v/netscape-cookies.svg)](https://pypi.org/project/netscape-cookies/)
[![License](https://img.shields.io/pypi/l/netscape-cookies.svg)](https://pypi.org/project/netscape-cookies/)

`netscape-cookies` is a Python extension that simplifies the process of exporting Selenium WebDriver cookies into the Netscape HTTP Cookie format. This is useful when you need to use cookies in various tools that require the Netscape format.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
    - [Basic Usage](#basic-usage)
    - [Example with Selenium WebDriver](#example-with-selenium-webdriver)
3. [Functions](#functions)
4. [Contributing](#contributing)
5. [License](#license)

## Installation

To install `netscape-cookies`, simply run:

```bash
pip install netscape-cookies
```

## Usage
### Basic Usage
```python
from netscape_cookies import save_cookies_to_file
from netscape_cookies import to_netscape_string

# Your Selenium WebDriver cookies
cookie_data = [
    {
        "domain": ".example.com",
        "expiry": 1677649426,
        "path": "/",
        "secure": True,
        "name": "cookie_name",
        "value": "cookie_value"
    }
]

file_path = "cookies.txt"

# Save cookies to file in Netscape format
save_cookies_to_file(cookie_data, file_path)

# Get cookies as String in Netscape format
to_netscape_string(cookie_data)
```

### Example with Selenium WebDriver
```python
from selenium import webdriver
from selnet_cookies import save_cookies_to_file
from netscape_cookies import to_netscape_string


browser = webdriver.Firefox()
browser.get("https://www.example.com")

# Get cookies from Selenium WebDriver
cookie_data = browser.get_cookies()

file_path = "cookies.txt"

# Save cookies to file in Netscape format
save_cookies_to_file(cookie_data, file_path)

# Get cookies as String in Netscape format
to_netscape_string(cookie_data)

browser.quit()

```

## Functions

`netscape-cookies` provides the following functions:

1. `to_netscape_string(cookie_data: List[Dict[str, Any]]) -> str`: Converts the given Selenium WebDriver cookie data into a Netscape HTTP Cookie formatted string.
2. `save_cookies_to_file(cookie_data: List[Dict[str, Any]], file_path: str) -> None`: Saves the given Selenium WebDriver cookie data to a file in the Netscape HTTP Cookie format.

## Contributing

Contributions to `netscape-cookies` are welcome!

## License

`netscape-cookies` is released under the [MIT License](LICENSE).
