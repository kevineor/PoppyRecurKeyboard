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
    #command = [duration,m1, m2, m3, m4, m5, m6]
    def __init__(self, command, sleeping=0):
        assert(len(command) ==7)
        self._command   = command
        self._sleeping  = sleeping

    def execDeplacement(self, robot):
        robot.send_command(self._command)
        print("flagP")
        time.sleep(self._sleeping)




class Routine(ABCDeplacement):
    

    def __init__(self,Pose_start, Pose_list):
        self._Pose_start    = Pose_start
        self._Pose_list     = Pose_list

    def execDeplacement(self, robot):
        self._Pose_start.execDeplacement(robot)
        print("")
        for Pose in self._Pose_list:
            print("flagR")
            Pose.execDeplacement(robot)


    
class PoseList:
    BasePosture     = Pose( [ 1 , 0     , 0     , 0     , 0         , 0 ,0 ], 1+1 )
    Posture1        = Pose( [ 1 , 180   , 0     , 90    , 90       , 90 ,0 ], 1+3 )

    Reverse         = Pose( [ 1   , 0 , 0, -90, -90   , 90,0 ], 3 )
    Sky_Watching    = Pose( [ 1   , 0 , 0, 0  , 0     , 0 ,0 ], 3 )
    Le_Plongeur     = Pose( [ 1   , 0 , 0, 0  , 0     , 0 ,0 ], 2 )

class RoutineList:
    BalaisBrosse    = Routine   (   Pose(       [ 2, 0      , 75, 0, -90 , 90, 0], 2 )
                                ,   [    
                                        Pose(   [ 1, 90     , None, 0, -90 , 90, 0], 1 )
                                    ,   Pose(   [ 2, -90    , None, 0, -90 , 90, 0], 2 )
                                    ,   Pose(   [ 2, 90     , None, 0, -90 , 90, 0], 2 )
                                    ,   Pose(   [ 2, -90    , None, 0, -90 , 90, 0], 2 )
                                    ,   Pose(   [ 1, 0      , None, 0, -90 , 90, 0], 1 )
                                    ])
    Route2    = Routine   (   Pose(       [ 1, -180  , 0, 0, 0, 0, 0], 1 )
                                ,   [    
                                        Pose(   [ 5, 180  , None, None, None, None, None], 0 )
                                    ,   Pose(   [ 1, None  , None, None, None, -90, None], 1 )
                                    ,   Pose(   [ 1, None  , None, None, None, 0, None], 1 )
                                    ,   Pose(   [ 1, None  , None, None, None, -90, None], 1 )
                                    ,   Pose(   [ 1, None  , None, None, None, 0, None], 1 )
                                    ,   Pose(   [ 1, None  , None, None, None, -90, None], 1 )
                                    ,   Pose(   [ 1, None  , None, None, None, 0, None], 1 )
                                    ])
    Route3    = Routine   (   Pose(       [ 1, -180  , 90, 0, 180, -90, 0], 1 )
                                ,   [    
                                        Pose(   [ 1, None  , 0, 90, None, 90, None], 1 )
                                    ])
    Crabrave    = Routine   (   Pose(       [ 1, 180  , 90, -45, 180, -45, 0], 1 )
                                ,   [    
                                        Pose(   [ 1, 45  , None, None, -45+90, None, None], 1 )
                                    ,   Pose(   [ 1, -45  , None, None, 45+90, None, None], 1 )
                                    ,   Pose(   [ 1, 45  , None, None, -45+90, None, None], 1 )
                                    ,   Pose(   [ 1, -45  , None, None, 45+90, None, None], 1 )
                                    ,   Pose(   [ 1, 45  , None, None, -45+90, None, None], 1 )
                                    ,   Pose(   [ 1, -45  , None, None, 45+90, None, None], 1 )
                                    ,   Pose(   [ 1, 45  , None, None, -45+90, None, None], 1 )
                                    ,   Pose(   [ 1, -45  , None, None, 45+90, None, None], 1 )
                                    ,   Pose(   [ 1, 180  , 90, -45, 180, -45, 0], 1 )
                                    ])

    HeadBang    = Routine   (   Pose(       [ 1, 180  , 0, -90, 0, -90, 0], 1 )
                                ,   [
                                        Pose(   [ 5/3, None  , None , -45 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -45 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , -45  , None, None, None, None], 0.3/3 )
                                    #1
                                    ,   Pose(   [ 5/3, None  , -45   , None, None, None, None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , None , -90 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -90 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , 0    , None, None, None, None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , None , -45 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -45 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , -45   , None, None, None, None], 0.3/3 )
                                    #2
                                    ,   Pose(   [ 5/3, None  , None , -90 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -90 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , 0    , None, None, None, None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , None , -45 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -45 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , -45   , None, None, None, None], 0.3/3 )
                                    #3
                                    ,   Pose(   [ 5/3, None  , None , -90 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -90 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , 0    , None, None, None, None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , None , -45 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -45 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , -45   , None, None, None, None], 0.3/3 )
                                    #4
                                    ,   Pose(   [ 5/3, None  , None , -90 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -90 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , 0    , None, None, None, None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , None , -45 , None, None, None], 0.4/3 )
                                    ,   Pose(   [ 5/3, None  , None , None, None, -45 , None], 0.3/3 )
                                    ,   Pose(   [ 5/3, None  , -45   , None, None, None, None], 0.3/3 )
                                    #5
                                    ])
    Houaaa    = Routine   (   Pose(       [ 1, 180  , 0, -90, 0, 90, 0], 1 )
                                ,   [    
                                        Pose(   [ 8, -180  , None, None, None, None, None], 0 )
                                    ,   Pose(   [ 1, None  , None, -90, 90, None, None] , 1 )
                                    ,   Pose(   [ 1, None  , None, 90, -180, None, None], 1 )
                                    ,   Pose(   [ 1, None  , None, -90, 90, None, None] , 1 )
                                    ,   Pose(   [ 1, None  , None, 90, -180, None, None], 1 )
                                    ,   Pose(   [ 1, None  , None, -90, 90, None, None] , 1 )
                                    ,   Pose(   [ 1, None  , None, 90, -180, None, None], 1 )
                                    ,   Pose(   [ 1, None  , None, -90, 90, None, None] , 1 )
                                    ,   Pose(   [ 1, None  , None, 90, -180, None, None], 1 )
                                    ])