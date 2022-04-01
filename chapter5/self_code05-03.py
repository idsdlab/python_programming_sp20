# self_code05-03.py

num1 = int(input(" *** 숫자를 입력하세요 : "))
isPrime = True

for i in range(2, num1):
    if num1 % i == 0:
        isPrime = False

if isPrime:
    print('%d는 소수입니다.' % num1)
else:
    print('%d는 소수가 아닙니다.' % num1)
