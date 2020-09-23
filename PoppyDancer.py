import numpy as np

from pypot.creatures import *
from Choregraphy import *

class PoppyDancer(PoppyErgoJr):
    def __init__(self):
        self.choregraphy = Choregraphy()
        PoppyErgoJr.__init__()

    
