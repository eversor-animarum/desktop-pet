#importing the important stuff
import sys
import os
#these imports are for the tray icon and stuff
import threading
import pystray
from PIL import Image
# Adding the root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#IMPORTING THINGS FROM CONFIG
from config import WINDOW_TITLE,WINDOW_GEOMETRY,BACKGROUND_COLOR,TRANSPARENT_COLOR,ALWAYS_ON_TOP,RESIZABLE
#importing tkinter
import tkinter as tk
#importing the pet class
from core.pet import Pet
#this is the function to quite the app
def quit_app(icon,item):
    icon.stop()
    root.quit()
    os._exit(0)
#this sets up the sytem tray icon
def setup_tray():
    try:
        icon_image_path = os.path.join('assets', 'icon.png')  # Make sure icon exists
        image = Image.open(icon_image_path)
    except Exception as e:
        print(f"Tray icon error: {e}")
        return

    def on_exit(icon, item):
        quit_app(icon, item)

    menu = pystray.Menu(
        pystray.MenuItem('Exit', on_exit)
    )

    icon = pystray.Icon("Mochii", image, "Pet Running", menu)
    icon.run()

#creating the main window and the preferences 
root=tk.Tk()
#background and window preferences
root.title(WINDOW_TITLE)
root.wm_attributes('-topmost',ALWAYS_ON_TOP)
#I wanted to make the entire frame transparent but I've not yet figured out how to close the pet app, and so it gets stuck on the screen
#root.attributes('-toolwindow',True)
root.overrideredirect(True)
#making the window transoarent
root.configure(bg=BACKGROUND_COLOR)
root.wm_attributes('-transparentcolor',TRANSPARENT_COLOR)
#location and size of window on screen
root.geometry(WINDOW_GEOMETRY)
#making it non=resizable
root.resizable(*RESIZABLE)
#creating an instance of the controller and passing it in the window
pet=Pet(root)
#must call a method to start the behaviour loop
pet.start()
#running the application
# Starting the tray icon in a different loop
tray_thread = threading.Thread(target=setup_tray, daemon=True)
tray_thread.start()
root.mainloop()
