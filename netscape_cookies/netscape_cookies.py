from typing import Any, Dict, List, Optional, Union
from selenium import webdriver


class Cookie:
    """
    A class representing a cookie with its associated properties.

    Attributes:
        domain (str): The domain of the cookie.
        flag (bool): A flag indicating whether the cookie is persistent.
        path (str): The path for which the cookie is valid.
        secure (bool): Whether the cookie is secure (only sent over HTTPS).
        expiration (int): The expiration timestamp of the cookie.
        name (str): The name of the cookie.
        value (str): The value of the cookie.
    """

    def __init__(
        self,
        domain: str,
        flag: bool,
        path: str,
        secure: bool,
        expiration: int,
        name: str,
        value: str,
    ):
        self.domain = domain
        self.flag = flag
        self.path = path
        self.secure = secure
        self.expiration = expiration
        self.name = name
        self.value = value

    def __repr__(self):
        """Returns a string representation of the Cookie object."""
        return f"Cookie(domain={self.domain}, flag={self.flag}, path={self.path}, secure={self.secure}, expiration={self.expiration}, name={self.name}, value={self.value})"

    def to_selenium_cookie(self):
        return {
            "name": self.name,
            "value": self.value,
            "path": self.path,
            "secure": self.secure,
            "domain": self.domain,
        }


def to_netscape_string(cookie_data: List[Dict[str, Any]]) -> str:
    """
    Converts a list of cookies to a Netscape cookie string format.

    Args:
        cookie_data (List[Dict[str, Any]]): A list of dictionaries where each dictionary contains cookie attributes.

    Returns:
        str: A string representation of the cookies in Netscape format.
    """
    result = []
    for cookie in cookie_data:
        domain: str = cookie.get("domain", "")
        expiration_date: Union[int, None] = cookie.get("expiry", None)
        path = cookie.get("path", "")
        secure = cookie.get("secure", False)
        name = cookie.get("name", "")
        value = cookie.get("value", "")

        include_sub_domain = domain.startswith(".") if domain else False
        expiry = str(int(expiration_date)) if expiration_date else "0"

        result.append(
            [
                domain,
                str(include_sub_domain).upper(),
                path,
                str(secure).upper(),
                expiry,
                name,
                value,
            ]
        )

    return "\n".join("\t".join(cookie_parts) for cookie_parts in result)


def parse_from_string(input_string: str) -> Dict[str, Cookie]:
    cookies = {}
    # Split the string by new lines and filter out empty lines
    lines = [line for line in input_string.split("\n") if line.strip() != ""]
    for line in lines:
        # Skip comment lines, which start with "#" but allow lines with #HttpOnly_ prefix
        if line.startswith("#") and not line.startswith("#HttpOnly_"):
            continue  # Skip regular comment lines

        lineFields = line.strip().split("\t")

        # Ensure there are enough fields to create a valid Cookie object
        if len(lineFields) >= 7:
            # If domain starts with "#HttpOnly", clean it up
            domain = (
                lineFields[0].replace("#HttpOnly_", "")
                if lineFields[0].startswith("#HttpOnly")
                else lineFields[0]
            )
            flag = (
                lineFields[1].upper() == "TRUE"
            )  # Convert 'TRUE' or 'FALSE' to boolean
            path = lineFields[2]
            secure = (
                lineFields[3].upper() == "TRUE"
            )  # Convert 'TRUE' or 'FALSE' to boolean
            expiration = (
                int(lineFields[4]) if lineFields[4].isdigit() else 0
            )  # Handle expiration
            name = lineFields[5]
            value = lineFields[6]

            # Create a Cookie object
            cookie = Cookie(domain, flag, path, secure, expiration, name, value)

            # Store the cookie in the dictionary with the cookie name as the key
            cookies[name] = cookie
    return cookies


def parse_from_file(cookieFile: str) -> Dict[str, Cookie]:
    """Parse a Netscape cookies file into a dictionary with cookies identified by their name."""

    with open(cookieFile, "r") as file:
        return parse_from_string(file.read())


def netscape_from_driver(
    driver: webdriver.Chrome, file_path: Optional[str] = None
) -> str:
    """
    Extracts cookies from a Selenium WebDriver instance and returns them in Netscape format.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance (Chrome).
        file_path (Optional[str]): The file path where the cookies will be saved (if provided).

    Returns:
        str: A string representation of the cookies in Netscape format.
    """
    data = to_netscape_string(driver.get_cookies())
    if file_path:
        save_cookies_to_file(driver.get_cookies(), file_path)
    return data


def save_cookies_to_file(cookie_data: List[Dict[str, Any]], file_path: str) -> None:
    """
    Saves the given cookies in Netscape format to a file.

    Args:
        cookie_data (List[Dict[str, Any]]): A list of cookies to be saved.
        file_path (str): The file path where the cookies should be saved.
    """
    netscape_string = to_netscape_string(cookie_data)
    with open(file_path, "w") as file:
        file.write(netscape_string)


def save_to_file(cookies: List[Cookie], cookieFile: str):
    """Save a list of Cookie objects into a Netscape cookie file."""

    with open(cookieFile, "w") as file:
        # Write the header for the Netscape cookie format
        file.write("# Netscape HTTP Cookie File\n")
        file.write("# http://curl.haxx.se/rfc/cookie_spec.html\n")
        file.write("# This is a generated file!  Do not edit.\n\n")

        for cookie in cookies:
            # Write each cookie in the required format: domain, flag, path, secure, expiration, name, value
            flag = "TRUE" if cookie.flag else "FALSE"
            secure = "TRUE" if cookie.secure else "FALSE"
            expiration = (
                str(cookie.expiration)
                if cookie.expiration is not None and cookie.expiration > 0
                else ""
            )

            # Write the cookie to the file
            file.write(
                f"{cookie.domain}\t{flag}\t{cookie.path}\t{secure}\t{expiration}\t{cookie.name}\t{cookie.value}\n"
            )
        return cookieFile
