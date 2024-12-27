#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:25:46 2023

@author: m&m
"""
#Data (today's date, how many days in each month, and a list of the months)
from datetime import date
today = date.today()
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

#Input
print("This is a decimal age calculator\nEnter your birthday:")
bday = [int(input("Day: ")), input("Month: "), int(input("Year: "))]
#If they put a month as a word
if len(bday[1]) >= 3:
    for i in range(12):
        if months[i][slice(len(bday[1]))] == bday[1].lower():
            bday[1] = i+1
            break
bday[1] = int(bday[1])

#Takes in the month and day and returns the day in the year. ex. mar 8 = 67 since 31+28+8
def actual_day(month, day):
    total = 0
    for i in range(month-1):
        total += days_in_month[i]
    return total + day

decimal_date = today.year + actual_day(today.month, today.day) / 365
decimal_bday = bday[2] + actual_day(bday[1], bday[0]) / 365

age = decimal_date - decimal_bday

#Output
print(age)