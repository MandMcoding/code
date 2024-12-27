#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 01:58:27 2023
 
@author: marwanGPT
"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Define the URL of the website you want to scrape
url = "https://earth.nullschool.net/#current/wind/surface/level/orthographic=61.29,21.34,2734"
#"https://earth.nullschool.net/#current/wind/isobaric/10hPa/waterman"
#"https://calendar.google.com/calendar/u/0/r"
#"https://minesweeperonline.com/"
#https://earth.nullschool.net/#current/wind/surface/level/orthographic=-226.41,16.15,1161
#https://earth.nullschool.net/#current/wind/surface/level/orthographic=61.29,21.34,2734
print(url)

# Set up the Selenium webdriver with headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--window-size=2560, 1600")
chrome_driver_path = "/Users/marwan/Documents/Code/Python/Calendar Background/chromedriver"

#while True:
# Create a Service object with the ChromeDriver executable path
service = webdriver.chrome.service.Service(chrome_driver_path)
service.start()

# Set the ChromeDriver service in the webdriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website using Selenium
driver.get(url)

print("Taking Pic")
time.sleep(10)

# Get the page screenshot
screenshot_path = os.path.join(os.path.expanduser("~"), "screenshot.png")
driver.save_screenshot(screenshot_path)

# Close the Selenium webdriver
driver.quit()

print("Applying Background")
# Set the screenshot as the desktop background using osascript
script = """
tell application "System Events"
    tell every desktop
        set picture to "{}" as POSIX file
    end tell
end tell
""".format(screenshot_path)

os.system("osascript -e '{}'".format(script))
#os.remove(screenshot_path)

#time.sleep(60)
print("done!")
