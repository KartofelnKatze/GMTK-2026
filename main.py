import pygame
import game
import menu

#Variables
HEIGHT = 720
WIDTH = 1280
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GMTK 2026")
clock = pygame.time.Clock()
running = True
#Init game 
main_game = game.Game(WIDTH, HEIGHT)
main_menu = menu.Menu()

game_start = main_menu.game_start

while running:
    game_start = main_menu.game_start
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    if game_start :
        main_game.Draw(screen)
        main_game.update(events)
    else :
        main_menu.Draw(screen)
        main_menu.update(events)
        main_game.clock.tick(60)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()