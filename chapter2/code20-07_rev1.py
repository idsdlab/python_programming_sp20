# code02-07_rev1.py

import turtle
import random

flag = False

def draw(x, y):
    global flag
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    flag = True
    turtle.goto(x, y)
    flag = False

## 함수 선언 부분 ##
def screenLeftClick(x, y):
    global flag

    if flag == False:
        draw(x,y)

def move(x, y):
    global flag

    flag = True
    turtle.penup()
    turtle.goto(x, y)
    flag = False

def screenRightClick(x, y):
    global flag

    if flag == False:
        move(x, y)

# def screenRightClick(x, y):
#     global flag
#
#     flag = True
#     turtle.penup()
#     turtle.goto(x, y)
#     flag = False

def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()