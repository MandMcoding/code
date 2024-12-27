#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:07:56 2023

@author: m&m
"""

#YOUTUBE SPIDER
#I need to make it with selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
URL = 'https://www.youtube.com/@LinusTechTips/channels'
driver = webdriver.Chrome()
driver.get(URL)
driver.implicitly_wait(0.5)

channels = driver.find_elements(By.TAG_NAME, 'ytd-grid-channel-renderer')
for channel in channels:
    print(channel)