# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
from constants import *
from player import Player

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
dt = 0

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )

def main():
    print("Starting Asteroids!")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return    
        screen.fill((0, 0, 0))  # Fill screen with black
        player.draw(screen)
        pygame.display.flip()  # Update display
        zeit = clock.tick(60)
        dt = zeit / 1000

if __name__ == "__main__":
    main()
    



    
