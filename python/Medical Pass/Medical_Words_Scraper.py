#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:06:58 2023

@author: m&m
"""
#Scraping medical words from Harvard's Medical Dictionary of Health Terms (https://www.health.harvard.edu/a-through-c)
import requests
from bs4 import BeautifulSoup

web_range = ['ac','di','jp','qz'] #There are 4 pages, that follow the url path .edu/#-through-# so I just made it a list
words = []
for i in range(len(web_range)): #Loop 4 times for the 4 pages.
    url = 'https://www.health.harvard.edu/'+web_range[i][0]+'-through-'+web_range[i][1]
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    
    #This next line is responsible for scraping all the words from each page
    #Every page has each word in bold as a <strong> tag. So by finding all the strong tags we get all the words
    #Then there is some splicing to remove the <strong> tag and the : from each word
    #The words list is appened 4 times, each is an array of all the medical words in that page
    words.append([word.get_text().replace(': ', '') for word in soup.find_all("strong")])
    for j in range (12): #There are 12 unrelated links at the end of each page
        words[i].pop(-1)

#Here we just transfer all the words into a txt file
with open("medical_words_list.txt", "w") as f:
    for group in words:
        for word in group:
            f.write(word+'\n')