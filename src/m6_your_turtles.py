"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Joey Hatfield.
"""
###############################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
bonzibuddy = rg.SimpleTurtle('turtle')
otherturtle = rg.SimpleTurtle('turtle')

window = rg.TurtleWindow()
window.delay(20)

bonzibuddy.pen_up()
bonzibuddy.go_to(rg.Point(-300,-300))
bonzibuddy.pen_down()
bonzibuddy.speed = 10
bonzibuddy.draw_square(600)

for k in range(5):
    bonzibuddy.forward(60)
    bonzibuddy.left(90)
    bonzibuddy.forward(600)
    bonzibuddy.right(90)
    bonzibuddy.forward(60)
    bonzibuddy.right(90)
    bonzibuddy.forward(600)
    bonzibuddy.left(90)

otherturtle.pen_up()
otherturtle.go_to(rg.Point(-300,-300))
otherturtle.speed = 10
otherturtle.pen_down()
otherturtle.left(90)

for k in range(5):

    otherturtle.forward(60)
    otherturtle.right(90)
    otherturtle.forward(600)
    otherturtle.left(90)
    otherturtle.forward(60)
    otherturtle.left(90)
    otherturtle.forward(600)
    otherturtle.right(90)

otherturtle.pen_up()
bonzibuddy.pen_up()

otherturtle.speed = 1
bonzibuddy.speed = 1

otherturtle.go_to(rg.Point(0,0))
bonzibuddy.go_to(rg.Point(0,0))
window.close_on_mouse_click()

