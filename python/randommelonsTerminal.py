#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 00:36:00 2023

@author: marwanGPT
"""
import random as ran
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

#i made this in schitcho skitso szkitcho mode from 2 to 5 am
#This version is ment to be run in a terminal. to run you open the terminal and put python filepath/file.py
print("This is a program that automatically picks a video from the porn aggragation sites from the fuq network")
print("For next video type 'Enter'. For multiple videos type 'repeat num' or 'xnum'. For settings type 'settings'")

site_setting = 1 #1=normal 1 site 2=fully random site 3=prefered sites
url = "https://www.melonstube.com" 
percent_included = 20
full_random_setting = False
filter_by_category = False
cat = "beauty"

prefered_sites = ["melonstube", "fuq", "assoass", "cartoonpornvideos", "DinoTube", "forhertube", "fucd", "GotPorn", "HDPorzo", "HomemadeGalore", "iXXX", "LatinGalore", "LesbianPornVideos", "LobsterTube", "LupoPorno", "MetaPorn", "PornHD", "Porzo", "Qorno", "SambaPorno", "stocking-tease", "Tiava", "toroporno", "TubeGalore", "tubepornstars"]
sites = ["melonstube", "fuq", "analgalore", "asiangalore", "assoass", "cartoonpornvideos", "DinoTube", "EbonyGalore", "el-ladies", "ForHerTube", "fucd", "gaymaletube", "GotPorn", "HDPorzo", "HomemadeGalore", "iXXX", "LatinGalore", "LesbianPornVideos", "LobsterTube", "LupoPorno", "MatureTube", "MetaPorn", "PornHD", "Porzo", "Qorno", "SambaPorno", "stocking-tease", "TGTube", "Tiava", "toroporno", "TubeBDSM", "TubeGalore", "tubepornstars", "VRXXX"]


user_input = ""
while user_input == "":
    user_input = input().lower()
        
    if user_input == "settings":
        done = False
        while not done:
            settings = ["1-site setting: (1=normal 1 site 2=fully random site 3=prefered sites)", site_setting, "2-url:", url, "3-category:", cat, "4-percent included:", percent_included, "5-full random setting:", full_random_setting, "6-filter by category:", filter_by_category]
            for setting in settings:
                print(setting)
            change = int(input("What would you like to change? "))
            #for i in range(0, len(settings), 2):
            #    if change == settings[i][:-1]:
            if change == 5:
                full_random_setting = not full_random_setting
            elif change == 6:
                filter_by_category = not filter_by_category
            else:
                change_value = input("What's the new value? ")
                if change == 1:
                    site_setting = int(change_value)
                elif change == 2:
                    url = change_value
                elif change == 3:
                    cat = change_value
                elif change == 4:
                    percent_included = int(change_value)
                    
            if not 1 <= site_setting <= 3:
                site_setting = 1
                
            if percent_included > 100:
                percent_included = 100
            elif percent_included < 0:
                percent_included = 1
                
            if site_setting == 2:
                url = "https://www."+sites[ran.randint(0,len(sites)-1)]+".com"
            elif site_setting == 3:
                url = "https://www."+prefered_sites[ran.randint(0,len(prefered_sites)-1)]+".com"      
            
            if input("Done? \n").lower() == "yes":
                done = True
                user_input = input().lower()
        
    count = 1
    if user_input[:7] == "repeat ":
        count = int(user_input[7:])
        user_input = ""
    try:
        int(user_input[1:])
        if user_input[0] == "x":
            count = int(user_input[1:])
            user_input = ""
    except:
        ""
        
    if user_input != "":
        break
        
    for i in range(count):
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
            page = requests.get(url+link_href).text
        
        if filter_by_category:
            page = requests.get(url+"/category/"+cat).text
            print(cat)
            
        soup = BeautifulSoup(page, "lxml")
        cards = soup.find_all("div", class_="card sub")
        random_index = ran.randint(0, int(round(len(cards)*(percent_included/100),0)) - 1)
        random_card = cards[random_index]
        first_a_element = random_card.div.a
        vid = first_a_element.get("href")
        thumbnail = Image.open(BytesIO(requests.get(random_card.img.get("src")).content))
        thumbnail.show()
        print(random_card.h3.get("title"))
        print(url+vid+"\n")
    count = 1
    
        
        
        
        
        
        
        
        
        
        
        
        
        