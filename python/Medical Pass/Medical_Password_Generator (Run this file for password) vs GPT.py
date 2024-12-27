#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:53:30 2023

@author: m&m
"""

import random as r

#Input
print('Welcome to Medical Password Generator')
length = int(input('How many words is the password? '))

#Turning the txt file into a list (in order to pick a random word)
password = ''
med_words_list = []
with open('medical_words_list.txt', 'r') as med_words:
    for word in med_words:
        med_words_list.append(word)

#Making the password by repeadily picking random medical words
for i in range(length):
    rand_index = r.randint(1,2053)
    password += med_words_list[rand_index].replace("\n","").capitalize()
    
#output
print(password)

#ChatGPT's implementation (no fair I didn't know thoes special methods!!)
"""
with open('medical_words_list.txt', 'r') as med_words:
    words_list = med_words.read().splitlines()

random_words = r.sample(words_list, length)
capitalized_words = [word.capitalize() for word in random_words]
password = ''.join(capitalized_words)
print(password)
"""