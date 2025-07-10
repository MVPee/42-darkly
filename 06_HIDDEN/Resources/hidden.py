import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

def crawl_and_collect_readmes(url, out_file):
    response = requests.get(url)
    lines = response.text.splitlines()
    # Remove first 4 and last 2 lines
    html = "\n".join(lines[4:-2])
    soup = BeautifulSoup(html, "html.parser")
    links = [a['href'] for a in soup.find_all('a')]
    for link in links:
        if link == "README":
            readme_url = url + "README"
            readme_resp = requests.get(readme_url)
            out_file.write(readme_resp.text)
            logging.info(f"From {readme_url}:\n" + readme_resp.text + "\n")
            if "flag" in readme_resp.text:
                logging.info(f"Found flag at {readme_url}")
                break
        elif link.endswith('/') and link != "../":
            crawl_and_collect_readmes(url + link, out_file)

def main():
    base_url = "http://192.168.38.130/.hidden/"
    with open("out.txt", "w") as out_file:
        crawl_and_collect_readmes(base_url, out_file)


if __name__ == "__main__":
    main()