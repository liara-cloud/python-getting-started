from selenium import webdriver
import os
import json
from dotenv import load_dotenv

load_dotenv()
command_executor = os.getenv("COMMAND_EXECUTOR") + "/webdriver"
browserless_token = os.getenv("BROWSERLESS_TOKEN")

with open('websites.json') as f:
    websites_data = json.load(f)
    websites = websites_data["websites"]

screenshots_dir = 'screenshots'
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)
    with open(os.path.join('screenshots', '.gitignore'), 'w') as gitignore_file:
        gitignore_file.write("*\n!.gitignore")

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserless:token', browserless_token)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor=command_executor,
    options=chrome_options
)

for idx, website in enumerate(websites, start=1):
    name = website["name"]
    url = website["url"]
    driver.get(url)
    screenshot_path = os.path.join(screenshots_dir, f"{name.replace(' ', '_')}_screenshot.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved for {name} ({url}) as {screenshot_path}")
