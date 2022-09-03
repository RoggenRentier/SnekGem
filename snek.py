import pygame
import os
import copy

pygame.font.init()

RUN = True

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snek Gem")
FPS = 30
WINNER_TEXT = ""


#colors
WHITE = (255,255,255)
GREY  = (45 ,45 ,45 )
BLACK = (0  ,0  ,0  )
GREEN = (0  ,255,0  )
YELLOW= (255,255,0  )

#players
SIDE = 10
#player1
LEFT_DIRECTION = 1 #1 right, 2 down, 3 left, 4 up
LEFT_COLOR = YELLOW
#player2
RIGHT_DIRECTION = 3 #1 right, 2 down, 3 left, 4 up
RIGHT_COLOR = GREEN



def main():
    global RUN
    global WINNER_TEXT

    WINNER_TEXT = ""

    clock = pygame.time.Clock()

    #player 1
    left = pygame.Rect(center(100), center(50), SIDE, SIDE)
    #player 2
    right = pygame.Rect(center(800), center(450), SIDE, SIDE)

    squares_exist = [copy.copy([False]*(HEIGHT//SIDE)) for x in [False]*(WIDTH//SIDE)]
    squares_exist[to_squares_exist(left.x)][to_squares_exist(left.y)]
    squares_exist[to_squares_exist(right.x)][to_squares_exist(right.y)]

    print(squares_exist)

    draw_window_init()

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
        right = right_movement_handler(keys_pressed, right)

        if(WINNER_TEXT):
            print(WINNER_TEXT)
            RUN = False
        else:
            draw_window(left, right)





    if not RUN:
        print("exit")
        pygame.quit()





def draw_window(left, right):

    pygame.draw.rect(WIN, LEFT_COLOR, left)
    pygame.draw.rect(WIN, RIGHT_COLOR, right)

    pygame.display.update()

def draw_window_init():
    WIN.fill(BLACK)



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
    else: #continue in same direction
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


def right_movement_handler(keys_pressed, right):
    global RIGHT_DIRECTION

    if keys_pressed[pygame.K_UP] and RIGHT_DIRECTION != 2:
        right.y -= SIDE
        RIGHT_DIRECTION = 4
    elif keys_pressed[pygame.K_DOWN] and RIGHT_DIRECTION != 4:
        right.y += SIDE
        RIGHT_DIRECTION = 2
    elif keys_pressed[pygame.K_LEFT] and RIGHT_DIRECTION != 1:
        right.x -= SIDE
        RIGHT_DIRECTION = 3
    elif keys_pressed[pygame.K_RIGHT] and RIGHT_DIRECTION != 3:
        right.x += SIDE 
        RIGHT_DIRECTION = 1
    else: #continue in same direction
        match RIGHT_DIRECTION:
            case 1:
                right.x += SIDE
            case 2:
                right.y += SIDE
            case 3:
                right.x -= SIDE
            case 4:
                right.y -= SIDE
            #else
            case _:
                print("this is broken")

    return right


#takes the center coordinate and calculates upper left corner 
def center(a):
    return a - SIDE//2 

#takes a single coordinate and translates it into a position in squares_exist
def to_squares_exist(a):
    return(a//SIDE)


if __name__ == "__main__":
    while RUN:
        main()