import requests
import hashlib


def get_hashed(password):
    return hashlib.sha1(password.encode()).hexdigest().upper()


def get_response(hashed_password):
    req = requests.get(
        f'https://api.pwnedpasswords.com/range/{hashed_password}')
    return req.content.decode().split('\n')


def find_match(hashed_password, response):
    return [
        match for match in response if hashed_password in match
    ]


if __name__ == "__main__":
    import sys
    password = sys.argv[1]
    hashed_password = get_hashed(password)
    res = get_response(hashed_password[:5])
    match_list = find_match(hashed_password[5:], res)
    if len(match_list) > 0:
        match = match_list[0]
        count = match.split(':')[1].replace('\r', '')
        print(f'Your password have been pwned {count} times! Change it now!')
    else:
        print('No matches found for your password')
