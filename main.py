# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
from constants import *

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting Asteroids!")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return    
        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()  # Update display

if __name__ == "__main__":
    main()
    



    
