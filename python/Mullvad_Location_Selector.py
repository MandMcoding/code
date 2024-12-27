#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:15:15 2023

@author: m&m
"""
import random as r
#Mullvad Location Selector
#The final version includes full random and an automatic distance calculator and does random based on either a linear or standard deviation from your location, instead of constant
locations = [
            ['Tirana'],
            ['Adelaide', 'Brisbane', 'Melbourne', 'Perth', 'Sydney'],
            ['Vienna'],
            ['Brussels'],
            ['Sao Paulo'],
            ['Sofia'],
            ['Calgary', 'Montreal', 'Toronto', 'Vancouver'],
            ['Bogota'],
            ['Zagreb'],
            ['Prague'],
            ['Copenhagen'],
            ['Tallinn'],
            ['Helsinki'],
            ['Marseille','Paris'],
            ['Berlin', 'Dusseldorf', 'Frankfurt'],
            ['Athens'],
            ['Hong Kong'], 
            ['Budapest'], 
            ['Dublin'], 
            ['Tel Aviv'],
            ['Milan', 'Rome'],
            ['Osaka', 'Tokyo'],
            ['Riga'],
            ['Luxemburg'],
            ['Chisinau'],
            ['Amsterdam'],
            ['Aukland'],
            ['Skopje'],
            ['Oslo', 'Stavanger'],
            ['Warsaw'],
            ['Lisbon'],
            ['Bucharest'],
            ['Belgrade'],
            ['Singapore'],
            ['Bratislava'],
            ['Johannesburg'],
            ['Madrid'],
            ['Gothenburg', 'Malmo', 'Stockholm'],
            ['Zurich'],
            ['London', 'Manchester'],
            ['Kyiv'],
            ['Dubai'],
            ['Ashburn', 'Atlanta', 'Boston', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Los Angeles', 'Miami', 'New York', 'Phoenix', 'Raleigh', 'Salt Lake City', 'San Jose', 'Seattle', 'Secaucus']
]
  
country = locations[r.randint(0,len(locations)-1)]
print(country[r.randint(0,len(country)-1)]) #Output