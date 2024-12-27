#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:20:44 2023

@author: m&m
"""
#There is 1 bug, when there's a word with 2+ repeating letters, it puts a space after the wrong one, like sniff goes snif f or killl is kil ll. I think the best thing is to remove .split and do it normally
#Cow Code
print('COW language translate\nI Thought it\'d be cool to try and make a code out of moos. If you can figure out what it\'s based off comment what you think in the github page!')
#Input
choice = input('For english to cow type english or 1\nFor cow to english type cow or 2\n')
text = input('Enter text: ')

#This is the code from a-z 0-9 to moos
cow_dict = {
    'a': 'moO',
    'b': 'mOooo',
    'c': 'mOoOo',
    'd': 'mOoo',
    'e': 'mo',
    'f': 'mooOo',
    'g': 'mOOo',
    'h': 'moooo',
    'i': 'moo',
    'j': 'moOOO',
    'k': 'mOoO',
    'l': 'moOoo',
    'm': 'mOO',
    'n': 'mOo',
    'o': 'mOOO',
    'p': 'moOOo',
    'q': 'mOOoO',
    'r': 'moOo',
    's': 'mooo',
    't': 'mO',
    'u': 'mooO',
    'v': 'moooO',
    'w': 'moOO',
    'x': 'mOooO',
    'y': 'mOoOO',
    'z': 'mOOoo',
    '0': 'mOOOOO',
    '1': 'moOOOO',
    '2': 'mooOOO',
    '3': 'moooOO',
    '4': 'mooooO',
    '5': 'mooooo',
    '6': 'mOoooo',
    '7': 'mOOooo',
    '8': 'mOOOoo',
    '9': 'mOOOOo',
}
#This creates a bidirectional dictionary
revd=dict([reversed(i) for i in cow_dict.items()]) #Taken from https://stackoverflow.com/questions/3318625/how-to-implement-an-efficient-bidirectional-hash-table
cow_dict.update(revd)


#Translating algorithim (Output)
if choice == 'english' or choice == '1':
    for letter in text: #Turns each letter to it's moo counterpart from the cow dictionary
        try:
            print(cow_dict[letter.lower()], end=(' ')) 
        except KeyError: #Since punctuation isn't in the dictionary, it throws an error, so I just output it if it does.
            print(letter, end=(''))
if choice == 'cow' or choice == '2':
    #This block of code is just to add spaces inbetween words
    res = [i for i in range(len(text)) if text.startswith('  ', i)] #Taken from https://www.geeksforgeeks.org/python-all-occurrences-of-substring-in-string/
    b4space = []
    for index in res:
        i = index-1
        while True:
            if text[i] == ' ' or i == -1:
                break
            i -= 1
        b4space.append(text[i+1:index])
    
    moos = text.split() #Turn moo string into list of moos
    for moo in moos: #Turns each moo to it's letter counterpart from the cow dictionary
        try:
            print(cow_dict[moo], end=(''))
            if not len(b4space) == 0 and moo == b4space[0]: #Adding spaces
                print(end=" ")
                b4space.pop(0)
        except KeyError:
            print(moo, end=(' '))



#Made with 5 less lines, but awful to look/read
"""
b4space = []
if choice == 'cow' or choice == '2':
    res = [i for i in range(len(text)) if text.startswith('  ', i)] #Taken from https://www.geeksforgeeks.org/python-all-occurrences-of-substring-in-string/
    b4space = []
    for index in res:
        i = index-1
        while True:
            if text[i] == ' ' or i == -1:
                break
            i -= 1
        b4space.append(text[i+1:index])
    text = text.split()

for letter in text:
    try:
        print(cow_dict[letter.lower() if ((choice == 'english') or (choice == '1')) else letter], end=(' ' if choice == '1' else ''))
        if not len(b4space) == 0 and letter == b4space[0]: 
            print(end=" ")
            b4space.pop(0)
    except KeyError:
        print(letter, end=('' if (choice == '1') or choice == 'english' else ' '))
"""