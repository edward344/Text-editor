#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from keyboard import Keyboard

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

class Editor(object):
    def __init__(self):
        self.keyboard = Keyboard()
        self.font = pygame.font.SysFont("Calibri",25,True,False) 
        self.text_list = []
        

    def process_events(self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                return True
            # Run keyboard event handler
            self.keyboard.event_handler(event)
            # Check for return key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.add_new_line()

        return False

    def add_new_line(self):
        self.text_list.append(self.keyboard.text)
        self.keyboard.text = ""

    def run_logic(self):
        # Get the size of a letter
        size = self.font.size("a")
        letter_width = size[0]
        # Get the width of the new line
        size = self.font.size(self.keyboard.text)
        width = size[0]
        # add both to get the total width
        total_width = width + letter_width
        # Check if the line is longer than the screen width
        if total_width > SCREEN_WIDTH:
            self.add_new_line()

    def display_frame(self,screen):
        # First, clear the screen to white. Don't put other drawing commands
        screen.fill(WHITE)
        # --- Drawing code should go here
        # get the height of the font
        size = self.font.size("abc")
        height = size[1] + 2
        # draw all the lines onto the screen
        for index, item in enumerate(self.text_list):
            label = self.font.render(item,True,BLACK)
            # Go ahead and draw the label
            screen.blit(label,(0,height * index))

        # Get the total height of the text
        t_h = len(self.text_list) * height
        # Draw the new line onto the screen
        new_line = self.font.render(self.keyboard.text,True,BLACK)
        screen.blit(new_line,(0,t_h))
        # Get the width of the line
        width = new_line.get_width()
        # Draw the cursor onto the screen
        pygame.draw.line(screen, RED, [width,t_h], [width,t_h + height], 3)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
