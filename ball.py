import pygame
import math
import time



class ball():
    def __init__(self, x=0, y=0, screen = None):
        self.x = x
        self.y = y
        self.screen = screen
        
        self.g_constant = 9.81
        self.gravity = False
        
        self.vertical_velocity_when_bounce = 0
        self.vertical_velocity = 0
        self.go_up = False
        self.go_down = True
        self.time_start_falling_vertical = 0
        
        self.horizontal_velocity_when_bounce = 0
        self.horizontal_velocity = 10
        self.go_left = False
        self.go_right = True
        self.time_horizontal = 0

        self.friction = 1/500

        self.radius = 30
        self.e = 0.95
        self.x_c, self.y_c = self.screen.get_size()
        self.last_height = self.y_c

    def set_ball_co(self, x,y):
        self.x = x
        self.y = y

    def refresh(self): 
        #print(f"up : {self.go_up} || down : {self.go_down} ")
        #print(self.horizontal_velocity)
        if self.gravity: #si la gravité est activée
            if self.go_down: #si la balle descend
                self.vertical_velocity = self.g_constant * (time.time()- self.time_start_falling_vertical) #on change la vitesse verticale 
                self.y += self.vertical_velocity #on modifie les co
            if self.go_up: #si la balle monte
                self.vertical_velocity = self.vertical_velocity_when_bounce - (self.g_constant *(time.time()- self.time_start_falling_vertical)) #on modifie la vitesse verticale
                self.y -= self.vertical_velocity #on modifie les coordonnées
                if  -0.5 <= self.vertical_velocity <= 0.5: #quand elle arrive vers le max de sa hauteur
                    #print("CHANGE !!!!")
                    self.time_start_falling_vertical = time.time()
                    self.toggle_go_vertical()

            if self.go_left: #Si la balle va a gauche
                self.horizontal_velocity = self.horizontal_velocity - self.horizontal_velocity *self.friction #On lui retire de sa vitesse
                self.x -= self.horizontal_velocity
            
            if self.go_right:
                self.horizontal_velocity = self.horizontal_velocity - self.horizontal_velocity *self.friction
                self.x += self.horizontal_velocity
            
            if   self.y + self.radius + self.vertical_velocity >= self.y_c: #Quand elle rebondie vertical
                    if self.vertical_velocity < 0.1: #Si la vitesse est trop basse, on arrete
                        self.vertical_velocity = 0
                        self.gravity = False
                        self.go_down = False
                        self.go_up = False
                    else : #Sinon elle part vers le haut
                        self.vertical_velocity_when_bounce = self.e*self.vertical_velocity
                        self.time_start_falling_vertical = time.time()
                        self.vertical_velocity = 0
                        self.toggle_go_vertical()
            


            if   self.x - self.radius - self.horizontal_velocity <= 0: #Quand elle rebondie horizontal (gauche)
                        #self.horizontal_velocity = - self.horizontal_velocity
                        self.toggle_go_horizontal()

            if   self.x + self.radius + self.horizontal_velocity >= self.x_c: #Quand elle rebondie horizontal (gauche)
                        #self.horizontal_velocity = - self.horizontal_velocity
                        self.toggle_go_horizontal()

    def set_ball_x(self, x):
        self.x = x

    def toggle_go_horizontal(self):
        self.go_left = not self.go_left
        self.go_right = not self.go_right


    def toggle_go_vertical(self):
        self.go_down = not self.go_down
        self.go_up = not self.go_up

    def enable_gravity(self):
        self.gravity = True
        self.time_start_falling_vertical = time.time()
        self.time_horizontal = time.time()

    def disable_gravity(self):
        self.gravity = False

    def set_ball_y(self, y):
        self.y = y

    def send_ball_to_center(self):
        x_c, y_c = self.screen.get_size()
        self.x = x_c/2
        self.y = y_c/2

    def send_ball_to_the_top(self):
        x_c, y_c = self.screen.get_size()
        self.x = x_c/2
        self.y = 0

    def draw_ball(self):

        pygame.draw.circle(self.screen, (255,255,255), (self.x,self.y), self.radius)
        