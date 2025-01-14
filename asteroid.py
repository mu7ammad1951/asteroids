import pygame
import circleshape
import random
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity_A = self.velocity.rotate(angle)
        velocity_B = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_A = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_A.velocity = velocity_A * 1.2
        asteroid_B = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_B.velocity = velocity_B * 1.2