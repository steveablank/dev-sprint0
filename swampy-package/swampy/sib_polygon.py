# Polygon excercise from Week 0

# Name: Steve Blank

from TurtleWorld import *                 
world = TurtleWorld()                        
bob = Turtle()                                


# This is where you put code to move bob

import math

def square(turtle, n, l):
 for i in range (n):
        fd (turtle, l)
        lt(turtle)

def polyline(t, n, l, a):
        for i in range (n):
         fd(t, l)
         lt(t, a)

def polygon (t, n, l):
        a = 360.0 / n
        polyline(t, n, l, a)

def circle(t , r):
        circumference = 2 * math.pi * r
        n = int (circumference / 3) +1
        l = circumference / n
        polygon (t, n, l)

def arc (t , r, angle):
        arc_length = 2 * math.pi * r * angle/360
        n = int (arc_length / 3) +1
        step_length = arc_length / n
        step_angle = float(angle) / n

        for i in range (n):
                fd (t, step_length)
                lt (t, step_angle)

bob.delay = 0.01

#moves bob to the left
pu(bob)
bk(bob, 150)
pd(bob)

#call square function
square(bob, 4, 75)

pu(bob)
fd(bob, 100)
pd(bob)

#calls polygon function
polygon(bob, 6, 30)

pu(bob)
fd(bob, 75)
pd(bob)

circle(bob, 25)

pu(bob)
fd(bob, 40)
pd(bob)

arc( bob, 40, 180)

wait_for_user()  