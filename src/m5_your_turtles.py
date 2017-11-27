"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Hannah Levine.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  Hannah Levine  with your own name.
########################################################################

########################################################################
# DONE: 2.
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

spongebob = rg.SimpleTurtle('turtle')
spongebob.pen = rg.Pen('yellow', 5)
spongebob.speed = 50  # I made the speed 50.

# The square will be 100 x 100 pixels:
size = 100

# My loop will do the indented code 6 times.  Each time, it draws a square.
for k in range(6):

    # Put the pen down, then draw a square of the given size:
    spongebob.draw_square(size)

    spongebob.pen_up()
    spongebob.right(45)
    spongebob.forward(10)
    spongebob.left(45)

    # Now the code puts the pen down again.
    spongebob.pen_down()

import rosegraphics as rg

window = rg.TurtleWindow()

sandy = rg.SimpleTurtle('turtle')
sandy.pen = rg.Pen('green', 3)
sandy.speed = 30  # I made the speed 30.

# The circle will be 200 x 200 pixels:
size = 200

radius=100
# My loop will do the indented code 19 times.  Each time, it draws a square.
for k in range(19):

    # Put the pen down, then draw a circle of the given size:
    sandy.draw_circle(k)
    radius= radius-1
    sandy.pen_up()

    # Now the code puts the pen down again.
    sandy.pen_down()

window.close_on_mouse_click()
