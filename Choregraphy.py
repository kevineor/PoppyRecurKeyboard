import time
from Pose import *

class Choregraphy():
    _poses = []
    def __init__(self, poppy):
        self._poppy = poppy

    def AddPose(self, p):
        self._poses.append(p)



   # def RemovePose(self, i):
        

    def start(self):
        for pose in self._poses:
            pose.execDeplacement(self._poppy)

        #self._poses[0].execDeplacement(self._poppy)


