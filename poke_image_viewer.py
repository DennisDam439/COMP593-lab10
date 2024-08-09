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
script_name = inspect.getfile(inspect.currentframe())
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.geometry('600x600')
root.minsize (500,600)
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
root.iconbitmap(os.path.join(script_dir, 'poke_ball.ico'))

# TODO: Create frames
frm = ttk.Frame(root)
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)
frm.grid(sticky = NSEW)


# TODO: Populate frames with widgets and define event handler functions
image_path = os.path.join(script_dir, 'poke_ball.png')
photo = PhotoImage(file=image_path)

lbl_image = ttk.Label(frm, image=photo) ## TO DO 
lbl_image.grid(row=0, padx=10, pady=10, sticky=NS) ## TO DO 

## Create a combo for pokemon selection
cbox_poke_sel =ttk.Combobox(frm, values=poke_api.get_pokemon_names())
cbox_poke_sel.current(0)
cbox_poke_sel.grid(row=1, padx=10, pady=10, sticky=N)


#Create button to set desktop background
def handle_set_desktop(): ## Finish this
  image_path = os.path.join(images_dir, cbox_poke_sel.get() +'.png')
  ctypes.windll.users32.SystemParametersInfoW(20, 0, image_path, 0)

def handle_poke_sel(event):       # Finish this
  pokemon = cbox_poke_sel.get()
  image_path = os.path.join(images_dir, pokemon + 'png')
  if not os.path.exists(image_path):
     image_data = poke_api.get_pokemon_image(pokemon)
     with open(image_path, 'wb') as f:
        f.write(image_data)
photo = PhotoImage(file=image_path)
lbl_image.config(image=photo)
lbl_image.image = photo 

cbox_poke_sel.bind('<<ComboboxSelected>>', handle_poke_sel)

##Create desktop background button
btn_set_desktop = ttk.Button(frm, text= "Set as DESKTOP BACKGROUND", command=handle_set_desktop)
btn_set_desktop.grid(row=2, padx=10, pady=10, sticky=N)



root.mainloop()