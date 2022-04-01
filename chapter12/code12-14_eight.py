import multiprocessing
import time

class RacingCar:
    carName = ''

    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(16):
            carStr = self.carName + '~~ 달립니다.\n'
            print(carStr, end='')
            time.sleep(0.5)

if __name__ == '__main__':

    car_list = []

    for i in range(8):
        carname = '자동차 ' + str(i)
        car_list.append(carname)

    for carname in car_list:
        car = RacingCar(carname)
        mp = multiprocessing.Process(target=car.runCar)
        mp.start()

    mp.join()