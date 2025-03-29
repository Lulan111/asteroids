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

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updateable, drawable)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )

def main():
    print("Starting Asteroids!")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return   
            
        zeit = clock.tick(60)
        dt = zeit / 1000
        screen.fill((0, 0, 0))  # Fill screen with black
        for entity in drawable:
            entity.draw(screen)
        updateable.update(dt)
        pygame.display.flip()  # Update display
       

if __name__ == "__main__":
    main()
    



    
