#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 00:09:14 2023

@author: m&m VS Googled
"""

#randomized password, but it's made from medical words
import random
"""
num = '0123456789'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '-=[];\'\,./!@#$%^&*()_+{}:"|<>?'
"""

included = ['abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ','0123456789','-=[];\'\,./!@#$%^&*()_+{}:"|<>?']

#Offshoot Challange! I want special characters, but I want to be able to type them on the mac and phone keyboard
#I just typed all the special characters I can on mac and phone
"""
special_mac = '§-=[];\'\`,./±!@#$%^&*()_+{}:"|~<>?'
special_phone = '+x÷=/_€£¥W!@#$%^&*()-\'\":;,?`~\|<>{}[]'
"""
#So the algorithim I need get's the similar characters in both strings
#My implementation
"""
for char in special_mac:
    if char in (special_mac and special_phone):
        print(char, end = "")
special = '+-='
"""
#Google's implementation
"""
def similar_characters(str1, str2):
  result = ""
  for char in str1:
    if char in str2:
      result += char
  return result
print("")
print(similar_characters(special_mac, special_phone))
"""
#They both returned -=[];'\`,/!@#$%^&*()_+{}:"|~<>?
#Offshoot challenge done!


final_included = ''
options = input("Include caps letters, lowercase letters, numbers, special? (1 is yes, 0 is no, 2 for all) ")
length = int(input("How long is the password? "))
for i in range(len(included)):
    if options == '2' or options[i] == '1':
        final_included += included[i]
        
password = ''.join(random.choice(final_included) for _ in range(length))
print(password)