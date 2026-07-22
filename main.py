import pygame
import game

#Variables
HEIGHT = 720
WIDTH = 1280
#Init game 
main_game = game.Game(WIDTH, HEIGHT)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GMTK 2026")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    main_game.Draw(screen)
    main_game.Scrolling()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()