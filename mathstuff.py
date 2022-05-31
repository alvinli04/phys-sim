from math import *

length1 = 1
length2 = 0.9
mass1 = 1
mass2 = 2
angle1 = 0.5
angle2 = -0.3
w1 = 0
w2 = 0


def step(x1, x2, w1, w2, l1, l2, m1, m2):
    dt = 0.002
    g = 9.8

    a1 = (-g*(2*m1+m2)*sin(x1)-g*m2*sin(x1-2*x2)-2*m2*sin(x1-x2)*(w2*w2*l2+w1*w1*l1*cos(x1-x2)))/(l1*(2*m1+m2-m2*cos(2*x1-2*x2)))
    a2 = (2*sin(x1-x2)*(w1*w1*l1*(m1+m2)+g*(m1+m2)*cos(x1)+w2*w2*l2*m2*cos(x1-x2)))/(l2*(2*m1+m2-m2*cos(2*x1-2*x2)))

    x1 += dt * w1
    x2 += dt * w2

    w1 += dt * a1
    w2 += dt * a2

    return x1, x2, w1, w2


for i in range(0,1000):
    angle1, angle2, w1, w2 = step(angle1,angle2,w1,w2,length1,length2,mass1,mass2)
    print(angle1, angle2)
