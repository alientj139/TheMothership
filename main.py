import pygame
import config
from game import Game
from game_state import GameState
from pygame_functions import *

#Hello there! So this is my game thus far, if you have played it yet, you would noticed that it-..
#is not completed.
#GAME FEATURES THAT ARE MISSING
# 1. Cloud to player collision.
# 2. Cloud random smooth movement.
# 3. Player collecting objects.
#So these are the missing functions, this is due to the fact that I am learning the language as i go along..
#I have yet to learn sprite collision.. Player sprite collection.. etc.. I'm only 40% finished with..
#my courses! Now that this is out of the way, enjoy! :D

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_HEIGHT, config.SCREEN_WIDTH))

pygame.display.set_caption("My Game")
#Adding frame rate for updating
clock = pygame.time.Clock()
game = Game(screen)
game.set_up()



while game.game_state == GameState.RUNNING:
    #Basically the frames per second
    clock.tick(50)
    game.update()
    pygame.display.flip()