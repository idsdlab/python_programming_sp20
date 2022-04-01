# from cs1graphics import *
import cs1graphics

canvas = cs1graphics.Canvas(600, 200)
canvas.setBackgroundColor("light blue")

car = cs1graphics.Layer()
tire1 = cs1graphics.Circle(10, cs1graphics.Point(-20,-10))
tire1.setFillColor('black')
car.add(tire1)
tire2 = cs1graphics.Circle(10, cs1graphics.Point(20,-10))
tire2.setFillColor('black')
car.add(tire2)
body = cs1graphics.Rectangle(70, 30, cs1graphics.Point(0, -25))
body.setFillColor('blue')
body.setDepth(60)
car.add(body)

car.moveTo(50, 150)
canvas.add(car)


for i in range(360):
  car.move(1, 0)
  car.rotate(-1)

canvas.wait()

for i in range(50):
  car.move(2, 0)
for i in range(22):
  car.rotate(-1)
for i in range(50):
  car.move(2,-1)
for i in range(22):
  car.rotate(1)
for i in range(50):
  car.move(2,0)
for i in range(10):
  car.scale(1.05)

canvas.wait()
car.flip(0)
canvas.wait()
car.flip(90)
canvas.wait()
car.flip(180)
canvas.wait()
car.flip(270)

canvas.wait()

canvas.close()
