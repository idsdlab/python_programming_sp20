NumFirst = 1
NumSec = 100
result = 0

def myFunc():
    global result
    for i in range(NumFirst, NumSec+1):
        PNum = True
        for j in range(NumFirst, i):
            if i % j == 0 :
                PNum = False
                break
        if PNum == True :
            result = result + i

    print("%d 부터 %d 까지의 소수의 합은 %d 입니다"% (NumFirst, NumSec ,result))

def main():
    print("메인함수 시작")
    myFunc()

if __name__ == '__main__':
    main()