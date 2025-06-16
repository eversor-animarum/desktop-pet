from config import IDLE_ANIMATION_STATES, ANIMATION_DELAY
# importing random to randomize the animations
import random
# Creating the controller class
class Controller:
    # creating the constructor and initializing model and root
    def __init__(self, root, model, view):
        self.model = model
        self.view = view
        # this is a counter to prevent the pet from changing states too quickly
        self.state_change_counter = 30
        # initializing the behaviour loop,this made the loop run before the gui could keep up
        #self.behaviour_loop()
    # Defining a method to create the recurring behaviour loop, it'll be called in the main window
    def behaviour_loop(self):
     current_state = self.model.state
     print(f"Looping - Current state: {current_state}, Frame index: {self.model.frame_index}")
    # Update animation frame
     self.model.increment_frame()
     self.view.update_animation(current_state)
    # Change state after countdown
     if self.state_change_counter <= 0:
        new_state = random.choice(IDLE_ANIMATION_STATES)
        self.model.state = new_state
        self.view.update_animation(new_state)
        self.state_change_counter = 30
     else:
        self.state_change_counter -= 1

    # Loop again after delay
     self.view.root.after(ANIMATION_DELAY, self.behaviour_loop)

    # this method will change the pet's animation state
    def change_state(self, new_state):
        self.model.state = new_state

    # making a method for mouse interactions
