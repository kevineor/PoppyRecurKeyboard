from pypot.creatures import PoppyErgoJr
import time

poppy = PoppyErgoJr()

poppy.dance.start()

time.sleep(5)
poppy.dance.stop()
time.sleep(5)