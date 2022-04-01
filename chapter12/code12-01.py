class Car:
    # __color = ""
    # __speed = 0
    # _color = ""
    # _speed = 0

    def __init__(self, value1=10, value2="빨강"):
        # self._speed = 150
        # self._color = "빨강"
        self._speed = value1
        self._color = value2

    def upSpeed(self, value):
        # self.__speed += value
        if value >= 150:
            self._speed = 150
        else:
            self._speed += value

    def downSpeed(self, value):
        # self.__speed -= value
        self._speed -= value

    def printMessage(self):
        print("시험 출력이다.")


if __name__ == "__main__":
    car = Car()
    print(car._speed)
    # print(car.__color)

    car.upSpeed(10)
    print(car._speed)
    # print(car.__speed)

    car.upSpeed(200)
    print(car._speed)
    print(car._color)

    # car.printMessage()



