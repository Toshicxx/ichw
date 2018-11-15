import turtle
import math

sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")

mer= turtle.Turtle()
ven= turtle.Turtle()
ear= turtle.Turtle()
mar= turtle.Turtle()
jup= turtle.Turtle()
sat= turtle.Turtle()

planetlist = [mer,ven,ear,mar,jup,sat]
colorlist =["blue","brown","green","red","orange","purple"]
widthlist =[30,60,90,120,140,160]
heightlist =[20,40,60,80,100,120]

def planet(x,b,c):
    x.color(b)
    x.shape("circle")
    x.penup()
    x.goto(c,0)
    x.pendown()

    
for r in range(6):
    pla = planetlist[r]
    col = colorlist[r]
    dis = widthlist[r]
    planet(pla,col,dis)
    
def move(x,height,width):
    if x.ycor() > 0 or (x.ycor() == 0 and x.xcor() > 0):
        xposition = x.xcor() -1
        x.goto(xposition,math.sqrt(height**2*(1-xposition**2/width**2)))
    if x.ycor() < 0 or (x.ycor() == 0 and x.xcor() < 0):
        xposition = x.xcor() +1
        x.goto(xposition,0-math.sqrt(height**2*(1-xposition**2/width**2)))

while True:
    for x in range(6):
        planet = planetlist[x]
        height = heightlist[x]
        width = widthlist[x]
        move(planet,height,width)
