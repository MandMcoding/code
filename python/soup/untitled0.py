#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.youtube.com/c/vsauce1/videos").text
soup = BeautifulSoup(html_text, "lxml")
#video = soup.find("a", class_="style-scope ytd-grid-renderer")
print(soup)