# Flower excercise (4.2) from Week 0

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
        arc_length = 3 * math.pi * r * angle/360
        n = int (arc_length / 3) +1
        step_length = arc_length / n
        step_angle = float(angle) / n

        for i in range (n):
                fd (t, step_length)
                lt (t, step_angle)

def arc2 (t , r, angle):
        arc_length = 2 * math.pi * r * angle/360
        n = int (arc_length / 3) +1
        step_length = arc_length / n
        step_angle = float(angle) / n

        for i in range (n):
                
                rt (t, step_angle)
                fd (t, step_length)

def petal (t, r, a):
 for i in range (2):
         arc(t, r, a)
         lt (t, 180 - a)

def flower (t, n, r, a):
        for i in range(n):
                petal (t,r,a)
                lt(t, 360.0/n)

bob.delay = 0.001

#moves bob to the left
pu(bob)
bk(bob, 100)
pd(bob)

flower (bob, 7, 60, 60)

pu(bob)
fd(bob, 110)
pd(bob)

flower (bob, 5, 25, 85)

pu(bob)
fd(bob, 70)
pd(bob)

flower (bob, 15, 85, 15)

wait_for_user()      