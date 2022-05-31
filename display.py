from vpython import *
from math import *

pendulum_box = canvas(userzoom = False, userpan = False, userspin = True, align = 'left')
pendulum_box.width = 700
pendulum_box.height = 850
pendulum_box.range = 1.3
pendulum_box.title = "<h1>Double Pendulum</h1>"

gg = graph( width=750, height=500, xmin = -pi, xmax = pi, align = 'left', xtitle='speed, m/s', ytitle='Number of atoms', ymax=10)
f1 = gcurve(color=color.cyan) # a graphics curve
for x in arange(0, 8.05, 0.1): # x goes from 0 to 8
    f1.plot( x,5*cos(2*x)*exp(-0.2*x) )


box_object = box(canvas = pendulum_box)
