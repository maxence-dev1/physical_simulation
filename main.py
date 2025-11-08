import ball as b
import wall as w
import pygame
import time


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))
ball = b.ball(100,100, screen)
wall = w.Wall(screen )
ball.add_wall_tab(wall)
running = True
while running:
    time.sleep(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ball.send_ball_to_center()
            if event.key == pygame.K_c:
                ball.toggle_go_horizontal()
            if event.key == pygame.K_t:
                ball.send_ball_to_the_top()
            if event.key == pygame.K_g:
                ball.enable_gravity()
    screen.fill((0,0,0))
    ball.refresh()           
    ball.draw_ball()
    wall.draw_wall()

    pygame.display.flip()
    clock.tick(60)

