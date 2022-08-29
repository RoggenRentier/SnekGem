import pygame
import os

pygame.font.init()

RUN = True

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snek Gem")
FPS = 30


#colors
WHITE = (255,255,255)
GREY  = (45 ,45 ,45 )

#players
SIDE = 10
LEFT_DIRECTION = 1 #1 right, 2 down, 3 left, 4 up



def main():
    global RUN

    clock = pygame.time.Clock()

    #player 1
    left = pygame.Rect(centerX(5), centerY(5), SIDE, SIDE)

    while RUN:
        clock.tick(FPS)
        events = pygame.event.get()
        pygame.event.clear()
        for event in events:
            if event.type == pygame.QUIT:
                RUN = False
                break

        keys_pressed = pygame.key.get_pressed()   
        left = left_movement_handler(keys_pressed, left)


        draw_window(left)






    if not RUN:
        print("exit")
        pygame.quit()





def draw_window(left):
    WIN.fill(GREY)
    #test = pygame.Rect(700,250,10,10)
    #pygame.draw.rect(WIN, WHITE, test)
    pygame.draw.rect(WIN, WHITE, left)
    pygame.display.update()


def left_movement_handler(keys_pressed, left):
    global LEFT_DIRECTION

    if keys_pressed[pygame.K_w] and LEFT_DIRECTION != 2:
        left.y -= SIDE
        LEFT_DIRECTION = 4
    elif keys_pressed[pygame.K_s] and LEFT_DIRECTION != 4:
        left.y += SIDE
        LEFT_DIRECTION = 2
    elif keys_pressed[pygame.K_a] and LEFT_DIRECTION != 1:
        left.x -= SIDE
        LEFT_DIRECTION = 3
    elif keys_pressed[pygame.K_d] and LEFT_DIRECTION != 3:
        left.x += SIDE 
        LEFT_DIRECTION = 1
    else:
        match LEFT_DIRECTION:
            case 1:
                left.x += SIDE
            case 2:
                left.y += SIDE
            case 3:
                left.x -= SIDE
            case 4:
                left.y -= SIDE
            #else
            case _:
                print("this is broken")

    return left


#takes the center x coordinate and calculates upper left corner x 
def centerX(x):
    return x - SIDE//2 
#takes the center y coordinate and calculates upper left corner y 
def centerY(y):
    return y - SIDE//2


if __name__ == "__main__":
    while RUN:
        main()