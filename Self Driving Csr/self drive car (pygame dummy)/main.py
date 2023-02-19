import pygame
pygame.init()
board = pygame.display.set_mode((1252,696))
road = pygame.image.load('road.png')
car = pygame.image.load('car.png')
clock = pygame.time.Clock()
focal_dis = 40
drive = True
direction = 'up'
camx_offset = 0
camy_offset = 0
x = 45
y = 510
while True:
    # If quit = car stop driving
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    clock.tick(60)
    camx = x + 55 + camx_offset
    camy = y + 3 + camy_offset


    #car move
    go_up = board.get_at((camx, camy - focal_dis))[0]
    go_right = board.get_at((camx + focal_dis, camy))[0]
    go_down = board.get_at((camx, camy + focal_dis))[0]
    print(go_up,go_down,go_right)


    # turn car
    if direction == 'up' and go_up == 125 and go_down == 72 and go_right == 123:
        direction = 'right'
        y=y-47
        camx_offset = 45
        camy_offset = 50
        car = pygame.transform.rotate(car, -90)

    if direction == 'right' and go_up == 124 and go_down == 124 and go_right == 127:
        direction = 'down'
        x = x+38
        camx_offset = 0
        camy_offset = 95
        car = pygame.transform.rotate(car, -90)

    if direction == 'down' and go_up == 61 and go_down == 53 and go_right == 126:
        direction = 'right'
        y = y + 38
        camx_offset = 45
        camy_offset = 50
        car = pygame.transform.rotate(car, +90)

    if direction == 'right' and go_up == 126 and go_down == 126 and go_right == 73:
        direction = 'up'
        x = x + 40
        camx_offset = 0
        camy_offset = 5
        car = pygame.transform.rotate(car, +90)

    if direction == 'up' and go_up == 52 and go_down == 247 and go_right == 126:
        direction = 'left'
        y = y - 35
        camx_offset = -50
        camy_offset = 50
        car = pygame.transform.rotate(car, +90)

    if direction == 'left' and go_up == 121 and go_down == 121 and go_right == 70:
        direction = 'up'
        camx_offset = 0
        camy_offset = 5
        car = pygame.transform.rotate(car, -90)

    if direction == 'up' and go_up == 52 and go_down == 247 and go_right == 125:
        direction = 'right'
        y = y - 35
        camx_offset = 46
        camy_offset = 50
        car = pygame.transform.rotate(car, -90)

    if direction == 'right' and go_up == 126 and go_down == 126 and go_right == 101:
        direction = 'down'
        x = x + 35
        camx_offset = 0
        camy_offset = 94
        car = pygame.transform.rotate(car, -90)

    if direction == 'down' and go_up == 0 and go_down == 125 and go_right == 126:
        direction = 'left'
        y = y + 40
        camx_offset = -50
        camy_offset = +48
        car = pygame.transform.rotate(car, -90)


    # drive car
    if (go_right == 126 and go_down == 72 and go_up == 125) or (go_right == 126 and go_down == 72 and go_up == 124) or (go_right == 126 and go_down == 72 and go_up == 126) or (go_right == 124 and go_down == 72 and go_up == 125) or (go_right == 124 and go_down == 72 and go_up == 129) or (go_right == 125 and go_down == 72 and go_up == 125):
        y = y - 4
    elif direction == 'right' and ((go_up == 124 and go_down == 124 and go_right == 125) or (go_up == 125 and go_down == 128 and go_right == 125) or (go_up == 124 and go_down == 52 and go_right == 124) or (go_up == 124 and go_down == 52 and go_right == 125) or (go_up == 124 and go_down == 55 and go_right == 125) or (go_up == 125 and go_down == 52 and go_right == 125) or (go_up == 126 and go_down == 52 and go_right == 125) or (go_up == 126 and go_down == 52 and go_right == 124) or (go_up == 126 and go_down == 52 and go_right == 125) or (go_up == 125 and go_down == 52 and go_right == 126) or (go_up == 124 and go_down == 52 and go_right == 126) or (go_up == 125 and go_down == 52 and go_right == 124) or (go_up == 126 and go_down == 52 and go_right == 126) or (go_up == 124 and go_down == 51 and go_right == 126) or (go_up == 125 and go_down == 126 and go_right == 126) or (go_up == 126 and go_down == 125 and go_right == 126) or (go_up == 125 and go_down == 125 and go_right == 126) or (go_up == 125 and go_down == 125 and go_right == 125) or (go_up == 125 and go_down == 125 and go_right == 124) or (go_up == 124 and go_down == 125 and go_right == 125) or (go_up == 125 and go_down == 126 and go_right == 124) or (go_up == 124 and go_down == 126 and go_right == 124) or (go_up == 125 and go_down == 126 and go_right == 125) or (go_up == 126 and go_down == 126 and go_right == 125) or (go_up == 126 and go_down == 126 and go_right == 124)):
        x = x + 3
    elif direction == 'down' and ((go_up == 124 and go_down == 124 and go_right == 127) or (go_up == 61 and go_down == 125 and go_right == 125) or (go_up == 61 and go_down == 125 and go_right == 126) or (go_up == 61 and go_down == 126 and go_right == 125) or (go_up == 61 and go_down == 126 and go_right == 124) or (go_up == 61 and go_down == 126 and go_right == 126)or (go_up == 61 and go_down == 125 and go_right == 124) or (go_up == 61 and go_down == 128 and go_right == 126)):
        y = y + 3
    elif direction == 'right' and ((go_up == 61 and go_down == 53 and go_right == 126) or (go_up == 121 and go_down == 120 and go_right == 126) or (go_up == 126 and go_down == 126 and go_right == 126) or (go_up == 124 and go_down == 124 and go_right == 126) or (go_up == 124 and go_down == 125 and go_right == 126) or (go_up == 126 and go_down == 124 and go_right == 126)):
        x = x + 3
    elif direction == 'up' and ((go_up == 126 and go_down == 126 and go_right == 73) or (go_up == 126 and go_down == 126 and go_right == 247) or (go_up == 126 and go_down == 124 and go_right == 126) or (go_up == 126 and go_down == 247 and go_right == 126) or (go_up == 126 and go_down == 247 and go_right == 125) or (go_up == 54 and go_down == 247 and go_right == 126) or (go_up == 52 and go_down == 247 and go_right == 126)):
        y = y - 4
    elif direction == 'left' and ((go_up == 52 and go_down == 247 and go_right == 126) or (go_up == 126 and go_down == 126 and go_right == 70) or (go_up == 124 and go_down == 126 and go_right == 70) or (go_up == 125 and go_down == 126 and go_right == 70) or (go_up == 126 and go_down == 124 and go_right == 70) or (go_up == 126 and go_down == 125 and go_right == 70)):
        x = x - 4
    elif direction == 'up' and ((go_up == 121 and go_down == 121 and go_right == 70) or (go_up == 124 and go_down == 247 and go_right == 126) or (go_up == 125 and go_down == 247 and go_right == 126) or (go_up == 125 and go_down == 247 and go_right == 125) or (go_up == 125 and go_down == 247 and go_right == 124) or (go_up == 129 and go_down == 247 and go_right == 124)):
        y = y - 4
    elif direction == 'right' and ((go_up == 52 and go_down == 247 and go_right == 125) or (go_up == 123 and go_down == 50 and go_right == 125) or (go_up == 123 and go_down == 53 and go_right == 124) or (go_up == 125 and go_down == 53 and go_right == 125) or (go_up == 126 and go_down == 53 and go_right == 125) or (go_up == 124 and go_down == 53 and go_right == 124) or (go_up == 124 and go_down == 53 and go_right == 125) or (go_up == 125 and go_down == 53 and go_right == 124) or (go_up == 124 and go_down == 53 and go_right == 126) or (go_up == 125 and go_down == 53 and go_right == 126) or (go_up == 126 and go_down == 53 and go_right == 126) or (go_up == 126 and go_down == 53 and go_right == 124) or (go_up == 126 and go_down == 98 and go_right == 126) or (go_up == 124 and go_down == 126 and go_right == 126)):
        x = x + 3
    elif direction == 'down' and ((go_up == 126 and go_down == 126 and go_right == 101) or (go_up == 0 and go_down == 126 and go_right == 126) or (go_up == 0 and go_down == 124 and go_right == 126) or (go_up == 0 and go_down == 126 and go_right == 127)):
        y = y + 4
    elif direction == 'left' and ((go_up == 0 and go_down == 125 and go_right == 126) or (go_up == 52 and go_down == 126 and go_right == 78) or (go_up == 52 and go_down == 124 and go_right == 78) or (go_up == 52 and go_down == 125 and go_right == 78) or (go_up == 52 and go_down == 126 and go_right == 78) or (go_up == 52 and go_down == 128 and go_right == 78)):
        x = x - 4


    # Stack the car on top of the road
    board.blit(road, (0,0))
    board.blit(car, (x, y))
    pygame.draw.circle(board, (0, 0, 255), (camx, camy), 4)
    pygame.display.update()