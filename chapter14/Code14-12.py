import pygame
import random
import sys
import glob


### 함수 선언 부분 ###
def paintEntity(entity, x, y):
    # global monitor
    monitor.blit(entity, (int(x), int(y)))

def playGame():
    global monitor, ship

    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)

    shipX = swidth / 2
    shipY = sheight * 0.8
    dx, dy = 0, 0

    # 무한 반복함.
    while True:
        (pygame.time.Clock()).tick(50)  # 게임 진행을 늦춰 줌(10~100 정도가 적당)
        monitor.fill((r, g, b))  # 화면 배경 칠하기

        # 키보드나 마우스 이벤트가 들어오는 것을 체크
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:  # <X> 누르면  종료
                pygame.quit()
                sys.exit()

            if e.type in [pygame.KEYDOWN]:
                if e.key == pygame.K_LEFT : dx = -5
                elif e.key == pygame.K_RIGHT: dx = 5
                elif e.key == pygame.K_UP: dy = -5
                elif e.key == pygame.K_DOWN: dy = 5

            if e.type in [pygame.KEYUP]:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                  or e.key == pygame.K_UP or e.key == pygame.K_DOWN :
                  dx, dy = 0, 0

        if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) \
            and (sheight / 2 < shipY + dy and shipY + dy <= sheight - shipSize[1]) :
                shipX += dx
                shipY += dy

        paintEntity(ship, shipX, shipY)

        pygame.display.update()  # 화면 업데이트하기.
        # print('~', end='')  # 게임 진행 확인


### 전역 변수 선언 부분 ###
swidth, sheight = 500, 700  # 화면 크기
monitor = None  # 게임 화면
ship, shipSize = None, 0

### 메인 코드 부분 ###
pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship = pygame.image.load('images/ship02.png')
shipSize = ship.get_rect().size

# monsterImage = [
#     'images/monster01.png',
#     'images/monster02.png',
#     'images/monster03.png',
#     'images/monster04.png',
#     'images/monster05.png',
#     'images/monster06.png',
#     'images/monster07.png',
#     'images/monster08.png',
#     'images/monster09.png',
#     'images/monster10.png'
# ]
# print(monsterImage)

# monsterImage = []
# for filename in glob.glob('images/monster*.png'):
#     # print(filename)
#     monsterImage.append(filename)

monsterImage = glob.glob('images/monster*.png')

print(monsterImage)

sys.exit(0)

monster = None

playGame()
