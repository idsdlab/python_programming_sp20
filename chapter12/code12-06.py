class Car:
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1

myCar1, myCar2 = [None] * 2

# print(myCar1, myCar2)

myCar1 = Car()
myCar1.speed = 30

print(Car.count)

myCar2 = Car()
myCar2.speed = 100

print(myCar2.count)
