class Car:
    def __init__(self, name="벤츠", speed=0):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

car1, car2 = None, None

car1 = Car("아우디", 0)
car2 = Car(speed=30)

print("%s의 현재 속도는 %d 입니다." % (car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d 입니다." % (car2.getName(), car2.getSpeed()))
