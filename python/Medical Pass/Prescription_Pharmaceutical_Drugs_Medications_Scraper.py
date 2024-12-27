#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 18:06:58 2023

@author: m&m
"""
#Scraping drugs from Drugs.com
import requests
from bs4 import BeautifulSoup
import time
import random as r

drugs = []
#drugs.com's file system is aa-zz, so that's why 26x26 loops
a = 'a'
b = 'a'
text = open('DRUGS IM GOING TO TAKE ILLEGIALLY', 'w')
for i in range(26):
    for i in range(26):
        page = requests.get('https://www.drugs.com/alpha/'+a+b+'.html') #Get html
        if not page.history: #If it doesn't have any (like aa or aw) then skip if it redirects
            page = page.text
            soup = BeautifulSoup(page, "lxml")
            drugs_list = soup.select_one('ul.ddc-list-column-2') #get first unordered list
            
            #Writing the words in the page
            if drugs_list:
                drug_links = drugs_list.find_all('a')
                for drug in drug_links:
                    text.write(drug.get_text()+"\n")
                    print(drug.get_text())
        
        #Going to next page. ex. aa-ab or az-ba
        if b != 'z':
            b = chr(ord(b) + 1)
        else:
            b = 'a'
    a = chr(ord(a) + 1)
    time.sleep(r.random()+1) #The site returns an error if you go too fast, so I put a random delay of 1-2 sec

text.close()