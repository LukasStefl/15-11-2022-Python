import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk
import turtle
  
t = turtle.Turtle()
 
s = int(input("Enter the length of the side of square: "))
 
for _ in range(4):
  t.forward(s)
  t.left(90)
turtle.exitonclick()