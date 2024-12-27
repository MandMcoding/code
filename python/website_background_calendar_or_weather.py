from PIL import Image, ImageEnhance, ImageDraw
import numpy as np
from AppKit import NSWorkspace, NSWindow, NSImage, NSScreen

def capture_window_screenshot(window):
    # Get the window frame
    window_frame = window.frame()

    # Calculate the screen coordinates of the window
    screen_rect = NSScreen.mainScreen().frame()
    window_rect = window.convertRectToScreen_(window_frame)
    window_rect.origin.y = screen_rect.size.height - window_rect.origin.y - window_rect.size.height

    # Create an NSImage with the size of the window
    image = NSImage.alloc().initWithSize_(window_rect.size)

    # Set the image as the current graphics context
    image.lockFocus()

    # Capture the window's content
    window.drawViewHierarchyInRect_(window_frame, afterScreenUpdates=True)

    # Unlock the image
    image.unlockFocus()

    # Convert the NSImage to a PIL Image
    pil_image = Image.frombytes("RGB", image.size(), image.TIFFRepresentation())

    # Convert the PIL Image to a numpy array if needed
    screenshot_array = np.array(pil_image)

    return screenshot_array


# Get the shared instance of NSWorkspace
workspace = NSWorkspace.sharedWorkspace()

# Get the running applications
running_apps = workspace.runningApplications()

# Iterate through the running applications
for app in running_apps:
    # Get the application's windows
    windows = app.windows()

    # Iterate through the windows
    for window in windows:
        # Capture a screenshot of the window
        screenshot = capture_window_screenshot(window)

        # Process the screenshot as needed
        # ...

        break  # Break the loop after capturing the first window of each application
