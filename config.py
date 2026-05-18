# config.py
from pathlib import Path

# Paths
PATH_TO_IMAGES = Path(r'G:\subwAI\images\training')
PATH_TO_IMAGES2 = Path(r'G:\subwAI\images\training2') #  for flipping all the training images horizontally in order to double the size of the training set
VIDEO_PATH = r'G:\subwAI\recordings\\'
PRELOAD_DIR = Path(r'G:\subwAI\dataset_preloaded')

# Coordinates
GAME = {"top": 337, "left": 673, "width": 573, "height": 603} # location on the screen of where the game will be
PAUSE = {"top": 65, "left": 687, "width": 60, "height": 60} # location of the pause button

# Constants
NUM_CATEGORIES = 5