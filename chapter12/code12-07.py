class Car:
    speed = 0
    def upSpeed(self, value=0):
        self.speed += value

        print("현재 속도(super class) : %d" % self.speed)


class Sedan(Car):
    def upSpeed(self, value=0):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

        print("현재 속도(sub class) : %d" % self.speed)

class Sonata(Sedan):
    pass

class Truck(Car):
    pass

truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

print("트럭 --> ", end="")
truck1.upSpeed(200)

print("승용차 --> ", end="")
sedan1.upSpeed(200)

print("소나타 --> ", end="")
sonata1.upSpeed(200)


