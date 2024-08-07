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
import image_lib
import inspect 
import ctypes

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")

# TODO: Set the icon
icon_path = os.path.join(script_dir, 'icon.ico')
root.iconbitmap(icon_path)

# TODO: Create frames
top_frame = Frame(root)
top_frame.pack(fill=X)

middle_frame = Frame(root)
middle_frame.pack(fill=BOTH, expand=True)

bottom_frame = Frame(root)
bottom_frame.pack(fill=X)

# TODO: Populate frames with widgets and define event handler functions
pokemon_label =Label(top_frame, text=  "Select a Pokemon:")
pokemon_label.pack(side=LEFT)

pokemon_combobox =ttk.Combobox(top_frame)
pokemon_combobox['values'] = poke_api.get_getpokemon_names()
pokemon_combobox.pack(side=LEFT)

root.mainloop()