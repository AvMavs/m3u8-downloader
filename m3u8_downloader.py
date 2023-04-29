import os
import re
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def login_to_website(driver, login_url, username, password, username_field_id, password_field_id, submit_button_class):
    driver.get(login_url)

    username_field = driver.find_element_by_id(username_field_id)
    password_field = driver.find_element_by_id(password_field_id)

    username_field.send_keys(username)
    password_field.send_keys(password)

    submit_button = driver.find_element_by_css_selector(f".{submit_button_class}")
    submit_button.click()

def play_media_and_get_m3u8_url(driver, link):
    driver.get(link)

    # Play the media
    media_elements = driver.find_elements_by_tag_name("video") + driver.find_elements_by_tag_name("audio")
    for media in media_elements:
        driver.execute_script("arguments[0].play()", media)

    # Get page source after playing media
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # Find m3u8 URL
    m3u8_url = ""
    for script in soup.find_all("script"):
        if script.string and "m3u8" in script.string:
            m3u8_url = re.search("https?://[^\s]+\.m3u8", script.string).group()
            break
    return m3u8_url

def download_m3u8_file(m3u8_url, output_file):
    if not m3u8_url:
        print("No m3u8 URL found.")
        sys.exit(1)
    else:
        print(f"Found m3u8 URL: {m3u8_url}")

    # Download m3u8 file using ffmpeg
    ffmpeg_command = f"ffmpeg -i {m3u8_url} -c copy -bsf:a aac_adtstoasc {output_file}"
    os.system(ffmpeg_command)
    print(f"Downloaded m3u8 file to {output_file}")

if __name__ == "__main__":
    link = input("Enter the link: ")
    output_file = input("Enter the output file name (with extension): ")

    # Set up WebDriver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # Log in to the website (if necessary)
    login_required = input("Is the website locked behind a login? (yes/no): ").lower()
    if login_required == "yes":
        login_url = input("Enter the login URL: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        username_field_id = input("Enter the ID of the username field: ")
        password_field_id = input("Enter the ID of the password field: ")
        submit_button_class = input("Enter the class of the submit button: ")

        login_to_website(driver, login_url, username, password, username_field_id, password_field_id, submit_button_class)

    m3u8_url = play_media_and_get_m3u8_url(driver, link)
    driver.quit()
    download_m3u8_file(m3u8_url, output_file)