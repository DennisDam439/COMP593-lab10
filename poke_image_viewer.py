"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.exists(images_dir):
    os.makedir(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")

# TODO: Set the icon
icon_path = os.path.join(script_dir, 'icon.ico')
root.iconbitmap(icon_path)

# TODO: Create frames


# TODO: Populate frames with widgets and define event handler functions

root.mainloop()