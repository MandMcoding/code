#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:00:50 2023

@author: m&mGPT
"""

import random as r

#Input
print('Welcome to Pharmaceutical Drugs Password Generator')
length = int(input('How many words is the password? '))

#Turning the txt file into a list (in order to pick a random word)
with open('prescription_pharmaceutical_drugs_medications_list.txt', 'r') as med_words:
    med_words_list = [word.strip() for word in med_words]

#Making the password by repeadily picking random drugs
password_words = r.sample(med_words_list, length)
password = ''.join(word.capitalize() for word in password_words)

#Output
print(password)
