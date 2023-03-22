# netscape_cookies.py
def to_netscape_string(cookie_data):
    result = []
    for cookie in cookie_data:
        domain = cookie.get('domain', '')
        expiration_date = cookie.get('expiry', None)
        path = cookie.get('path', '')
        secure = cookie.get('secure', False)
        name = cookie.get('name', '')
        value = cookie.get('value', '')

        include_sub_domain = domain.startswith('.') if domain else False
        expiry = str(int(expiration_date)) if expiration_date else '0'

        result.append([
            domain,
            str(include_sub_domain).upper(),
            path,
            str(secure).upper(),
            expiry,
            name,
            value
        ])

    return "\n".join("\t".join(cookie_parts) for cookie_parts in result)


def save_cookies_to_file(cookie_data, file_path):
    netscape_string = to_netscape_string(cookie_data)
    with open(file_path, 'w') as file:
        file.write(netscape_string)
