from poppy_ergo_jr import PoppyErgoJr
from pypot.creatures import *
import pypot


class PoppyController:
    def __init__(self):
        self.poppy = PoppyErgoJr(simulator='vrep', scene='poppy_ergo_jr_holder.ttt')

    def send_commands(self, commands) -> None:
        for command in commands:
            self.send_command(command)
            
    
    """
    # Send command to the robot
        param command {
                [0] => motion_duration,
                [1] => motor1_orientation,
                .
                .
                [6] => motor6_orientation
            }
        return True if motion is valid and if it has been executed
    """
    def send_command(self, command) -> bool:
        # Check if command contains 6 motors orientations and motion duration
        if len(command) < 7 :
            return False
        
        # Send rotation request to motors and wait until rotation is executed
        self.poppy.goto_position({'m1':command[1],
                                      'm2':command[2],
                                      'm3':command[3],
                                      'm4':command[4],
                                      'm5':command[5],
                                      'm6':command[6]},
                                      command[0], wait=True)

        
        # Done
        return True
            
    
    # Close VREP CoppeliaSim connection
    def close_connection(self):
        self.poppy.stop_simulation()
        pypot.vrep.close_all_connections()
        

