import turtle
import random
class Shape:
    myTurtle = None
    cx, cy = 0, 0

    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle')

    def setPen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r,g,b))
        pSize = random.randrange(1, 10)
        self.myTurtle.pensize(pSize)

    def drawShape(self):
        pass

class Rectangle(Shape):
    width, height = [0] * 2
    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)

    def drawShape(self):
        sx1, sy1, sx2, sy2 = [0] * 4

        sx1 = self.cx - self.width / 2
        sy1 = self.cy - self.height / 2
        sx2 = self.cx + self.width / 2
        sy2 = self.cy + self.height / 2

        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)

# 상속을 받아 원, 다각형, 별 구현하기 :
# https://blog.naver.com/PostView.nhn?blogId=icbanq&logNo=221690768541&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
# (직)삼각형
# https://kaliblog.tistory.com/51

class Triangle(Shape):
    pass

class Octagon(Shape):
    pass

class Circle(Shape):
    pass

class Star(Shape):
    pass

def screenLeftClick(x, y):
    randint = random.randint(0, 5)

    if randint == 0:
        tri = Triangle(x, y)
        tri.drawShape()
    elif randint == 1:
        oct = Octagon(x, y)
        oct.drawShape()
    elif randint == 2:
        star = Star(x, y)
        star.drawShape()
    elif randint == 3:
        rect = Rectangle(x, y)
        rect.drawShape()
    else:
        circle = Circle(x, y)
        circle.drawShape()

if __name__ == '__main__':
    turtle.title('거북이로 객체지향 다양한 Shape 그리기')
    turtle.onscreenclick(screenLeftClick, 1)
    turtle.done()

