from PoppyDancer import *
from pypot.creatures import PoppyErgoJr
from Pose import PoseList
import time
"""
poppy = PoppyErgoJr()
poppy.dance.start()
"""
poppy = PoppyDancer()
poppy.choregraphy.AddPose(PoseList.BasePosture)
time.sleep(5)
poppy.choregraphy.AddPose(PoseList.Reverse)
poppy.choregraphy.start()
time.sleep(5)