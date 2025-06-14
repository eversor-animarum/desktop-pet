#importing the os
import os
#importing tkinter and pillow
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
#from utils.loader import load_animation_frames
from config import ANIMATION_FOLDER, BACKGROUND_COLOR, DEFAULT_FRAME_SIZE, USE_FIXED_SIZE
# Creating the View class
class View:
    #making the constructor
    def __init__(self, root):
        #storing the root window
        self.root = root
        #using a dictionary to store animation frames
        self.animations = {}
        # this is to load the gifs using the utils
        self.load_animations()
        #setting the current state and frame index
        self.current_state = 'newgif'
        self.current_frame_index = 0
        """Commenting these lines of code out to test something"""
        #creating a tkinter label to display the images
        self.label = tk.Label(self.root, bd=0, bg=BACKGROUND_COLOR)
        self.label.place(x=240, y=70)
        # Set initial frame if state exists
        if 'newgif' in self.animations:
            frame = self.animations['newgif'][0]
            self.label.config(image=frame)
            self.label.image = frame
        else:
            print("Warning: 'newgif' state not found in animations.")
            #making everything animate
        self.animate()

# Defining a method to update animation based on state
    def load_animations(self):
        #the path to the assets folder
         assets_path = os.path.join(os.path.dirname(__file__), '..', ANIMATION_FOLDER)
         #so this is to load each frame in the folder
         for filename in os.listdir(assets_path):
             if filename.endswith('gif'):
                 gif_path = os.path.join(assets_path, filename)
                 img = Image.open(gif_path)
                 # Extract state name from filename (remove extension)
                 state = os.path.splitext(filename)[0]
                 # storing it into tkinter photoimage format yahh
                 frames = []
                 for frame in ImageSequence.Iterator(img):
                     frame = frame.convert('RGBA')
                     if USE_FIXED_SIZE:
                         target_size = DEFAULT_FRAME_SIZE
                     else:
                         target_size = frame.size
                     resized = frame.resize(target_size, Image.Resampling.NEAREST)
                     frames.append(ImageTk.PhotoImage(resized))
                 # store the list of frames under the state name
                 self.animations[state] = frames
                 print(f"Loaded animations: {self.animations.keys()}")
         for state, frames in self.animations.items():
             print(f"{state} has {len(frames)} frames")

# This method updates the current frame to be displayed using the controller
    def update_animation(self, state):
        print(f"Updating to state: {state}, Frame index: {self.current_frame_index}")
        #getting the animations
        frames = self.animations.get(state)
        #if the stae doesn't exist
        if not frames:
            return
        #setting the current state
        self.current_state = state
        #getting the current frame to display
        self.current_frame_index %= len(frames)
        #frame= frames[self.current_frame_index]
        #updating the label to show the current frame
        #self.label.image=frame
        #increment of the frame index
        #self.current_frame_index += 1
        #commenting out the old code to see if this would display a single frame
        frame = frames[0]
        self.label.config(image=frame)
        self.label.image = frame

# Define a method to move the pet to new screen coordinates
    def set_position(self, x, y):
        self.label.place(x=x, y=y)

    def animate(self):
        # Get frames of current state
        frames = self.animations.get(self.current_state)
        if not frames:
            return
        self.current_frame_index %= len(frames)
        frame = frames[self.current_frame_index]
        self.label.configure(image=frame)
        self.label.image = frame
        self.current_frame_index += 1
        # Call again after delay
        self.root.after(120, self.animate)

#I'll handle image flipping in the future if the direction is changed
