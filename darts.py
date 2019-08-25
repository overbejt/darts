import pygame
import random

print("so far so good!")

# Defining global variables
display_width = 1200
display_height = 647

#***********************************************************#
# This is the method that will update the coordinates of    #
# Koala.  It will also do bounds checking to keep the koala #
# on the screen.                                            #
#***********************************************************#


def updateKoala(prevX, direction):
    result = prevX + direction
    if(result < 0):
        return 0
    elif(result > 1075):
        return 1075
    else:
        return result
#************ end of 'updateKoala' method *******************


#***********************************************************#
# This is the method that will update to coordinates of a   #
# coconut.                                                  #
#***********************************************************#
def updateCoconut(prevX, prevY):
    # initialize an array
    result = [prevX, prevY]

    # check if off the screen
    if(prevY < display_height):
        result[1] += 35
    else:
        # need random math for x movement
        # result[0] = 0
        # result[0] = 1118
        result[0] = random.randint(0, 1118)
        # update y coordinate
        result[1] = 0

    return result

#********** end of 'updateCoconut' method *******************

#***********************************************************#
# This is the method that will check to see if there is a   #
# colision between the coconut and the koala.  When there   #
# is a colision, this method will return true.  When there  #
# is not a colision, this method will return false.  It     #
# will take in 3 integers.  The X and Y coordinates of the  #
# coconut.  And the X coordinate of the koala.              #
#***********************************************************#
def collisionCheck(cx, cy, kx):
    if(cy < 125):
        return False
    elif(cx >= kx & & cx <= (kx + 125)):
        return True
    else:
        return False
#******* End of the 'collisionCheck' method *****************


#***********************************************************#
# This is the main method.  It will contain the game loop.  #
# It will also check and handle all of the events from      #
# pygame.                                                   #
#***********************************************************#
def main():

    # initializing a pygame module
    pygame.init()
    # setting the caption
    pygame.display.set_caption("My version of darts game")

    # frame rate
    fps = 35
    # clocks
    clock = pygame.time.Clock()
    # theme song
    pygame.mixer.music.load("SwayThisWay.wav")

    # creating a surface on the screen that has a size of 240 x 180
    screen = pygame.display.set_mode((display_width, display_height))

    # declaring and initializing to controll when the game is running
    running = True

    # initializing the main character
    koala = pygame.image.load("Killer-koala.png").convert_alpha()
    # initializing the coconut
    coconut = pygame.image.load("coconut.png").convert_alpha()
    # initializing the background
    background = pygame.image.load("jungle-palm-trees.png").convert()

    # cooridinates
    kx = 600    # koala x
    ky = display_height - 125    # koala y
    cx = 600    # coconut x
    cy = 0      # coconut y

    # color?
    white = [255, 255, 255]

    # start the theme song and loop it
    pygame.mixer.music.play(-1)

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
                    kx = updateKoala(kx, -35)
                # Check if the right arrow hit
                if(event.key == pygame.K_RIGHT):
                    kx = updateKoala(kx, 35)

        # screen.fill(white)
        screen.blit(background, (0, 0))
        # draw the koala to the screen
        screen.blit(koala, (kx, ky))

        # update coordinates of coconut
        coconutCoords = updateCoconut(cx, cy)
        cx = coconutCoords[0]
        cy = coconutCoords[1]
        # draw the coconut to the screen
        screen.blit(coconut, (cx, cy))

        # update the screen
        pygame.display.update()
        # increment the clock
        clock.tick(fps)

#**************** end of 'main' ****************************


# This will make the game run only if it is the main program
# If it is imported, then nothing will happen
if __name__ == "__main__":
    # call the main function
    main()
    print("Auf weider sehen!")
