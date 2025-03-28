import pygame
import random
from circleShape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.rotation = 0
        self.lineWidth = 2

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), self.position, self.radius, self.lineWidth)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            newRadius = self.radius - ASTEROID_MIN_RADIUS

            (x, y) = self.position
            newAsteroids = [Asteroid(x, y, newRadius), Asteroid(x, y, newRadius)]

            for na in newAsteroids:
                na.radius = newRadius

                multiplier = 1
                if newAsteroids.index(na) > 0:
                    multiplier = -1

                newV = self.velocity.rotate(angle * multiplier)

                na.velocity = newV

