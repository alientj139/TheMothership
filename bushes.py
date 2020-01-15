import pygame
import config

#Hello there! So this is my game thus far, if you have played it yet, you would noticed that it-..
#is not completed.
#GAME FEATURES THAT ARE MISSING
# 1. Cloud to player collision.
# 2. Cloud random smooth movement.
# 3. Player collecting objects.
#So these are the missing functions, this is due to the fact that I am learning the language as i go along..
#I have yet to learn sprite collision.. Player sprite collection.. etc.. I'm only 40% finished with..
#my courses! Now that this is out of the way, enjoy! :D 

class Bushes:
    # Loading the bush image into the map and scaling it to the config size of the map
    def __init__(self, x_position, y_position):
        print("bushes created")
        self.position = [x_position, y_position]
        self.image= pygame.image.load("imgs/Bush.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE_BUSH, config.SCALE_BUSH))
        self.rect = pygame.Rect(self.position[0] * config.SCALE_BUSH, self.position[1] * config.SCALE_BUSH, config.SCALE_BUSH, config.SCALE_BUSH)

    #printing an update message if anything changed to the cloud, if in case I would like to make it move..
    #realistically with wind in the future.
    def update(self):
        print("bushes updated")

    #Scaling the bushes image size with reference to the config file
    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]
        self.rect = pygame.Rect(self.position[0] * config.SCALE_BUSH, self.position[1] * config.SCALE_BUSH, config.SCALE_BUSH, config.SCALE_BUSH)

    def render(self, screen):
        screen.blit(self.image, self.rect)


 