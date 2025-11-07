import pygame


class Wall():
    def __init__(self,screen, co = (100,300), largeur = 300, hauteur = 10):
        self.screen = screen
        self.x = co[0]
        self.y = co[1]
        self.largeur = largeur
        self.hauteur = hauteur


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_largeur(self):
        return self.largeur
    
    def get_hauteur(self):
        return self.hauteur

    def draw_wall(self):
        pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, self.largeur, self.hauteur))
