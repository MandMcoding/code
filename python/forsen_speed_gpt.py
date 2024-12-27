#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:41:13 2023

@author: marwanGPT
"""
import pyautogui#
from PIL import Image, ImageEnhance, ImageDraw
from pync import Notifier
from skimage.metrics import structural_similarity as ssim#
import numpy as np
import time
          #X     Y   W   H
region = (2451, 372, 39, 25)
ssim_threshold = 0.95
reference_image = Image.open("modified_reference_imageg.png")

while True:
    # Capture/process the screen region
    screenshot = pyautogui.screenshot(region=region)
    screenshot = screenshot.convert("L") #Black/White
    screenshot = ImageEnhance.Contrast(screenshot).enhance(10) #Contrast
    draw = ImageDraw.Draw(screenshot)
    draw.rectangle([10, 0, 22, 22], fill="#00000000")
    
    # Compare the similarity between the captured screenshot and the reference image
    similarity = ssim(np.array(screenshot), np.array(reference_image), multichannel=True)
    #instead of ssim #similarity = np.sum(np.abs(screenshot - reference_array)) / np.prod(screenshot.shape)
    
    #instead of pyautogui # Capture the screenshot of the entire screen
    #screenshot = ImageGrab.grab()
    # Crop the screenshot to the timer region
    #timer_screenshot = screenshot.crop(timer_region)

    if similarity >= ssim_threshold:
        Notifier.notify("💀", title="Past 10 minutes!")
        time.sleep(30)
    
    #screenshot.show()
    time.sleep(30)

#Rework| Twitch API -> if live & playing mc: retrive live video frame (forsen/xqc). the difference from then is that instead of a screenshot (whole screen) it's a cropped portion of the video frame.
