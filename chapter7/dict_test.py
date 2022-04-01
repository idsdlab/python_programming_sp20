d = {}
d['t'] = 200
d['x'] = 100
d['z'] = 300

for k, v in d.items():
    print(k, v)

foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sides = ['오뎅', '단무지', '김치']



for food, side in zip(foods, sides):
    print(food, ' --> ', side)

# foods = [num for num in range(1,21)]

for cnt, food in enumerate(foods):
    print('%d --> %s' % (cnt, food))