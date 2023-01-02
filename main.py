import pygame
import os

WIDTH , HEIGHT = 900 , 650

WIN  = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption('War Zone')

WHITE = (255,255,255)
SPACESHIP_WIDTH  , SPACESHIP_HEIGHT = 55 , 40

FPS = 60

VEL = 5


def yellow_handle_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a]:
        yellow.x -= VEL
    if key_pressed[pygame.K_d]:
        yellow.x += VEL
    if key_pressed[pygame.K_w]:
        yellow.y -= VEL
    if key_pressed[pygame.K_s]:
        yellow.y += VEL

def red_handle_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT]:
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT]:
        red.x += VEL
    if key_pressed[pygame.K_UP]:
        red.y -= VEL
    if key_pressed[pygame.K_DOWN]:
        red.y += VEL

def draw_window(red,yellow):
    WIN.fill(WHITE)
    WIN.blit(RED_SPACESHIP , (red.x , red.y))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x , yellow.y))
    pygame.display.update()

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE , (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)) , 90
)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE , (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)) , 270
)

def main():

    yellow  = pygame.Rect(100,300 , SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed , yellow)
        red_handle_movement(key_pressed, red)

        draw_window(red, yellow)

        

    pygame.quit()


if __name__ == '__main__':
    main()