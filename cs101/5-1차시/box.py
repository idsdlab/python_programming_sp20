from cs1graphics import *

canvas = Canvas(400, 300)

canvas.setBackgroundColor("light blue")

sq = Square(100)

canvas.add(sq)

sq.setFillColor("blue")

sq.setBorderColor("red")

sq.setBorderWidth(5)

sq.moveTo(200, 200)

sq.rotate(45)


list1 = ["A", "B", "C", "D", "E"]

list1[-1] = list1[2]

list1 = list1[:4]

list1.sort()

list1.append("AA")

list1[list1.index("AA")-1] = list1[3]

print(list1)