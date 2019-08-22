import pygame

print("so far so good!")


def updateKoala(prevX, direction):
    result = prevX + direction
    if(result < 0):
        return 0
    elif(result > 1075):
        return 1075
    else:
        return result


# defining a main function
def main():

    # frame rate
    fps = 35
    # clocks
    clock = pygame.time.Clock()

    # initializing a pygame module
    pygame.init()
    # setting the caption
    pygame.display.set_caption("My version of darts game")

    # creating a surface on the screen that has a size of 240 x 180
    screen = pygame.display.set_mode((1200, 800))

    # declaring and initializing to controll when the game is running
    running = True

    # initializing the main character
    koala = pygame.image.load("Killer-koala.png").convert_alpha()
    # initializing the coconut
    coconut = pygame.image.load("coconut.png").convert_alpha()
    kx = 600    # koala x
    ky = 650    # koala y
    cx = 600    # coconut x
    cy = 0      # coconut y

    # color?
    white = [255, 255, 255]

    # game loop
    while(running):
        # handling game events
        for event in pygame.event.get():
            # Only handling quit events
            if(event.type == pygame.QUIT):
                # flip "running" off
                running = False
            # Check if a button was clicked
            if(event.type == pygame.KEYDOWN):
                # Check if left arrow hit
                if(event.key == pygame.K_LEFT):
                    # Move the koala left
                    kx = updateKoala(kx, -30)
                # Check if the right arrow hit
                if(event.key == pygame.K_RIGHT):
                    kx = updateKoala(kx, 30)

        screen.fill(white)
        # draw the koala to the screen
        screen.blit(koala, (kx, ky))
        # draw the coconut to the screen
        screen.blit(coconut, (cx, cy))
        # update the screen
        pygame.display.update()
        # increment the clock
        clock.tick(fps)


# This will make the game run only if it is the main program
# If it is imported, then nothing will happen
if __name__ == "__main__":
    # call the main function
    main()
    print("Auf weider sehen!")
