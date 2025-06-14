#Importing stuff from  config
from config import DEFAULT_STATE,MOVE_SPEED,BOUNCE_BACK
# Creating the  model class
class Model:
    #making a constructor, I guess
    def __init__(self,state=DEFAULT_STATE,frame_index=0,x=0,y=0,direction=0.0,):
        self.state=state
        self.position=(x,y)
        self.direction=direction
        self.frame_index=frame_index
        #setting the maximum number of frames
        self.max_frames=8
# Define getter and setter for state
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, value):
        self._state = value
#the getter and setter for position
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self,value):
        #I'm adding error handling
        if isinstance(value,tuple) and len(value)==2:
          self._position = value
        else:
            raise ValueError('It must be a tuple of (x,y)')
    #making a getter and setter for direction
    @property
    def direction(self,direction):
        return self._direction
    @direction.setter
    def direction(self,value):
        self._direction=value
    
     # Getter and setter for frame index
    @property
    def frame_index(self):
        return self._frame_index
    @frame_index.setter
    def frame_index(self, value):
        self._frame_index = value
    #method to toggle and change position, but none of my gifs walk
    """def update_position(self, screen_limit=800):
        x, y = self._position
        x += MOVE_SPEED
        # adding some boundaries
        if BOUNCE_BACK and x > screen_limit:
            x = 0
        self._position = (x, y)"""
# Logic to increment animation frame index
    def increment_frame(self):
        self.frame_index=(self.frame_index +1) % self.max_frames
# Logic to reset animation frame index
    def reset_frame(self):
        self.frame_index=0
