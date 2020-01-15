from enum import Enum 
# Creating the Start and End for the executable window
class GameState(Enum):
    NONE = 0
    RUNNING = 1,
    ENDED = 2