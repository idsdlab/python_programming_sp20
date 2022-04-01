# self-code05-02.py

select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

num1 = int(input(" *** 첫번째 숫자를 입력하세요 : "))
num2 = int(input(" *** 두번째 숫자를 입력하세요 : "))
num3 = int(input(" 더할 숫자를 입력하세요 : "))

for i in range(num1, num2 + 1, num3):
    answer = answer + i
print('%d+...+%d는 %d 입니다.' % (num1, num2, answer))
