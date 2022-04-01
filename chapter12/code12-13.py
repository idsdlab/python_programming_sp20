import threading
import time

class RacingCar:
    carName = ''

    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(8):
            carStr = self.carName + '~~ 달립니다.\n'
            print(carStr, end='')
            time.sleep(1)

if __name__ == '__main__':
    car_list = []
    th = []

    for i in range(8):
        carname = '자동차 ' + str(i)
        car_list.append(carname)

    for carname in car_list:
        car = RacingCar(carname)
        th = threading.Thread(target=car.runCar)
        th.start()