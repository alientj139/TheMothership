import pygame
import config
import os, sys
import random
from tkinter import *
from tkinter import messagebox
from player import Player
from game_state import GameState
from pygame_functions import *
from Cloud import *
from bushes import *

#Hello there! So this is my game thus far, if you have played it yet, you would noticed that it-..
#is not completed.
#GAME FEATURES THAT ARE MISSING
# 1. Cloud to player collision.
# 2. Cloud random smooth movement.
# 3. Player collecting objects.
#So these are the missing functions, this is due to the fact that I am learning the language as i go along..
#I have yet to learn sprite collision.. Player sprite collection.. etc.. I'm only 40% finished with..
#my courses! Now that this is out of the way, enjoy!

# Displaying a welcome message everytime the game loads
class Messages:
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showwarning("Welcome to my game!", "In this game, you'll hopefully get an understanding of me and my acheivements in life")

    window.deiconify()
    window.destroy()
    window.quit()

#Adding sound to the game
#BackgroundSound = pygame.mixer.Sound('')
#Movement sound
MoveSound = pygame.mixer.Sound('music/Walk.wav')
#Wall collision sound
CollisionSound = pygame.mixer.Sound('music/bruh.wav')
#Pool collision sound
PoolSound = pygame.mixer.Sound('music/Swamp.wav')
#Quit song
EndingSound = pygame.mixer.Sound('music/credits.wav')

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []

    def set_up(self):
        # Displaying player on map
        player = Player(28, 2)
        self.player = player
        self.objects.append(player)

        # Displaying clouds on map
        cloud = Cloud(5, 1)
        self.cloud = cloud
        self.objects.append(cloud)

        # Displaying bushes on map
        bush = Bushes(10, 11)
        self.bush = bush
        self.objects.append(bush)

        bush2 = Bushes(5, 10)
        self.bush2 = bush
        self.objects.append(bush2)

        bush3 = Bushes(2, 12)
        self.bush3 = bush
        self.objects.append(bush3)

        bush3 = Bushes(15, 12)
        self.bush3 = bush
        self.objects.append(bush3)

        bush3 = Bushes(16, 10)
        self.bush3 = bush
        self.objects.append(bush3)

        print("do set up")
        self.game_state = GameState.RUNNING

        self.load_map("01")

    def update(self):
        #clearing out the screen after movement
        self.screen.fill(config.BLACK)
        
        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen)
    
    def handle_events(self):
        # Allowing the window to be quitted
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Displaying message after quiting    
                EndingSound.play()
                window = Tk()
                window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
                window.withdraw()
                messagebox.showwarning("See you soon!", "Bye for now! Check for updates on github!")
                window.deiconify()
                window.destroy()
                window.quit()
                self.game_state = GameState.ENDED
            # Handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Displaying message after quiting
                    EndingSound.play()
                    window = Tk()
                    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
                    window.withdraw()
                    messagebox.showwarning("See you soon!", "Bye for now! Check for updates on github!")
                    window.deiconify()
                    window.destroy()
                    window.quit()
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w: # up
                    MoveSound.play()
                    self.move_unit(self.player, [0, -1])

                elif event.key == pygame.K_s: # down
                    MoveSound.play()
                    self.move_unit(self.player, [0, 1])

                elif event.key == pygame.K_a: # left
                    MoveSound.play()
                    self.move_unit(self.player, [-1, 0])
                    
                elif event.key == pygame.K_d: # right
                    MoveSound.play()
                    self.move_unit(self.player, [1, 0])
                
    # Loading the map with the textfile outline
    def load_map(self, file_name):
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles= []
               
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)

            print(self.map)

    def render_map(self, screen):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_images[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

    # Preventing character from going off the map and through walls
    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return
        # Avoiding the player from the walls
        if self.map[new_position[1]][new_position[0]] == "H":
            CollisionSound.play()
            return
        # Avoiding the player from the pool
        if self.map[new_position[1]][new_position[0]] == "U":
            PoolSound.play()
            return
        
        if self.map[new_position[1]][new_position[0]] == "J":
            PoolSound.play()
            return
        
        if self.map[new_position[1]][new_position[0]] == "B":
            PoolSound.play()
            return

        if self.map[new_position[1]][new_position[0]] == "N":
            PoolSound.play()
            return

        if self.map[new_position[1]][new_position[0]] == "M":
            PoolSound.play()
            return

        if self.map[new_position[1]][new_position[0]] == "L":
            PoolSound.play()
            return
        
        if self.map[new_position[1]][new_position[0]] == "O":
            PoolSound.play()
            return

        if self.map[new_position[1]][new_position[0]] == "I":
            PoolSound.play()
            return

        unit.update_position(new_position)

    # Collision
    
    #Declaring images with a letter in order to make the map on the txt file
map_tile_images = {

    "G" : pygame.transform.scale(pygame.image.load("imgs/grass3.png"), (config.SCALE, config.SCALE)),
    "W": pygame.transform.scale(pygame.image.load("imgs/house_floor.png"), (config.SCALE, config.SCALE)),
    "H": pygame.transform.scale(pygame.image.load("imgs/house_wall.png"), (config.SCALE, config.SCALE)),
    "U": pygame.transform.scale(pygame.image.load("imgs/pool_t_l.png"), (config.SCALE, config.SCALE)),
    "I": pygame.transform.scale(pygame.image.load("imgs/pool_t_m.png"), (config.SCALE, config.SCALE)),
    "O": pygame.transform.scale(pygame.image.load("imgs/pool_t_r.png"), (config.SCALE, config.SCALE)),
    "J": pygame.transform.scale(pygame.image.load("imgs/pool_m_l.png"), (config.SCALE, config.SCALE)),
    "K": pygame.transform.scale(pygame.image.load("imgs/pool_m_m.png"), (config.SCALE, config.SCALE)),
    "L": pygame.transform.scale(pygame.image.load("imgs/pool_m_r.png"), (config.SCALE, config.SCALE)),
    "B": pygame.transform.scale(pygame.image.load("imgs/pool_b_l.png"), (config.SCALE, config.SCALE)),
    "N": pygame.transform.scale(pygame.image.load("imgs/pool_b_m.png"), (config.SCALE, config.SCALE)),
    "M": pygame.transform.scale(pygame.image.load("imgs/pool_b_r.png"), (config.SCALE, config.SCALE)),
    "X": pygame.transform.scale(pygame.image.load("imgs/road_r.png"), (config.SCALE, config.SCALE)),
    "Z": pygame.transform.scale(pygame.image.load("imgs/road_l.png"), (config.SCALE, config.SCALE))
}