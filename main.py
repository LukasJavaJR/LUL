import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((350, 350))

# SETUP CTVERCU:
ctverec = pygame.Surface([30, 30])
ctverec_2 = pygame.Surface([30, 30])
ctverec_3 = pygame.Surface([30, 30])

ctverec_move = ctverec.get_rect(center = [350//2, 350//2])
ctverec_move_2 = ctverec.get_rect(center = [350//2, 350//2])
ctverec_move_3 = ctverec.get_rect(center = [350//2, 350//2])

# SETUP VELIKOSTI KROKU A FPS
step_range = range(3, 7)
fps = 30

def move_up():
    ctverec_move.bottom -= step_distance
def move_down():
    ctverec_move.bottom += step_distance
def move_left():
    ctverec_move.right -= step_distance
def move_right():
    ctverec_move.right += step_distance

def move_up_2():
    ctverec_move_2.bottom -= step_distance_2
def move_down_2():
    ctverec_move_2.bottom += step_distance_2
def move_left_2():
    ctverec_move_2.right -= step_distance_2
def move_right_2():
    ctverec_move_2.right += step_distance_2

def move_up_3():
    ctverec_move_3.bottom -= step_distance_3
def move_down_3():
    ctverec_move_3.bottom += step_distance_3
def move_left_3():
    ctverec_move_3.right -= step_distance_3
def move_right_3():
    ctverec_move_3.right += step_distance_3

def next_move():
    while True:
        step = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        if step == 'UP':
            return move_up()
        if step == 'DOWN':
            return move_down()
        if step == 'LEFT':
            return move_left()
        if step == 'RIGHT':
            return move_right()
    
        
def next_move_2():
    while True:
        step = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        if step == 'UP':
            return move_up_2()
        if step == 'DOWN':
            return move_down_2()
        if step == 'LEFT':
            return move_left_2()
        if step == 'RIGHT':
            return move_right_2()

def next_move_3():
    while True:
        step = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        if step == 'UP':
            return move_up_3()
        if step == 'DOWN':
            return move_down_3()
        if step == 'LEFT':
            return move_left_3()
        if step == 'RIGHT':
            return move_right_3()

# KOLIZE S OKRAJEM OKNA=GAME OVER // FUNGUJE:
# def is_out(ctverec_move, ctverec_move_2, ctverec_move_3):
#     if ctverec_move[0] < 0 or ctverec_move[1] < 0 or ctverec_move[0] > 335 or ctverec_move[1] > 335:
#         return True
#     if ctverec_move_2[0] < 0 or ctverec_move_2[1] < 0 or ctverec_move_2[0] > 335 or ctverec_move_2[1] > 335:
#         return True
#     if ctverec_move_3[0] < 0 or ctverec_move_3[1] < 0 or ctverec_move_3[0] > 335 or ctverec_move_3[1] > 335:
#         return True    
#     return False

# PRVNI POKUS O ZNEMOZNENI CTVERCE VYJIT MIMO OKNO // NEFUNGUJE FeelsBadMan:
# def je_v_poli(ctverec_move, ctverec_move_2, ctverec_move_3):
#     if ctverec_move[0] > 40 + ctverec_move[1] > 40 + ctverec_move[0] < 295 + ctverec_move[1] < 295:
#         return True
#     if ctverec_move_2[0] > 40 + ctverec_move_2[1] > 40 + ctverec_move_2[0] < 295 + ctverec_move_2[1] < 295:
#         return True
#     if ctverec_move_3[0] > 40 + ctverec_move_3[1] > 40 + ctverec_move_3[0] < 295 + ctverec_move_3[1] < 295:
#         return True    
#     return False


# "VRACEČ" -DRUHY POKUS O ZNEMOZNENI CTVERCE VYJIT MIMO OKNO // FUNGUJE! FeelsGoodMan:
def vracec(ctverec_move):
    if ctverec_move[0] <= 0:
        ctverec_move[0] = 15
    elif ctverec_move[1] <= 0:
        ctverec_move[1] = 15
    elif ctverec_move[0] >= 300:
        ctverec_move[0] = 285
    elif ctverec_move[1] >= 300:
        ctverec_move[1] = 285
    return ctverec_move

def vracec_2(ctverec_move_2):
    if ctverec_move_2[0] <= 0:
        ctverec_move_2[0] = 15
    elif ctverec_move_2[1] <= 0:
        ctverec_move_2[1] = 15
    elif ctverec_move_2[0] >= 300:
        ctverec_move_2[0] = 285
    elif ctverec_move_2[1] >= 300:
        ctverec_move_2[1] = 285
    return ctverec_move_2

def vracec_3(ctverec_move_3):
    if ctverec_move_3[0] <= 0:
        ctverec_move_3[0] = 15
    elif ctverec_move_3[1] <= 0:
        ctverec_move_3[1] = 15
    elif ctverec_move_3[0] >= 300:
        ctverec_move_3[0] = 285
    elif ctverec_move_3[1] >= 300:
        ctverec_move_3[1] = 285
    return ctverec_move_3

def end_game():
    print("GAME OVER")
    screen.fill((0, 0, 0))
    pygame.quit()
    sys.exit()   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    step_distance = random.choice(step_range)
    step_distance_2 = random.choice(step_range)
    step_distance_3 = random.choice(step_range)

    screen.fill((190, 190, 190))

    screen.blit(ctverec, ctverec_move)
    ctverec.fill((50, 50, 250))
    # if je_v_poli == True:
    next_move()
    vracec(ctverec_move)

    screen.blit(ctverec_2, ctverec_move_2)
    ctverec_2.fill((250, 50, 50))
    # if je_v_poli == True:
    next_move_2()
    vracec_2(ctverec_move_2)

    screen.blit(ctverec_3, ctverec_move_3)
    ctverec_3.fill((50, 250, 50))
    # if je_v_poli == True:
    next_move_3()
    vracec_3(ctverec_move_3)

    # if is_out(ctverec_move, ctverec_move_2, ctverec_move_3):
    #         end_game()          

    pygame.display.flip()
    clock.tick(fps)