import pygame
import os

WIDTH , HEIGHT = 900 , 650

WIN  = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption('War Zone')

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0 ,0)
YELLOW = (255,255,0)
SPACESHIP_WIDTH  , SPACESHIP_HEIGHT = 55 , 40
BORDER = pygame.Rect(WIDTH// 2-5, 0, 10,HEIGHT)

FPS = 60
BULLETS_VEL = 7
MAX_BULLETS = 3
VEL = 5

SPACE =  pygame.transform.scale(pygame.image.load(os.path.join('Assets' , 'space.png')), (WIDTH,HEIGHT))

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


def handle_bullets(yellow_bullets , red_bullets , yellow , red):
    for bullets  in yellow_bullets:
        bullets.x += BULLETS_VEL
        if red.colliderect(bullets):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullets)
        elif bullets.x > WIDTH:
            yellow_bullets.remove(bullets)



    for bullets  in red_bullets:
        bullets.x -= BULLETS_VEL
        if yellow.colliderect(bullets):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullets)
        elif bullets.x < 0:
            red_bullets.remove(bullets)

def yellow_handle_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height  < HEIGHT - 15:
        yellow.y += VEL

def red_handle_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y + VEL + red.height  < HEIGHT - 15:
        red.y += VEL

def draw_window(red,yellow , red_bullets , yellow_bullets):
    WIN.blit(SPACE , (0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(RED_SPACESHIP , (red.x , red.y))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x , yellow.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED , bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW , bullet)

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

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_LSHIFT and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width , yellow.y + yellow.height//2 - 2 ,10,5)
                    yellow_bullets.append(bullet)
                if event.key ==  pygame.K_RSHIFT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x , red.y + red.height//2 - 2 ,10,5)
                    red_bullets.append(bullet)
        
        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed , yellow)
        red_handle_movement(key_pressed, red)

        handle_bullets(yellow_bullets , red_bullets , yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets)

        

    pygame.quit()


if __name__ == '__main__':
    main()