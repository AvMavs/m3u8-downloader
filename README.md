# M3U8 Downloader

This Python script downloads M3U8 files by playing the media and getting the URL from the webpage source.

## Prerequisites

- Python 3.x
- `requests` library
- `BeautifulSoup` library
- `selenium` library
- `webdriver` for Chrome
- `ffmpeg` installed on your machine

## Installation

1. Install Python 3.x on your machine if it is not already installed.
2. Install the required libraries: `requests`, `BeautifulSoup`, and `selenium`.
```pip install requests beautifulsoup4 selenium```
3. Install the `webdriver` for Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Install `ffmpeg` on your machine: https://www.ffmpeg.org/download.html

## Usage

1. Run the script:
```python m3u8_downloader.py```
2. Enter the link to the media you want to download.
3. Enter the output file name (with extension).
4. If the website is locked behind a login, enter "yes" and fill in the required login details.
5. The script will download the M3U8 file to the specified output file.


## Notes

- This script only works for media files that are playable in a web browser.
- This script has only been tested on Windows 10 with Chrome. It may not work on other platforms or with other browsers.
- This script downloads the M3U8 file using `ffmpeg`. If you want to convert the file to a different format, you can modify the `ffmpeg` command in the `download_m3u8_file` function.

# Legal Disclaimer

This script is intended for personal and educational purposes only. The author does not condone or support piracy of any kind. It is the responsibility of the user to ensure that they have the legal right to download and use any media files obtained using this script.
The author of this script is not responsible for any illegal or unauthorized use of this script. The user assumes all responsibility and risk associated with the use of this script.
By using this script, you acknowledge that you have read and understood this disclaimer and agree to use this script at your own risk.
