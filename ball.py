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
        
        #Vitesse verticale
        self.vertical_velocity_when_bounce = 0
        self.vertical_velocity = 0
        self.go_up = False
        self.go_down = True
        self.time_start_falling_vertical = 0
        
        #vitesse horizontale
        self.horizontal_velocity_when_bounce = 0
        self.horizontal_velocity = 1
        self.go_left = False
        self.go_right = True
        self.time_horizontal = 0

        self.friction = 1/500

        self.initial_speed = 50
        self.radius = 30
        self.e = 1
        self.speed_multiplicator = 1
        self.x_c, self.y_c = self.screen.get_size()
        self.last_height = self.y_c

        self.wall_tab = []

    def set_ball_co(self, x,y):
        self.x = x
        self.y = y

    def add_wall_tab(self, wall):
        self.wall_tab.append([wall.get_x(), wall.get_y(), wall.get_largeur(), wall.get_hauteur()])


    def refresh(self): 

        if self.gravity: #si la gravité est activée
            
            if self.go_down: #si la balle descend
                self.vertical_velocity = self.g_constant * (time.time()- self.time_start_falling_vertical) + self.initial_speed#on change la vitesse verticale 
                self.y += self.vertical_velocity*self.speed_multiplicator #on modifie les co
                if (self.initial_speed !=0):
                    print("clear")
                    self.initial_speed = 0
            if self.go_up: #si la balle monte
                self.vertical_velocity = self.vertical_velocity_when_bounce - (self.g_constant *(time.time()- self.time_start_falling_vertical)) #on modifie la vitesse verticale
                self.y -= self.vertical_velocity*self.speed_multiplicator #on modifie les coordonnées
                if  -0.5 <= self.vertical_velocity <= 0.5: #quand elle arrive vers le max de sa hauteur
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
                        self.vertical_bounce_go_down()
            

            if self.y-self.radius-self.vertical_velocity <= 0:
                 self.vertical_bounce_go_down()

            if self.go_left and self.x - self.radius - self.horizontal_velocity <= 0: #Quand elle rebondie horizontal (gauche)
                        #self.horizontal_velocity = - self.horizontal_velocity
                        self.horizontal_bounce()

            if self.go_right and self.x + self.radius + self.horizontal_velocity >= self.x_c: #Quand elle rebondie horizontal (droite)
                        #self.horizontal_velocity = - self.horizontal_velocity
                        self.horizontal_bounce()

            #On vérifie les collisions aux murs
            for wall in self.wall_tab:
                pygame.draw.circle(self.screen, (0,0,255), (wall[0], wall[1]), 5)
                pygame.draw.circle(self.screen, (255,0,0), (wall[0], wall[1]+wall[3]), 5)
                pygame.draw.circle(self.screen, (255,0,0), (wall[0]+wall[2], wall[1]+wall[3]), 5)
                pygame.draw.circle(self.screen, (0,255,0), (wall[0]+wall[2], wall[1]), 5)
                if self.go_down:
                    if (wall[0] <= self.x <= wall[0]+wall[2]) and wall[1]<= self.y+self.radius/2+self.vertical_velocity <= wall[1]+wall[3]:
                        self.vertical_bounce_go_down()
                elif self.go_up:
                    if (wall[0] <= self.x <= wall[0]+wall[2]) and wall[1]<= self.y-self.radius/2-self.vertical_velocity <= wall[1]+wall[3]:
                        print("wwewewe bounce")
                        self.vertical_bounce_go_up()
                     
                    
                        

                          
                     
    def vertical_bounce_go_down(self):
        self.vertical_velocity_when_bounce = self.e*self.vertical_velocity
        self.time_start_falling_vertical = time.time()
        self.vertical_velocity = 0
        self.toggle_go_vertical()

    def vertical_bounce_go_up(self):
        self.time_start_falling_vertical = time.time()
        self.initial_speed = self.vertical_velocity
        self.toggle_go_vertical()
    
    def horizontal_bounce(self):
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
        self.y = self.radius 

    def draw_ball(self):

        pygame.draw.circle(self.screen, (255,255,255), (self.x,self.y), self.radius)
        