from vpython import *
from math import *
from mathstuff import *

dt = .002

pendulum_box = canvas(userzoom = False, userpan = False, userspin = True, align = 'left')
pendulum_box.width = 700
pendulum_box.height = 850
pendulum_box.range = 5
pendulum_box.title = "<h1>Double Pendulum</h1>"

gg = graph(title = '<b>Phase Diagram</b>', width=420, height=300, xmin = -3, xmax = 3,
            align = 'left', xtitle='Angle (rad)', ytitle='Angular Velocity (rad / s)', ymin = -10, ymax=10, scroll = False)

gh = graph(title = '<b>Phase Diagram</b>', width=420, height=300, xmin = -3, xmax = 3,
            align = 'left', xtitle='Angle (rad)', ytitle='Angular Velocity (rad / s)', ymin = -10, ymax=10, scroll = False)

# test curve
f1 = gcurve(color=color.red, dot = True, dot_color = color.red, graph = gg) # a graphics curve
f2 = gcurve(color=color.green, dot = True, dot_color = color.green, graph = gh)

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

#base
brown = vec(0.538, 0.261, 0.000)
axis = cylinder(pos = base + vec(0,0,-1.6), axis = vec(0,0,1.8),radius = 0.2, color=brown)
board1 = box(pos = vec(0,0,-1.6),length=2,height=6.5,width=0.6, color=brown)

s1 = sphere(radius = .5, pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0),color = color.red)
s2 = sphere(radius = .5, pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0) + vec(l2*sin(angle2), -l2*cos(angle2), 0),color=color.green)
b1 = cylinder(pos = base, axis = vec(l1*sin(angle1), -l1*cos(angle1), 0), radius = 0.1,color=color.red)
b2 = cylinder(pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0), axis = vec(l2*sin(angle2), -l2*cos(angle2), 0), radius = 0.1,color=color.green)

going = False

def flip(b):
    global going
    going = not going
    if going: b.text = "Pause"
    else: b.text = "Go"

button( bind=flip, text='Play', pos=pendulum_box.title_anchor )

while True:
    rate(500)

    if going:
        angle1, angle2, w1, w2 = step(angle1,angle2,w1,w2,l1,l2,1,m)
        if angle1 > pi:
            angle1 -= 2*pi
            f1 = gcurve(color=color.red, dot = True, dot_color = color.red)
        if angle1 < -pi:
            angle1 += 2*pi
            f1 = gcurve(color=color.red, dot = True, dot_color = color.red)
        if angle2 > pi:
            angle2 -= 2*pi
            f2 = gcurve(color=color.green, dot = True, dot_color = color.green)
        if angle2 < -pi:
            angle2 += 2*pi
            f2 = gcurve(color=color.green, dot = True, dot_color = color.green)
        f1.plot(pos=(angle1,w1))
        f2.plot(pos=(angle2,w2))

        s1.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)
        b1.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)
        s2.rotate(angle = w2 * dt - w1 * dt, axis = vec(0,0,1), origin = base + vec(l1*sin(angle1), -l1*cos(angle1), 0))
        s2.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)
        b2.rotate(angle = w2 * dt - w1 * dt, axis = vec(0,0,1), origin = base + vec(l1*sin(angle1), -l1*cos(angle1), 0))
        b2.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)

        # print(angle1, w1)
    # else:
    #     l1 = length1.value
    #     l2 = length2.value
    #     m = mratio.value
    #     w1 = 0
    #     w2 = 0
    #     gg.delete()
