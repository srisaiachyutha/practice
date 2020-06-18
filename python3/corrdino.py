import turtle
w=turtle.Screen()
w.bgcolor('black')
t=turtle.getturtle()
t.color('red')
l=[]
t.speed(0)
for i in range(0,360,5):#put 1 and see
    l.append([t.xcor(),t.ycor()])
    t.circle(100,5)#put 1 and see
#print(l)
#t.up()
for i in range(len(l)):
    t.up()
    t.setposition(l[i][0],l[i][1])
    t.down()
    t.setposition(l[i*2%len(l)][0],l[i*2%len(l)][1])
t.hideturtle()   
