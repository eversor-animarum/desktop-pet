#Importing controller,model and view modules
from .controller import Controller
from .model import Model
from .view import View
#the pet class would encapsulate from model,view and controller
class Pet:
    def __init__(self, root):
        # Create the model
        self.model = Model()
        # Create the view and pass in the root window
        self.view = View(root)
        # Create the controller, connecting model and view
        self.controller = Controller(root,self.model, self.view)
    # starting the behaviour loop method
    def start(self):
        self.controller.behaviour_loop()
# Defining __all__ to explicitly declare public interface
__all__ = ["Pet"]
