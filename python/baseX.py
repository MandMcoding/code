#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 00:45:16 2023

@author: m&m
"""
import math
#base = int(input("Base: "))
start_base = 36
end_base = 10
num = input("Input: ")

if end_base == 0:
    print("0"*num)
if end_base == 10:
    print(int(num, start_base))
if end_base == 2:
    places = math.trunc(math.log(num, 2))
    binary = []
    """temp = num
    string = ""
    places = math.trunc(math.log(temp, 2))
    print(places)
    for i in range(places-1, -1,-1):
        print("Num:"+str(temp))
        print("i:"+str(i)+" i^2:"+str(2**i))
        if temp % 2 == 0:
            string += "1"
        else:
            string += "0"
        temp = temp - (2**i)"""
#if base == 16