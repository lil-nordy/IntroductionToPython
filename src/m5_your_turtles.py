"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Neil Nordquist.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
## >> Final Questions: How to line break in the editor? Google didn't seem to help. Why does the speed not seem to matter
## when I have the speed set to accummulate by an interval of 10 on each iteration of the loop, but doesn't increase at
## all when I set the  speed to accumulate by an interval of 9 on each iteration? strange.
########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

radius = 50
speed = 1
erik = rg.SimpleTurtle('turtle')
erik.paint_bucket = rg.PaintBucket('red')

for k in range(10):
    erik.speed = speed + 10
# speed, integer from 1 - 10 in the doc-string  of the rose-graphics.py file, but seems to respond to much higher numbers
    erik.pen_down()
    erik.draw_circle(radius)
    radius = radius + 5

nate = rg.SimpleTurtle('turtle')
nate.paint_bucket = rg.PaintBucket('green')
speed = 10
nate.left(270)
nate.speed = 1
nate.forward(25)
window.close_on_mouse_click()



