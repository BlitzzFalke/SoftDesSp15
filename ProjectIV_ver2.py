import pygame
from pygame.locals import *
import random
import math
import time


class ShapeModel:
    """ Encodes the game state """
    def __init__(self):
        white = Rectangle(20, 20, 615, 5, (255, 255, 255))
        black = Rectangle(20, 20, 615, 25, (0, 0, 0))
        red = Rectangle(20, 20, 615, 45, (255, 0, 0))
        green = Rectangle(20, 20, 615, 65, (0, 255, 0))
        blue = Rectangle(20, 20, 615, 85, (0, 0, 255))
        
        self.new_color = (255, 255, 255)
        self.rectangles = [white, black, red, green, blue]
        self.drawing = False
        
        self.x = 0
        self.y = 0

    def create_rectangle(self, xpos, ypos):
        rectangle = Rectangle(5, 5, xpos, ypos, self.new_color)
        self.rectangles.append(rectangle)

    def update(self, mouse_xpos, mouse_ypos):
        if self.drawing == True:
            #print len(self.rectangles)
            self.create_rectangle(mouse_xpos, mouse_ypos)
              

class Rectangle:
    """ Encodes the state of a rectangle in the game """
    def __init__(self, height, width, x, y, color):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = color

class ShapeView:
    """ A view of shape game rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for rectangle in self.model.rectangles:
            pygame.draw.rect(self.screen, rectangle.color,pygame.Rect(rectangle.x,rectangle.y,rectangle.width,rectangle.height))
        pygame.display.update()

class ShapeController:
    """ responds to user input (mouse click and position)"""
    def __init__(self,model):
        self.model = model
    
    def handle_keyboard_event(self,event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if mouse_position[0] in range (615, 635):
                if mouse_position[1] in range(5, 25):
                    self.model.new_color = (255, 255, 255)
                elif mouse_position[1] in range(25, 45):
                    self.model.new_color = (0, 0, 0)
                elif mouse_position[1] in range(45, 65):
                    self.model.new_color = (255, 0, 0)
                elif mouse_position[1] in range(65, 85):
                    self.model.new_color = (0, 255, 0)
                elif mouse_position[1] in range(85, 105):
                    print "true"
                    self.model.new_color = (0, 0, 255)

            self.model.x = mouse_position[0]
            self.model.y = mouse_position[1]
            self.model.drawing = True
        elif event.type == MOUSEBUTTONUP:
            self.model.drawing = False

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = ShapeModel()
    view = ShapeView(model,screen)
    controller = ShapeController(model)
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                print len(model.rectangles)
                running = False
            else: #event.type == MOUSEBUTTONDOWN or MOUSEBUTTONUP:
                controller.handle_keyboard_event(event)
        model.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        view.draw()
        time.sleep(.00001)

    pygame.quit()

