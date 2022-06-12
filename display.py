from vpython import *
from math import *
from mathstuff import *

#title screen
start_screen = canvas(userzoom = True, userpan = True, userspin = True, align = 'left')
start_screen.width = 700
start_screen.height = 850
start_screen.range = 5
start_screen.title = "<h1>Double Pendulum</h1>Welcome! This screen displays all the variables that can be adjusted in the following interactive simulation. Click the start button when you are ready to continue.\n"

base = vec(0,3,0)

brown = vec(0.538, 0.261, 0.000)
axis = cylinder(pos = base + vec(0,0,-1.6), axis = vec(0,0,1.8),radius = 0.2, color=brown, visible=False)
board1 = box(pos = vec(0,0,-1.6),length=2,height=6.5,width=0.6, color=brown, visible=False)

l1 = 2.2
l2 = 2.6
x = 0.9
y = -0.7

s1_start = sphere(radius = .6, pos = base + vec(l1*sin(x), -l1*cos(x), 0),color = color.red, visible=False)
s2_start = sphere(radius = 5.0/12, pos = base + vec(l1*sin(x), -l1*cos(x), 0) + vec(l2*sin(y), -l2*cos(y), 0),color=color.green, visible=False)
b1_start = cylinder(pos = base, axis = vec(l1*sin(x), -l1*cos(x), 0), radius = 0.1,color=color.red, visible=False)
b2_start = cylinder(pos = base + vec(l1*sin(x), -l1*cos(x), 0), axis = vec(l2*sin(y), -l2*cos(y), 0), radius = 0.1,color=color.green, visible=False)

length1_text = text(text='Length 1',
     align='center', color=color.red, pos = base + vec(l1*sin(x), -l1*cos(x), 0) * 0.5, height = 0.2, visible=False)
length1_text.rotate(angle = -0.68, axis = vec(0,0,1), origin = base + vec(l1*sin(x), -l1*cos(x), 0) * 0.5)
length1_text.pos = length1_text.pos + vec(0.1,0.1,0)

length2_text = text(text='Length 2',
     align='center', color=color.green, pos = base + vec(l1*sin(x), -l1*cos(x), 0) + vec(l2*sin(y), -l2*cos(y), 0) * 0.5, height = 0.2, visible=False)
length2_text.rotate(angle = 0.87, axis = vec(0,0,1), origin = base + vec(l1*sin(x), -l1*cos(x), 0) + vec(l2*sin(y), -l2*cos(y), 0) * 0.5)
length2_text.pos = length2_text.pos + vec(-0.1,0.1,0)

mass1_text = text(text='Mass 1',
     align='center', color=color.red, pos = s1_start.pos+vec(1,0,0), height = 0.2, visible=False)

mass2_text = text(text='Mass 2',
     align='center', color=color.green, pos = s2_start.pos-vec(0.9,0,0), height = 0.2, visible=False)

mratio_text = text(text='Mass ratio = Mass 2 / Mass 1', color=color.white, align = 'center', pos = vec(0,-5,0), height = 0.5, visible=False)

arc1 = curve()
arc1.visible = False
for i in range(0,101):
    arc1.append(base + vec(sin(i/100.0*x),-cos(i/100.0*x),0))

arc2 = curve()
arc2.visible = False
for i in range(0,101):
    arc2.append(base + vec(l1*sin(x), -l1*cos(x), 0) + vec(sin(i/100.0*y),-cos(i/100.0*y),0))

angle_marker_1 = cylinder(pos = base, axis = vec(0,-1.4,0), radius = 0.05, color = color.yellow, visible = False)
angle_marker_2 = cylinder(pos = base + vec(l1*sin(x), -l1*cos(x), 0), axis = vec(0,-1.4,0), radius = 0.05, color = color.yellow, visible = False)

angle1_text = text(text = 'Angle 1', align='center', color = color.white, pos = base + vec(-0.6,-1,0),height = 0.2, visible = False)
angle2_text = text(text = 'Angle 2', align='center', color = color.white, pos = base + vec(l1*sin(x), -l1*cos(x), 0) + vec(0.6,-1,0),height = 0.2, visible = False)

axis.visible = True
board1.visible = True
s1_start.visible = True
s2_start.visible = True
b1_start.visible = True
b2_start.visible = True
length1_text.visible = True
length2_text.visible = True
mass1_text.visible = True
mass2_text.visible = True
mratio_text.visible = True
arc1.visible = True
arc2.visible = True
angle_marker_1.visible = True
angle_marker_2.visible = True
angle1_text.visible = True
angle2_text.visible = True

def start_button(b):
    global started
    start_screen.delete()
    start_screen.title = ""
    b.delete()
    started = True
start = button( bind=start_button, text='Start', pos=start_screen.title_anchor )
started = False

while True:
    if started:
        dt = .0005
        rate(2000)

        pendulum_box = canvas(userzoom = False, userpan = False, userspin = False, align = 'left')
        pendulum_box.width = 700
        pendulum_box.height = 850
        pendulum_box.range = 5
        pendulum_box.title = "<h1>Double Pendulum</h1>"

        gg = graph(title = '<b>Phase Diagram, Mass 1</b>', width=420, height=300, xmin = -3, xmax = 3,
                align = 'left', xtitle='Angle (rad)', ytitle='Angular Velocity (rad / s)', ymin = -10, ymax=10, scroll = False)

        gh = graph(title = '<b>Phase Diagram, Mass 2</b>', width=420, height=300, xmin = -3, xmax = 3,
                align = 'left', xtitle='Angle (rad)', ytitle='Angular Velocity (rad / s)', ymin = -10, ymax=10, scroll = False)

        # test curve
        gint = 250 #plotting interval; graph plots 2000 / gint times per second i think
        f1 = gcurve(color=color.red, dot = True, dot_color = color.red, graph = gg, interval = gint) # a graphics curve
        f2 = gcurve(color=color.green, dot = True, dot_color = color.green, graph = gh, interval = gint)
        f1.plot(0,0)
        f2.plot(0,0)

        # pendulum object
        base = vector(0,3,0)

        def f():
            pass

        pendulum_box.append_to_caption('<h3>Intitial Conditions</h3> The units are arbitrary; what matters is the ratios.\n\n')
        pendulum_box.append_to_caption('Length of rod 1:   0.1')
        length1 = slider(min = 0.1, max = 5, value = 2, length = 250, bind = f)
        pendulum_box.append_to_caption('5\n\n')

        pendulum_box.append_to_caption('Length of rod 2:   0.1')
        length2 = slider(min = 0.1, max = 5, value = 2, length = 250, bind = f)
        pendulum_box.append_to_caption('5\n\n')

        pendulum_box.append_to_caption('Mass ratio:          0.1')
        mratio = slider(min = 0.1, max = 10, value = 1, length = 250, bind = f)
        pendulum_box.append_to_caption('10\n\n')

        pendulum_box.append_to_caption('Angle 1:              -𝝅')
        ang1 = slider(min = -pi, max = pi, value = 1, length = 250, bind = f)
        pendulum_box.append_to_caption('𝝅\n\n')

        pendulum_box.append_to_caption('Angle 2:              -𝝅')
        ang2 = slider(min = -pi, max = pi, value = 1, length = 250, bind = f)
        pendulum_box.append_to_caption('𝝅\n\n')

        l1 = length1.value
        l2 = length2.value
        angle1 = ang1.value
        angle2 = ang2.value
        m = mratio.value

        #base
        brown = vec(0.538, 0.261, 0.000)
        axis = cylinder(pos = base + vec(0,0,-1.6), axis = vec(0,0,1.8),radius = 0.2, color=brown)
        board1 = box(pos = vec(0,0,-1.6),length=2,height=6.5,width=0.6, color=brown)

        s1 = sphere(radius = .5, pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0),color = color.red, make_trail = False, retain = 70, trail_radius = .05)
        s2 = sphere(radius = .5, pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0) + vec(l2*sin(angle2), -l2*cos(angle2), 0),color=color.green, make_trail = False, retain = 70, trail_radius = .05)
        b1 = cylinder(pos = base, axis = vec(l1*sin(angle1), -l1*cos(angle1), 0), radius = 0.1,color=color.red)
        b2 = cylinder(pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0), axis = vec(l2*sin(angle2), -l2*cos(angle2), 0), radius = 0.1,color=color.green)

        going = False
        reset_mode = True

        def flip(b):
            global going, reset_mode
            going = not going
            if reset_mode:
                f1.delete()
                f2.delete()
                s1.make_trail = True
                s2.make_trail = True
                reset_mode = False
            if going:
                b.text = "Pause"
                length1.disabled = True
                length2.disabled = True
                mratio.disabled = True
                ang1.disabled = True
                ang2.disabled = True
            else: b.text = "Play"

        but1 = button( bind=flip, text='Start', pos=pendulum_box.title_anchor )

        def reset(b):
            global going, reset_mode, but1, gg, gh, f1, f2
            going = False
            reset_mode = True
            length1.disabled = False
            length2.disabled = False
            mratio.disabled = False
            ang1.disabled = False
            ang2.disabled = False
            s1.make_trail = False
            s1.clear_trail()
            s2.make_trail = False
            s2.clear_trail()
            w1 = 0
            w2 = 0
            but1.text = "Start"
            gg.delete()
            gh.delete()
            gg = graph(title = '<b>Phase Diagram, Mass 1</b>', width=420, height=300, xmin = -3, xmax = 3,
                    align = 'left', xtitle='Angle (rad)', ytitle='Angular Velocity (rad / s)', ymin = -10, ymax=10, scroll = False)
            gh = graph(title = '<b>Phase Diagram, Mass 2</b>', width=420, height=300, xmin = -3, xmax = 3,
                    align = 'left', xtitle='Angle (rad)', ytitle='Angular Velocity (rad / s)', ymin = -10, ymax=10, scroll = False)
            f1 = gcurve(color=color.red, dot = True, dot_color = color.red, graph = gg, interval = gint) # a graphics curve
            f2 = gcurve(color=color.green, dot = True, dot_color = color.green, graph = gh, interval = gint)
            f1.plot(0,0)
            f2.plot(0,0)

        but2 = button( bind=reset, text='Reset', pos=pendulum_box.title_anchor )

        while True:
            if going:
                angle1, angle2, w1, w2 = step(angle1,angle2,w1,w2,l1,l2,1,m)
                if angle1 > pi:
                    angle1 -= 2*pi
                    f1 = gcurve(graph = gg, color=color.red, dot = True, dot_color = color.red)
                if angle1 < -pi:
                    angle1 += 2*pi
                    f1 = gcurve(graph = gg, color=color.red, dot = True, dot_color = color.red)
                if angle2 > pi:
                    angle2 -= 2*pi
                    f2 = gcurve(graph = gh, color=color.green, dot = True, dot_color = color.green)
                if angle2 < -pi:
                    angle2 += 2*pi
                    f2 = gcurve(graph = gh, color=color.green, dot = True, dot_color = color.green)
                f1.plot(pos=(angle1,w1))
                f2.plot(pos=(angle2,w2))

                s1.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)
                b1.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)
                s2.rotate(angle = w2 * dt - w1 * dt, axis = vec(0,0,1), origin = base + vec(l1*sin(angle1), -l1*cos(angle1), 0))
                s2.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)
                b2.rotate(angle = w2 * dt - w1 * dt, axis = vec(0,0,1), origin = base + vec(l1*sin(angle1), -l1*cos(angle1), 0))
                b2.rotate(angle = w1 * dt, axis = vec(0,0,1), origin = base)

            if reset_mode:
                sleep(0.01)
                w1 = 0
                w2 = 0
                l1 = length1.value
                l2 = length2.value
                angle1 = ang1.value
                angle2 = ang2.value
                m = mratio.value
                s1.pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0)
                s2.pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0) + vec(l2*sin(angle2), -l2*cos(angle2), 0)
                b1.axis = vec(l1*sin(angle1), -l1*cos(angle1), 0)
                b2.pos = base + vec(l1*sin(angle1), -l1*cos(angle1), 0)
                b2.axis = vec(l2*sin(angle2), -l2*cos(angle2), 0)
                s1.radius = 0.5/sqrt(m)
                s2.radius = 0.5*sqrt(m)
