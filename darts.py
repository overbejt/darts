import pygame
import random
import time 
import sys

print("so far so good!")

# Defining global variables
display_width = 1200
display_height = 647
global is_paused 
is_paused = False

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Reserved Btn Keywords
PLAY_AGAIN_BTN = 'playAgain'
QUIT_BTN = 'quit'

#***********************************************************#
# This method is responsible for puase/unpuase of the game. #
# It will also pause/unpause the audio for the game.        #
#***********************************************************#
def togglePause(music):
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
    pause_msg = font.render('Paused', True, BLACK)
    x = (display_width / 2) - 200
    y = (display_height / 2) - 255
    screen.blit(pause_msg, (x, y))
#************ end of 'displayPaused' method ******************

#***********************************************************#
# This method draws the users score.                        #
#***********************************************************#
def drawScore(screen, font, score):
    score_msg = font.render("Score: {}".format(score), True, BLACK)
    x = 40
    y = 25
    screen.blit(score_msg, (x, y))
#************ end of 'drawScore' method *********************

#***********************************************************#
# This method draws how many lives the user has left.       #
#***********************************************************#
def drawLives(screen, font, livesCount):
    lives_str = ''
    for i in range(livesCount):
        lives_str += 'X'

    lives_msg = font.render('Lives:{}'.format(lives_str), True, BLACK)
    x = 40
    y = 66
    screen.blit(lives_msg, (x, y))
#************ end of 'drawLives' method *********************

#***********************************************************#
# This method will draw the game over message on the screen #
#***********************************************************#
def drawGameOver(pygame, screen, font):
    game_over_msg = font.render('Game Over', True, BLACK)
    x = (display_width / 2) - 300
    y = (display_height / 2) - 255
    screen.blit(game_over_msg, (x, y))
#************ end of 'drawGameOver' method ******************

#***********************************************************#
# This method draws the delta T between frames.             #
#***********************************************************#
def drawFps(screen, font, deltaT):
    fps_msg = font.render('{}'.format(deltaT), True, BLACK)
    x = 40
    y = 107
    screen.blit(fps_msg, (x, y))
#************ end of 'drawFps' method **********************

#***********************************************************#
# This method draws the play again button.  It returns the  #
# rect so that I can check if the user clicks on it         #
#***********************************************************#
def drawPlayAgainBtn(pygame, screen, font):
    play_again_msg = font.render('Play Again', True, WHITE)
    w = 125
    h = 50
    x = (display_width / 2) - (w / 2)
    y = (display_height / 2) + 20
    padding_left = 8
    btn = pygame.draw.rect(screen, BLACK, (x, y, w, h))
    screen.blit(play_again_msg, (x + padding_left, y))
    return btn
#************ end of 'drawQuitBtn' method *******************

#***********************************************************#
# This method draws the quit button.  It returns the rect   #
# so that I can check if the user clicks on it.             #
#***********************************************************#
def drawQuitBtn(pygame, screen, font):
    play_again_msg = font.render('Quit', True, WHITE)
    w = 125
    h = 50
    x = (display_width / 2) - (w / 2)
    y = (display_height / 2) + (20 + h + 10)
    padding_left = 40
    btn = pygame.draw.rect(screen, BLACK, (x, y, w, h))
    screen.blit(play_again_msg, (x + padding_left, y))
    return btn
#************ end of 'drawQuitBtn' method *******************

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
    # initialize a list
    result = [prevX, prevY]

    # check if off the screen
    if(prevY < display_height):
        # If you update this, update the collision check
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
    koala_top = display_height - 125
    if(cy < koala_top):
        return False
    elif(cx >= kx):
        if(cx <= (kx + 125)):
            # only return true on the first collision
            if (cy >= koala_top and cy < koala_top + 35):
                # TODO update if the speed of the coconut is 
                # ever changed
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#******* End of the 'collisionCheck' method *****************

#***********************************************************#
# mx is the mouse x, my is the mouse y.  The btn is a       #
# pygame Rect object.                                       #
#***********************************************************#
def btnClicked(mx, my, btn):
    btn_clicked = False

    # for readability
    btn_left = btn.midleft[0]
    btn_right = btn.midright[0]
    btn_top = btn.midtop[1]
    btn_bottom = btn.midbottom[1]

    if(mx >= btn_left and mx <= btn_right):
        if(my >= btn_top and my <= btn_bottom):
            btn_clicked = True
    return btn_clicked
#******* End of the 'btnClicked' method *********************

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
    # for capturing the time delta
    delta_t = 0
    # clocks
    clock = pygame.time.Clock()

    # creating a surface on the screen that has a size of 240 x 180
    screen = pygame.display.set_mode((display_width, display_height))

    # declaring and initializing to controll when the game is running
    running = True
    global is_paused
    is_paused = False

    # keep track of the score
    score = 0
    # keep track of the lives
    life_count = 10  # TODO update some day?
    # for keeping track of if the score needs updated
    is_koala_hit = False

    # initializing the main character
    koala = pygame.image.load("Killer-koala.png").convert_alpha() # 125 x 125
    # initializing the coconut
    coconut = pygame.image.load("coconut.png").convert_alpha() # 82 x 82
    # initializing the background
    background = pygame.image.load("jungle-palm-trees.png").convert()

    # initializing fonts
    pause_font = pygame.font.Font("AmaticSC-Regular.ttf", 225)
    game_over_font = pygame.font.Font("AmaticSC-Regular.ttf", 225)
    score_font = pygame.font.Font("AmaticSC-Bold.ttf", 36)
    lives_font = pygame.font.Font("AmaticSC-Bold.ttf", 36)
    fps_font = pygame.font.Font("AmaticSC-Bold.ttf", 36)
    play_again_font = pygame.font.Font("AmaticSC-Bold.ttf", 36)
    quit_font = pygame.font.Font("AmaticSC-Bold.ttf", 36)

    # keeping all the buttons in one place
    buttons = { }


    # cooridinates
    kx = 600    # koala x
    ky = display_height - 125    # koala y
    cx = 400    # coconut x
    cy = 0      # coconut y

    # start the theme song and loop it
    pygame.mixer.music.play(-1)

    # game loop
    while(running):
        # check for collisions
        if life_count > 0:
            if(collisionCheck(cx, cy, kx)):
                sound.play()
                life_count = life_count - 1
                is_koala_hit = True

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
                if(event.key == pygame.K_SPACE and life_count > 0):
                    togglePause(pygame.mixer.music)
                # Check if they want to quit the game
                if(event.key == pygame.K_ESCAPE):                    
                    sys.exit()
            # Check if the player left clicked a button 
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mx, my = pygame.mouse.get_pos()
                if (life_count == 0):
                    # Check if they want to play again
                    if buttons[PLAY_AGAIN_BTN] is not None:
                        if(btnClicked(mx, my, buttons[PLAY_AGAIN_BTN])):
                            del buttons[PLAY_AGAIN_BTN]
                            main() # Restart
                    # Check if they want to quit
                    if buttons[QUIT_BTN] is not None:
                        if(btnClicked(mx, my, buttons[QUIT_BTN])):                        
                            sys.exit()


        if is_paused is False and life_count > 0:
            screen.blit(background, (0, 0))
            # draw the koala to the screen
            screen.blit(koala, (kx, ky))

            # update coordinates of coconut
            coconutCoords = updateCoconut(cx, cy)
            cx = coconutCoords[0]
            cy = coconutCoords[1]
            # draw the coconut to the screen
            screen.blit(coconut, (cx, cy))

            # check if the score should increment
            if (cy == 0):
                if is_koala_hit is False:
                    score = score + 1
                # reset the koala hit flag
                is_koala_hit = False
        elif is_paused is False and life_count == 0:
            # check if the game is over
            drawGameOver(pygame, screen, game_over_font)
            buttons[PLAY_AGAIN_BTN] = drawPlayAgainBtn(pygame, screen, play_again_font)
            buttons[QUIT_BTN] = drawQuitBtn(pygame, screen, quit_font)
            pygame.mixer.music.pause()
            # Do not create a tightly wound loop 
            # and bind the cpu
            time.sleep(0.1)
        elif is_paused is True:
            # draw the paused message
            displayPaused(screen, pause_font)
            # Do not create a tightly wound loop 
            # and bind the cpu
            time.sleep(0.1)

        # draw the player's score
        drawScore(screen, score_font, score)
        # draw the lives
        drawLives(screen, lives_font, life_count)
        # drawFps(screen, fps_font, delta_t) # More like draw delta_t    

        # update the screen
        pygame.display.update()
        # increment the clock
        delta_t = clock.tick(fps)

#**************** end of 'main' ****************************


# This will make the game run only if it is the main program
# If it is imported, then nothing will happen
if __name__ == "__main__":
    # call the main function
    main()
    print("Auf weider sehen!")
