# Prob4. stepup

def step_up(n):
    answer = 0
    if (n < 0):
        return 0
    elif n == 0:
        return 1
    else:
        return step_up(n-1) + step_up(n-2) + step_up(n-3)


if __name__ == '__main__':
    print('step-up')
    steps = int(input('오르는 계단 수를 입력하세요 : '))

    methods = step_up(n=steps)

    print('계단 오르는 방법은 %d 가지입니다.' % methods)