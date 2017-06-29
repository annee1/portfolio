from turtle import *

sides = int(input("Enter number of sides:"))
angle = 360/sides
color = input("color")

begin_fill()
pencolor(color)
fillcolor(color)
for sides in range(int(sides)):
    forward(90)
    right(angle)
    forward(100)
    print ("sides:", sides, "angle:", angle)
end_fill()
exitonclick()
