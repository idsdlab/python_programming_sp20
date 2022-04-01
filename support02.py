import turtle

num1,num2,result = 0,0,0
swidth,sheight = 1000 , 300
curX = 0
curY = 0

def myFunc():
    global curY, curX
    turtle.shape('turtle')
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90) # 거북이의 방향이 위를 보도록 조정

    num1 = int(input("첫번째 숫자 입력"))  # 10진수 입력받기
    num2 = int(input("두번째 숫자 입력"))
    binary1 = bin(num1)  # 이진수로 변환(문자)
    binary2 = bin(num2)
    result = num1 & num2

    curY = 100
    Turtle(binary1, num1)  # 함수 대입
    curY = 0
    Turtle(binary2, num2)  # 함수 대입
    curY = -100
    Turtle(bin(result), result)  # 함수 대입
    turtle.done()

def Turtle(binary,num):
    curX = swidth/2
    for i in range(len(binary)-2): #이진수의 숫자 수 만큼 반복
        turtle.goto(curX,curY) #거북이를 계산된 좌표로 이동
        if num & 1 : #변환한 비트가 1인경우
            turtle.color('red')
            turtle.turtlesize(2)
        else : #변환한 비트가 0인경우
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp() # 도장 찍기
        curX -=50 #x좌표 왼쪽으로 50만큼 이동
        num>>=1 #우측 비트를 이미 표현 했기 때문에 삭제
    print(curY)

def main():
    print("메인함수 실행")
    myFunc()

if __name__ == '__main__':
    main()