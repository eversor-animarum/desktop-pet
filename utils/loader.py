# loader.py

# Importing PIL modules to process GIFs
from PIL import Image, ImageTk, ImageSequence

# Define a function to load a GIF and return a list of PhotoImage frames
def load_animation(gif_path, resize_to=None, double_size=False):
    """
    Loads a GIF and returns a list of Tkinter-compatible PhotoImage frames.
    
    Parameters:
        gif_path (str): The file path to the GIF.
        resize_to (tuple): (width, height) to resize frames to. Optional.
        double_size (bool): Whether to double the frame dimensions. Optional.

    Returns:
        List[ImageTk.PhotoImage]: A list of processed frames.
    """
    
    frames = []

    # Open the GIF file using PIL
    with Image.open(gif_path) as img:
        # Iterate through each frame in the image
        for frame in ImageSequence.Iterator(img):
            # Convert each frame to RGBA for transparency
            frame = frame.convert("RGBA")
            
            # Resize frame if specified
            if resize_to:
                frame = frame.resize(resize_to, Image.LANCZOS)
            elif double_size:
                width, height = frame.size
                frame = frame.resize((width * 2, height * 2), Image.LANCZOS)

            # Convert each frame to a Tkinter PhotoImage
            tk_frame = ImageTk.PhotoImage(frame)

            # Append to frames list
            frames.append(tk_frame)

    # Return the processed list of frames
    return frames
