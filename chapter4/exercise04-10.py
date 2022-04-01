import turtle
import sys

num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

def stampTurtle(x, y, num, binary):
    curX = x
    curY = y

    for i in range(len(binary) - 2):
        turtle.goto(curX, curY)
        if num & 1:
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>= 1

if __name__ == "__main__":
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num1 = int(input("숫자를 입력하세요:"))
    num2 = int(input("숫자를 입력하세요:"))
    num3 = num1 & num2

    binary1 = bin(num1)
    binary2 = bin(num2)
    binary3 = bin(num3)

    curX = swidth / 2
    curY = 50
    stampTurtle(curX, curY, num1, binary1)

    curX = swidth / 2
    curY = 0
    stampTurtle(curX, curY, num2, binary2)

    curX = swidth / 2
    curY = -50
    stampTurtle(curX, curY, num3, binary3)

turtle.done()

