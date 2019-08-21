import pygame

print("so far so good!")


def updateKoala(prevX):
    return prevX + 10


# defining a main function
def main():

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
    kx = 600
    ky = 650

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
                if(event.key & pygame.K_LEFT):
                    print("The left arrow key was pressed!")

        screen.fill(white)
        # draw the koala to the screen
        screen.blit(koala, (kx, ky))
        # update the screen
        pygame.display.update()


# This will make the game run only if it is the main program
# If it is imported, then nothing will happen
if __name__ == "__main__":
    # call the main function
    main()
    print("Auf weider sehen!")
