import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        vector_spawn_1 = self.velocity.rotate(random_angle) * 1.2
        vector_spawn_2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1= Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2= Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vector_spawn_1
        asteroid_2.velocity = vector_spawn_2

        return asteroid_1, asteroid_2

