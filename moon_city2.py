from turtle import *

def star(x,y,ps,col,f,tilt): #отрисовка звёзд
    left(tilt)
    penup()
    goto(x,y)
    color(col)
    begin_fill()
    pendown()
    pensize(ps)
    for i in range (5):
        left(36)
        forward(f)
        left(180)
    end_fill()
    penup()

def house(x,y,width,height,col): #отрисовка дома
    penup()
    goto(x,y)
    color(col)
    pendown()
    begin_fill()
    for i in range(2):
        left(90)
        forward(width)
        left(90)
        forward(height)
    end_fill()
    penup()

def window(x,y):
    penup()
    goto(x,y)
    color('lightblue')
    begin_fill()
    pendown()
    for i in range(4):
        forward(40)
        left(90)
    end_fill()
    penup()
    pensize(5)
    goto(x,y)
    color('burlywood')
    pendown()
    for i in range(4):
        forward(40)
        left(90)
    
    left(90)
    forward(20)
    right(90)
    forward(40)
    left(90)
    forward(20)
    left(90)
    forward(20)
    left(90)
    forward(40)
    right(90)
    forward(20)
    left(180)
    penup()

def windows():
    window(-85,-25) # y-60
    window(-25,-25)

    window(-85,-85)
    window(-25,-85)

    window(-85,-145)
    window(-25,-145)


def moon(): #отрисовка луны
    color('white')
    goto(160,140)
    pendown()
    begin_fill()
    circle(35)
    end_fill()
    penup()
    goto(191,155)
    color('darkblue')
    begin_fill()
    pendown()
    circle(21)
    end_fill()

def sky(): #отрисовка всего неба
    background()
    moon()
    star(95,160,1,'yellow',25,12)
    star(45,140,1,'yellow',25,12)
    star(5,170,1,'yellow',25,12)
    star(-95,135,1,'yellow',25,12)
    star(-5,120,1,'yellow',25,12)
    star(-135,190,1,'yellow',25,52)

def background(): #отрисовка отрисовка фона
    penup()
    color('darkblue')
    begin_fill()
    goto(-300,300)
    pendown()
    for i in range(4):
        forward(600)
        right(90)
    end_fill()
    penup()

def grass(): #отрисовка травы
    goto(-300,-300)
    color('green')
    pendown()
    begin_fill()
    right(112)
    forward(600)
    left(90)
    forward(100)
    left(90)
    forward(600)
    left(90)
    forward(100)
    end_fill()
    
def petal(size,col_petal,tilt): #отрисовка одного лепестка цветочка
    for i in range(col_petal):
        circle(size)
        size += 3


def flower(ps,col,x,y,size,col_petal,tilt): #отрисовка одного цветочка
    penup()
    pensize(ps)
    color(col)
    goto(x,y)
    pendown()
    begin_fill()
    left(tilt)
    for i in range(4):
        petal(size,col_petal,tilt)
        left(90)
    end_fill()
    penup()

def city():
    house(-180,-200,120,260,'saddlebrown')
    house(-140,-230,125,255,'sienna')
    house(-100,-260,130,250,'peru')
    windows()
    penup()
    goto(-85,-205)
    color('chocolate')
    pendown()
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(100)
        left(90)
    end_fill()
    penup()

def land(): #отрисовка всей земли
    grass()
    flower(1,'purple',100,-200,7,1,25)
    flower(1,'orange',130,-230,3,2,36)
    flower(1,'lightpink',170,-270,3,4,52)
    flower(1,'lightblue',200,-220,2,2,76)
    right(52+36+25+76)
    city()

def all_art():
    speed(10)
    sky()
    land()
    hideturtle()
