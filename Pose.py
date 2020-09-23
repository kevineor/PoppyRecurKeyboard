import time

class ABCDeplacement():
    def execDeplacement(self, robot):
        pass


class Pose(ABCDeplacement):
    _command = []

    """
    def __init__(self, m1, m2, m3, m4, m5, m6, duration=0, sleeping=0):
        self.__init__([duration,m1, m2, m3, m4, m5, m6], sleeping)
    """
    def __init__(self, command, sleeping=0):
        assert(len(command) ==7)
        self._command   = command
        self._sleeping  = sleeping

    def execDeplacement(self, robot):
        robot.send_command(self._command)
        time.sleep(self._sleeping + self._command[0])




class Routine(ABCDeplacement):
    

    def __init__(self,Pose_start, Pose_list):
        self._Pose_start    = Pose_start
        self._Pose_list     = Pose_list

    def execDeplacement(self, robot):
        self._Pose_start.execDeplacement(robot)

        for Pose in self._Pose_list:
            Pose.execDeplacement(robot)


    
class PoseList:
    BasePosture     = Pose([0,0,0,0,0,0,0],0)
    Reverse         = Pose([5,0,0,-90,-90,90,0],10)
    Sky_Watching    = Pose([0,0,0,0,0,0,0],3)
    Le_Plongeur     = Pose([0,0,0,0,0,0,0],2)