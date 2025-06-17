#IMPORTING THINGS FROM CONFIG
from config import WINDOW_TITLE,WINDOW_GEOMETRY,BACKGROUND_COLOR,TRANSPARENT_COLOR,ALWAYS_ON_TOP,RESIZABLE
#importing tkinter
import tkinter as tk
#importing the pet class
from core.pet import Pet
#tis is the launch window methd, I'd modify it later to display all three pets
def launch_window(parent):
#creating the main window and the preferences 
 window=tk.Toplevel(parent)
#background and window preferences
 window.title(WINDOW_TITLE)
 window.wm_attributes('-topmost',ALWAYS_ON_TOP)
 window.overrideredirect(True)
#making the window transoarent
 window.configure(bg=BACKGROUND_COLOR)
 window.wm_attributes('-transparentcolor',TRANSPARENT_COLOR)
#location and size of window on screen
 window.geometry(WINDOW_GEOMETRY)
#making it non=resizable
 window.resizable(*RESIZABLE)
#creating an instance of the controller and passing it in the window
 pet=Pet(window)
#must call a method to start the behaviour loop
 pet.start()
#the return function
 return window
