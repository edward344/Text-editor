#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Keyboard(object):
    def __init__(self):
        self.text = ""
        self.uppercase = False

    def set_letter(self,letter):
        # Convert to uppercase if uppercase is true
        if self.uppercase:
            self.text += letter.upper()
        else:
            self.text += letter
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                self.uppercase = True
            # Check for all the letter
            elif event.key == pygame.K_a:
                self.set_letter("a")
            elif event.key == pygame.K_b:
                self.set_letter("b")
            elif event.key == pygame.K_c:
                self.set_letter("c")
            elif event.key == pygame.K_d:
                self.set_letter("d")
            elif event.key == pygame.K_e:
                self.set_letter("e")
            elif event.key == pygame.K_f:
                self.set_letter("f")
            elif event.key == pygame.K_g:
                self.set_letter("g")
            elif event.key == pygame.K_h:
                self.set_letter("h")
            elif event.key == pygame.K_i:
                self.set_letter("i")
            elif event.key == pygame.K_j:
                self.set_letter("j")
            elif event.key == pygame.K_k:
                self.set_letter("k")
            elif event.key == pygame.K_l:
                self.set_letter("l")
            elif event.key == pygame.K_m:
                self.set_letter("m")
            elif event.key == pygame.K_n:
                self.set_letter("n")
            elif event.key == pygame.K_o:
                self.set_letter("o")
            elif event.key == pygame.K_p:
                self.set_letter("p")
            elif event.key == pygame.K_q:
                self.set_letter("q")
            elif event.key == pygame.K_r:
                self.set_letter("r")
            elif event.key == pygame.K_s:
                self.set_letter("s")
            elif event.key == pygame.K_t:
                self.set_letter("t")
            elif event.key == pygame.K_u:
                self.set_letter("u")
            elif event.key == pygame.K_v:
                self.set_letter("v")
            elif event.key == pygame.K_w:
                self.set_letter("w")
            elif event.key == pygame.K_x:
                self.set_letter("x")
            elif event.key == pygame.K_y:
                self.set_letter("y")
            elif event.key == pygame.K_z:
                self.set_letter("z")
            # Check for space
            elif event.key == pygame.K_SPACE:
                self.text += " "
            # Check for period
            elif event.key == pygame.K_PERIOD:
                self.text += "."
            # Check for comma
            elif event.key == pygame.K_COMMA:
                self.text += ","
            # Check for numbers
            elif event.key == pygame.K_0:
                self.text += "0"
            elif event.key == pygame.K_1:
                self.text += "1"
            elif event.key == pygame.K_2:
                self.text += "2"
            elif event.key == pygame.K_3:
                self.text += "3"
            elif event.key == pygame.K_4:
                self.text += "4"
            elif event.key == pygame.K_5:
                self.text += "5"
            elif event.key == pygame.K_6:
                self.text += "6"
            elif event.key == pygame.K_7:
                self.text += "7"
            elif event.key == pygame.K_8:
                self.text += "8"
            elif event.key == pygame.K_9:
                self.text += "9"
            # check for backspace to delete the last character
            elif event.key == pygame.K_BACKSPACE:
                if len(self.text) > 1:
                    self.text = self.text[:len(self.text)-1]
                else:
                    self.text = ""
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                self.uppercase = False
