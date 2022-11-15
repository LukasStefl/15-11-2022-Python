import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk
import turtle
t = turtle.Turtle()

def draw_square(size, x=0, y=0): 
	t.penup() 
	t.goto(x,y) 
	t.pendown() 
	speed = t.speed() 
	t.speed(0)           #speed set at max 
 
	for i in range(4): 
		t.forward(size) 
		t.left(90) 
 
	t.speed(speed)       #speed restored to defaul
t.home(); t.clear() 
d = 300 
while d >=50: 
	draw_square(d) 
	d -= 5  