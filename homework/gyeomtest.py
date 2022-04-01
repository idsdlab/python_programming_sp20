import turtle
import random
import math


## 클래스 선언 부분 ##
class Shape:  # 부모 클래스
    myTurtle = None
    cx, cy = 0, 0  # 사각형 및 원의 중심점.

    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle')  # 거북이 생성.

    def setPen(self):  # 펜 색상과 두께를 랜덤하게 뽑기
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1, 10)
        self.myTurtle.pensize(pSize)

    def drawShape(self):  # 하위 클래스에서 상속받아서 오버라이딩
        pass


class Rectangle(Shape):  # 자식 클래스
    width, height = [0] * 2

    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)

    def drawShape(self):
        sx1, sy1, sy2 = [0] * 3

        sx1 = self.cx - self.width / 2
        sy1 = self.cy - self.height / 2
        sy2 = self.cy - self.height / 2

        sx1_ = int(sx1)
        sy1_ = int(sy1)
        sy2_ = int(sy2)

        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        a = math.acos((math.pow(sy1_, 2) + math.pow(sx1_, 2) - math.pow(sy2_, 2)) / (2 * sx1_ * sy1_))
        b = math.acos((math.pow(sy1_, 2) + math.pow(sy2_, 2) - math.pow(sx1_, 2)) / (2 * sy1_ * sy2_))
        angle1 = (180 - math.degrees(a))
        angle2 = (180 - math.degrees(b))
        self.myTurtle.forward(sx1)
        self.myTurtle.right(angle1)   #이 부분에서 각도가 왼쪽 으론쪽, 오른쪽 왼쪽 ,왼쪽 왼쪽 이런식으로 움직입니다.
        self.myTurtle.forward(sy1)
        self.myTurtle.right(angle2)
        self.myTurtle.forward(sy2)


## 함수 선언 부분 ##
def screenLeftClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()


## 메인 코드 부분 ##
turtle.title('거북이로 객체지향 사각형  그리기')
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()