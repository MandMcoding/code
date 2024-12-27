#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 00:57:53 2023

@author: marwan
"""

from PIL import Image, ImageEnhance, ImageDraw

# Load the reference image
reference_image = Image.open("Untitled-1.png")  # Replace "reference_image.png" with the path to your reference image

# Convert the reference image to grayscale (black and white)
reference_image = reference_image.convert("L")

contrast_factor = 10  # Adjust the contrast factor as per your requirements

enhancer = ImageEnhance.Contrast(reference_image)
reference_image = enhancer.enhance(contrast_factor)

# Define the coordinates of the transparent box
x1, y1, x2, y2 = 10, 0, 22, 22

# Create a transparent mask with the same size as the screenshot
#mask = Image.new("RGBA", reference_image.size, (0, 0, 0, 0))

# Draw a rectangle on the mask to define the transparent box region
draw = ImageDraw.Draw(reference_image)
draw.rectangle([10, 0, 22, 22], fill="#00000000")

# Apply the mask to the screenshot using the alpha composite operation
#edited_screenshot = Image.alpha_composite(reference_image.convert("RGBA"), mask)
# Apply the mask to the reference image using the paste() method
#reference_image.paste(mask, (0, 0), mask)

# Display the modified reference image
reference_image.show()

# Save the modified reference image to a file
reference_image.save("modified_reference_imageg.png")  # Replace "modified_reference_image.png" with your desired file path

