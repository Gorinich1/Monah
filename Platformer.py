# codding : ulft-8

import pygame
import random

pygame.init()
size = [1000, 667]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

man = pygame.image.load('Man.png').convert_alpha()
block = pygame.image.load('grass.png').convert_alpha()
background = pygame.transform.scale(pygame.image.load('background.png').convert_alpha(), (1000, 667))
carrot = pygame.image.load('carrot.png').convert_alpha()
arrow_left = pygame.image.load('danger.png').convert_alpha()
shadow = pygame.image.load('shadow.png').convert_alpha()
lighter = pygame.image.load('lighter.png').convert_alpha()
block_size2 =[60, 80]
block_size = [1000, 60]

font = pygame.font.Font('ChinaOne.ttf', 40)
sound = pygame.mixer.Sound("sound.wav")
sound = pygame.mixer.Sound("sound.wav")
sound = pygame.mixer.Sound("sound.wav")

#  (100, 100)
scaled_man = pygame.transform.scale(man, (72, 72))
scaled_block = pygame.transform.scale(block, block_size)
scaled_block2 = pygame.transform.scale(lighter, block_size2)
scaled_carrot = pygame.transform.scale(carrot, (50, 50))
scaled_arrow = pygame.transform.scale(arrow_left, (40, 40))
scaled_shadow = pygame.transform.scale(shadow, (72, 18))

carrots = 0
arr_acc = 10
angle = 1

upper_point = 320
block2_vel = [2, 0]
block2_acc = [0, 0.5]
hero_pos = [200, 100]
hero_vel = [5, 5]
hero_acc = [0, 0.5]
block_pos = [0, 667-60]
block_pos2 = [540, 320]
carrot_pos = [606, 667-200]
arrow_pos = [0, 0]
text_pos = [50, 667-50]

man_mask = pygame.mask.from_surface(scaled_man)
block_mask = pygame.mask.from_surface(scaled_block)
carrot_mask = pygame.mask.from_surface(scaled_carrot)
arrow_mask = pygame.mask.from_surface(scaled_arrow)
block_mask2 = pygame.mask.from_surface(scaled_block2)

text = font.render(str(carrots), True, [0,0,0])

running = True
print(0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero_vel[1] = -10
                hero_acc[1] = 0.5
    sound.play()
    if block_pos2[1] < upper_point:
            block_pos2[1] = upper_point
    if block_pos2[1] > upper_point:
            block2_vel[1] -= 1
    if pygame.key.get_pressed()[pygame.K_a]:
        hero_vel[0] = -5
    if pygame.key.get_pressed()[pygame.K_d]:
        hero_vel[0] = 5

    block_pos2[0] += block2_vel[0]
    block_pos2[1] += block2_vel[1]

    block2_vel[0] += block2_acc[0]
    block2_vel[1] += block2_acc[1]

    arrow_pos[0] += arr_acc

    hero_pos[0] += hero_vel[0]
    hero_pos[1] += hero_vel[1]

    hero_vel[1] += hero_acc[1]
    hero_vel[0] += hero_acc[0]

    offset = (int(hero_pos[0] - block_pos[0]), int(hero_pos[1] - block_pos[1]))                 #CPABHUBAEM MACKU block U hero

    if block_mask.overlap_area(man_mask, offset) > 0:
        if hero_pos[1] < block_pos[1]:
            hero_vel = [0,0]
            hero_pos[1] = block_pos[1] - 72
        if  block_pos[1] + block_size[1] - 72 < hero_pos[1] < block_pos[1] + block_size[1]:
            hero_pos[1] = block_pos[1] + 72
        if hero_pos[0] + 72 < block_pos[0]:
            hero_pos[0] = block_pos[0] + 72
        if hero_pos[0] > block_pos[0] + block_size[0]:
            hero_pos[0] = block_pos[0] + 72

    offset = (int(hero_pos[0] - block_pos2[0]), int(hero_pos[1] - block_pos2[1]))                 #CPABHUBAEM MACKU block2 U hero

    if block_mask2.overlap_area(man_mask, offset) > 0:
        if hero_pos[1] < block_pos2[1]:
            hero_vel[0] = block2_vel[0]
            hero_vel[1] = 0
            hero_pos[1] = block_pos2[1] - 72
            block2_vel[1] = 4
            hero_pos[0] = block_pos2[0]
        if  block_pos2[1] + block_size2[1] - 72 < hero_pos[1] < block_pos2[1] + block_size2[1]:
            hero_pos[1] = block_pos2[1] + 72
        if hero_pos[0] + 72 < block_pos2[0]:
            hero_pos[0] = block_pos2[0] + 72
        if hero_pos[0] > block_pos2[0] + block_size[0]:
            hero_pos[0] = block_pos2[0] + 72

    offset = (int(hero_pos[0] - arrow_pos[0]), int(hero_pos[1] - arrow_pos[1]))                 #CPABHUBAEM MACKU arrow U hero

    if arrow_mask.overlap_area(man_mask, offset) > 0:
        if carrots > 3:
            carrots -= 3
            hero_pos = [500,667 - 150]
            text = font.render(str(carrots), True, [0,0,0])
        else:
            running = False

    offset = (int(hero_pos[0] - carrot_pos[0]), int(hero_pos[1] - carrot_pos[1]))                 #CPABHUBAEM MACKU carrot U hero

    if carrot_mask.overlap_area(man_mask, offset) > 0:
        carrots += 1
        carrot_pos[0] = random.randint(1, 1000 - 50)
        carrot_pos[1] = random.randint(0, 667 - 70)
        text = font.render(str(carrots), True, [0,0,0])

    angle += 10

    if hero_pos[1] > 640:
        running = False

    if hero_pos[0] > (1000 - 72):
        hero_pos[0] = (1000 - 72)
    if hero_pos[0] < 0:
        hero_pos[0] = 0

    if block_pos2[0] > (1000 - block_size2[0]):
        block2_vel[0] = -2
    if block_pos2[0] < 0:
        block2_vel[0] = 2

    if arrow_pos[0] > 1000:
        arr_vel = random.randint(0, 1)
        if arr_vel == 0:
            arr_acc = 10
            arrow_pos[0] = 0
            arrow_pos[1] = random.randint(0, 667-162)
        if arr_vel == 1:
            arr_acc = -10
            arrow_pos[0] = 1000
            arrow_pos[1] = random.randint(0, 667-162)
    if arrow_pos[0] < 0:
        arr_vel = random.randint(0, 1)
        if arr_vel == 0:
            arr_acc = 10
            arrow_pos[0] = 0
            arrow_pos[1] = random.randint(0, 667-162)
        if arr_vel == 1:
            arr_acc = -10
            arrow_pos[0] = 1000
            arrow_pos[1] = random.randint(0, 667-162)
    rotate_arrow = pygame.transform.rotate(pygame.transform.scale(arrow_left, (40, 40)), angle)
    # ??????
    screen.fill((200, 100, 0))
    screen.blit(background, (0, 0))
    screen.blit(scaled_block, block_pos)
    screen.blit(scaled_block2, block_pos2)
    screen.blit(scaled_man, hero_pos)
    screen.blit(scaled_carrot, carrot_pos)
    screen.blit(rotate_arrow, arrow_pos)
    screen.blit(scaled_shadow, (hero_pos[0], block_pos[1]))
    screen.blit(text, text_pos)
    screen.blit(scaled_carrot, (0, 667 - 50))
    sound.play()
    broke_arr.play()
    collect_carrot.play()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()