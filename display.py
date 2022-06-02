from vpython import *
from math import *
from mathstuff import *

dt = .002

pendulum_box = canvas(userzoom = False, userpan = False, userspin = True, align = 'left')
pendulum_box.width = 700
pendulum_box.height = 850
pendulum_box.range = 5
pendulum_box.title = "<h1>Double Pendulum</h1>"

gg = graph(title = '<b>Phase Diagram</b>', width=750, height=500, xmin = -3, xmax = 3,
            align = 'left', xtitle='Angle (rad)', ytitle='Angular Velocity (rad / s)', ymin = -10, ymax=10, scroll = False)

# test curve
f1 = gcurve(color=color.cyan, dot = True, dot_color = color.red) # a graphics curve
f2 = gcurve(color=color.green, dot = True, dot_color = color.purple)

# pendulum object
base = vector(0,3,0)

def f():
    pass

length1 = slider(min = 0.1, max = 5, value = 2, length = 250, right = 50, bottom = 30, bind = f)
length2 = slider(min = 0.1, max = 5, value = 2, length = 250, right = 50, bottom = 30, bind = f)
mratio = slider(min = 0.1, max = 3, value = 1, length = 250, right = 50, bottom = 30, bind = f)

l1 = length1.value
l2 = length2.value
m = mratio.value

s1 = sphere(radius = .5, pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0))
s2 = sphere(radius = .5, pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0) + vec(l2*sin(angle2), -l2*cos(angle2), 0))
# b1 = 

while True:
    rate(500)
    angle1, angle2, w1, w2 = step(angle1,angle2,w1,w2,l1,l2,1,m)
    if angle1 > pi:
        angle1 -= 2*pi
        f1 = gcurve(color=color.cyan, dot = True, dot_color = color.red)
    if angle1 < -pi:
        angle1 += 2*pi
        f1 = gcurve(color=color.cyan, dot = True, dot_color = color.red)
    if angle2 > pi:
        angle2 -= 2*pi
        f2 = gcurve(color=color.green, dot = True, dot_color = color.purple)
    if angle2 < -pi:
        angle2 += 2*pi
        f2 = gcurve(color=color.green, dot = True, dot_color = color.purple)
    f1.plot(pos=(angle1,w1))
    f2.plot(pos=(angle2,w2))

    s1.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)
    s2.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)
    s2.rotate(angle = w2 * dt - w1 * dt, axis = vec(0,0,1), origin = base + vec(l1*sin(angle1), -l1*cos(angle1), 0))

    # print(angle1, w1)
