# self_code02-02.py

# ref : https://stackoverflow.com/questions/46262739/stop-python-turtle-onscreenclick-when-drawing/46263029

import turtle
import random

## 함수 선언 부분 ##
def drawShape(x, y):
    global working
    r = random.random()
    g = random.random()
    b = random.random()
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    turtle.pencolor((r, g, b))
    turtle.pendown()
    working = True
    turtle.goto(x, y)
    working = False

def screenLeftClick(x, y):
    # global r, g, b
    global working
    if working == False:
        drawShape(x, y)

def moveShape(x, y):
    global working

    turtle.penup()
    working = True
    turtle.goto(x, y)
    working = False

def screenRightClick(x, y):
    global working
    if working == False:
        moveShape(x, y)

# def screenMidClick(x, y):
#     global r, g, b

pSize = 10
r, g, b = 0.0, 0.0, 0.0
working = False

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
# turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
