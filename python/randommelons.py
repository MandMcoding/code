#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 00:36:00 2023

@author: m&mGPT
"""
import random as ran
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

#this is a program that automatically picks a video from the porn aggragation sites from the fuq network
#This version is ment to be run in an IDE since you can change settings and press run as many times as you want
site_setting = 1 #1=normal 1 site 2=fully random site 3=prefered sites
url = "https://www.melonstube.com" 
percent_included = 20
rand_page = True
filter_by_category = True
cat = "beauty"
times = 4

full_random_setting = False #Preset settings

prefered_sites = ["melonstube", "fuq", "assoass", "cartoonpornvideos", "DinoTube", "forhertube", "fucd", "GotPorn", "HDPorzo", "HomemadeGalore", "iXXX", "LatinGalore", "LesbianPornVideos", "LobsterTube", "LupoPorno", "MetaPorn", "PornHD", "Porzo", "Qorno", "SambaPorno", "stocking-tease", "Tiava", "toroporno", "TubeGalore", "tubepornstars"]
sites = ["melonstube", "fuq", "analgalore", "asiangalore", "assoass", "cartoonpornvideos", "DinoTube", "EbonyGalore", "el-ladies", "ForHerTube", "fucd", "gaymaletube", "GotPorn", "HDPorzo", "HomemadeGalore", "iXXX", "LatinGalore", "LesbianPornVideos", "LobsterTube", "LupoPorno", "MatureTube", "MetaPorn", "PornHD", "Porzo", "Qorno", "SambaPorno", "stocking-tease", "TGTube", "Tiava", "toroporno", "TubeBDSM", "TubeGalore", "tubepornstars", "VRXXX"]

if not 1 <= site_setting <= 3:
    site_setting = 1

if percent_included > 100:
    percent_included = 100
elif percent_included < 0:
    percent_included = 1

if full_random_setting:
    site_setting = 2
    filter_by_category = False
    rand_page = True
    percent_included = 100

for i in range(times):
    if site_setting == 2:
        url = "https://www."+sites[ran.randint(0,len(sites)-1)]+".com"
    elif site_setting == 3:
        url = "https://www."+prefered_sites[ran.randint(0,len(prefered_sites)-1)]+".com"
    print(url)
    
    if not filter_by_category:
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        cards = soup.find_all("div", class_="card")
        random_index = ran.randint(0, int(round(len(cards)*(percent_included/100),0)) - 1)
        print(str(percent_included)+"% or "+ str(int(round(len(cards)*(percent_included/100),0))) + " categories & videos")
        random_card = cards[random_index]
        first_a_element = random_card.a
        link_href = first_a_element.get("href")
        print(random_card.div.a.h3.get("title"))
        chosen_cat = url+link_href
    
    if filter_by_category:
        chosen_cat = url+"/category/"+cat
        print(cat)
    
    if rand_page:
        chosen_page = str(ran.randint(0,percent_included))
        chosen_cat = chosen_cat+"?page="+chosen_page
        print("Page "+chosen_page)
        
    page = requests.get(chosen_cat).text
    soup = BeautifulSoup(page, "lxml")
    cards = soup.find_all("div", class_="card sub")
    random_index = ran.randint(0, int(round(len(cards)*(percent_included/100),0)) - 1)
    if rand_page:
        random_index = ran.randint(0, len(cards) - 1)
    random_card = cards[random_index]
    first_a_element = random_card.div.a
    vid = first_a_element.get("href")
    thumbnail = Image.open(BytesIO(requests.get(random_card.img.get("src")).content))
    thumbnail.show()
    print(random_card.h3.get("title"))
    print(url+vid+"\n")