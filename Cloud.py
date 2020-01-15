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

class Cloud:
    # Loading the clouds image into the map and scaling it to the config size of the map
    def __init__(self, x_position, y_position):
        print("clouds created")
        self.position = [x_position, y_position]
        self.image= pygame.image.load("imgs/clouds.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE_CLOUDS, config.SCALE_CLOUDS))
        self.rect = pygame.Rect(self.position[0] * config.SCALE_CLOUDS, self.position[1] * config.SCALE_CLOUDS, config.SCALE_CLOUDS, config.SCALE_CLOUDS)

    #printing an update message if anything changed to the cloud, eg: movement
    def update(self):
        print("cloud updated")

    #Scaling the cloud image size with reference to the config file
    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]
        self.rect = pygame.Rect(self.position[0] * config.SCALE_CLOUDS, self.position[1] * config.SCALE_CLOUDS, config.SCALE_CLOUDS, config.SCALE_CLOUDS)

    def render(self, screen):
        screen.blit(self.image, self.rect)


 