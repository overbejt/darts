import pygame

print("so far so good!")

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

    # declaring and initializing an image to hold the koala
    koala = pygame.image.load("Killer-koala.png").convert()
    #koala.set_alpha(128)

    # game loop
    while(running):
        # draw the koala to the screen
        screen.blit(koala, (300, 300))
        # update the screen
        pygame.display.flip()
        # handling game events
        for event in pygame.event.get():
            # Only handling quit events
            if(event.type == pygame.QUIT):
                # flip "running" off
                running = False


# This will make the game run only if it is the main program
# If it is imported, then nothing will happen
if __name__ == "__main__":
    # call the main function
    main()
    print("Auf weider sehen!")
