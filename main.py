from PoppyDancer import *
from pypot.creatures import PoppyErgoJr
from Pose import PoseList
import time
"""
poppy = PoppyErgoJr()
poppy.dance.start()
"""
poppy = PoppyDancer()


poppy.choregraphy.AddPose( PoseList.BasePosture     )

poppy.choregraphy.AddPose( PoseList.Posture1        )
poppy.choregraphy.AddPose( RoutineList.BalaisBrosse )

poppy.choregraphy.AddPose( RoutineList.Route2 )
poppy.choregraphy.AddPose( PoseList.Le_Plongeur )
poppy.choregraphy.AddPose( RoutineList.Route3 )
poppy.choregraphy.AddPose( RoutineList.Crabrave )
#poppy.choregraphy.AddPose( RoutineList.HeadBang )
poppy.choregraphy.AddPose( PoseList.Sky_Watching )
poppy.choregraphy.AddPose( RoutineList.Houaaa )

poppy.choregraphy.AddPose( PoseList.BasePosture     )


poppy.choregraphy.start()

time.sleep(5)aphy.AddPose( RoutineList.Houaaa )

poppy.choregraphy.AddPose( PoseList.BasePosture     )

poppy.choregraphy.start()

time.sleep(5)aphy.AddPose( RoutineList.Houaaa )

poppy.choregraphy.AddPose( PoseList.BasePosture     )

poppy.choregraphy.start()

time.sleep(5)