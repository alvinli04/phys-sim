from vpython import *
from math import *
from mathstuff import *

pendulum_box = canvas(userzoom = False, userpan = False, userspin = True, align = 'left')
pendulum_box.width = 700
pendulum_box.height = 850
pendulum_box.range = 1.3
pendulum_box.title = "<h1>Double Pendulum</h1>"

gg = graph(title = '<b>Phase Diagram</b>', width=750, height=500, xmin = -2*pi, xmax = 2*pi, align = 'left', xtitle='Angle', ytitle='Angular Velocity (rad/s)', ymin = -10, ymax=10)

# test curve
f1 = gcurve(color=color.cyan) # a graphics curve



box_object = box(canvas = pendulum_box)

def f():
    pass

length1 = slider(min = 0.1, max = 5, value = 2, length = 250, right = 50, bottom = 30, bind = f)
length2 = slider(min = 0.1, max = 5, value = 2, length = 250, right = 50, bottom = 30, bind = f)
mratio = slider(min = 0.1, max = 3, value = 1, length = 250, right = 50, bottom = 30, bind = f)

l1 = length1.value
l2 = length2.value
m = mratio.value

while True:
    angle1, angle2, w1, w2 = step(angle1,angle2,w1,w2,l1,l2,1,m)
    f1.plot(pos=(angle1,w1))
    print(angle1, w1)
