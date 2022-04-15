import pygame
import random
import time 

print("so far so good!")

# Defining global variables
display_width = 1200
display_height = 647
global is_paused 
is_paused = False

#***********************************************************#
# This method is responsible for puase/unpuase of the game. #
# It will also pause/unpause the audio for the game.        #
#***********************************************************#
def togglePause(music):
    # TODO put a pause message on the screen
    global is_paused
    is_paused = not is_paused

    # Toggle the music too
    if is_paused is True:
        music.pause()
    else:
        music.unpause()
#************ end of 'togglePause' method *******************

#***********************************************************#
# This method will draw the paused message on the screen.   #
#***********************************************************#
def displayPaused(screen, font):
    pause_color = (0, 0, 0)
    pause_msg = font.render('Paused', True, pause_color)
    x = (display_width / 2) - 200
    y = (display_height / 2) - 255
    screen.blit(pause_msg, (x, y))
#************ end of 'displayPaused' method ******************    

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
    if(cy < (display_height - 125)):
        return False
    elif(cx >= kx):
        if(cx <= (kx + 125)):
            return True
        else:
            return False
    else:
        return False
#******* End of the 'collisionCheck' method *****************

#***********************************************************#
# This is the method that will handle when a colision has   #
# occured.                                                  #
#***********************************************************#


def handleColision():
    sound.play()
#******* End of the 'handleColision' method *****************


#***********************************************************#
# This is the main method.  It will contain the game loop.  #
# It will also check and handle all of the events from      #
# pygame.                                                   #
#***********************************************************#
def main():

    # initializing a pygame module
    pygame.init()

    pygame.mixer.music.load("SwayThisWay.wav")
    sound = pygame.mixer.Sound("collision.wav")
    # setting the caption
    pygame.display.set_caption("Krazy Koala")

    # frame rate
    fps = 35
    # clocks
    clock = pygame.time.Clock()

    # creating a surface on the screen that has a size of 240 x 180
    screen = pygame.display.set_mode((display_width, display_height))

    # declaring and initializing to controll when the game is running
    running = True
    global is_paused
    is_paused = False

    # initializing the main character
    koala = pygame.image.load("Killer-koala.png").convert_alpha()
    # initializing the coconut
    coconut = pygame.image.load("coconut.png").convert_alpha()
    # initializing the background
    background = pygame.image.load("jungle-palm-trees.png").convert()

    # initializing the paused font
    pause_font = pygame.font.Font("AmaticSC-Regular.ttf", 225)

    # cooridinates
    kx = 600    # koala x
    ky = display_height - 125    # koala y
    cx = 400    # coconut x
    cy = 0      # coconut y

    # color?
    white = [255, 255, 255]

    # start the theme song and loop it
    pygame.mixer.music.play(-1)

    # game loop
    while(running):

        # check for collisions
        if(collisionCheck(cx, cy, kx)):
            sound.play()
            # handleColision()

        # handling game events
        for event in pygame.event.get():
            # Only handling quit events
            if(event.type == pygame.QUIT):
                # toggle "running" off
                running = False
            # Check if a button was clicked
            if(event.type == pygame.KEYDOWN):
                # Only update the Koala if the game is not paused
                if is_paused is False:
                    # Check if left arrow hit
                    if(event.key == pygame.K_LEFT):
                        # Move the koala left
                        kx = updateKoala(kx, -35)
                    # Check if the right arrow hit
                    if(event.key == pygame.K_RIGHT):
                        kx = updateKoala(kx, 35)
                # Check if they want to pause the game
                if(event.key == pygame.K_SPACE):
                    togglePause(pygame.mixer.music)
                # Check if they want to quit the game
                if(event.key == pygame.K_ESCAPE):
                    running = False

        if is_paused is False:
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
        else:
            # draw the paused message
            displayPaused(screen, pause_font)
            # Do not create a tightly wound loop 
            # and bind the cpu
            time.sleep(0.1)

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
