from turtle import *
t=Turtle()
w=Screen()
w.bgcolor('black')
t.color('green')
points=[[-175,-125],[0,175],[175,-125]]
def mid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)


    
def triangle(points,depth):
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    if depth>0:

        triangle([points[0],mid(points[0],points[1]),mid(points[0],points[2])],depth-1)
        triangle([points[1],mid(points[0],points[1]),mid(points[1],points[2])],depth-1)
        triangle([points[2],mid(points[0],points[2]),mid(points[1],points[2])],depth-1)
        
triangle(points,4)
