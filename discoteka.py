import random
import pygame
pygame.init()
import pygame.mixer
pygame.mixer.init()#



pygame.mixer.music.load("music.mp3")#
pygame.mixer.music.play(-1)#

size=(0, 0)
pygame.display.set_caption("Моя игра")
screen = pygame.display.set_mode(size)

BACKGROUND=(255, 255, 255)

line_color=(255, 0, 0)#
line_width=5#
start_pos=(0, size[1]//2)#
end_pos=(size[0], size[1]//2)#

GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)
YELLOW=(255, 255, 0)
GYAN=(0, 255, 255)
MAGENTA=(255, 0, 255)
GRAY=(128, 128, 128)
ORANGE=(255, 165, 0)
PINK=(255, 192, 203)
BROWN=(165, 42, 42)
PURPLE=(128, 0, 128)
LIME=(0, 255, 0)
NAVY=(0, 0, 128)
OLIVE=(128, 128, 0)
MAROON=(128, 0, 0)
TEAL=(0, 128, 128)
SILVER=(192, 192, 192)
GOLD=(255, 215, 0)

COLORS=[GREEN, RED, BLUE, YELLOW, GYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE,
        MAROON, TEAL, SILVER, GOLD]

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    color_index=random.randint(0,7)
    if color_index==7:
        BACKGROUND = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    else:
        BACKGROUND = COLORS[color_index]
    screen.fill(BACKGROUND)

    for _ in range(23):
        x=random.randint(0,2160)
        y=random.randint(0,1080)
        radius=random.randint(10, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))
pygame.quit()