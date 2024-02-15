import os
import json
import requests
import time


def fetch_website_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    try:
        with open("websites.json", "r", encoding='utf-8') as file:
            websites = json.load(file)

        html_files_directory = "html_files"
        if not os.path.exists(html_files_directory):
            os.makedirs(html_files_directory)

        while True:
            for website in websites:
                website_url = website["url"]
                website_name = website["name"]
                content = fetch_website_content(website_url)
                if content:
                    filename = f"{website_name}_{int(time.time())}.html"
                    file_path = os.path.join(html_files_directory, filename)
                    with open(file_path, "w", encoding='utf-8') as file:
                        file.write(content)
                        print(f"Content of {website_name} has been saved to {file_path}")
                else:
                    print(f"Failed to fetch content of {website_name}")

            time.sleep(10)  

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
