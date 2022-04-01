import math

def solution(price, grade):
    print(type(price), type(grade))
    if grade == "V":
        answer = int(float(price) * 0.85)
    elif grade == "G":
        answer = int(float(price) * 0.9)
    elif grade == "S":
        answer = int(float(price) * 0.95)

    # Write code here.
    # answer = 0
    return answer

# The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
