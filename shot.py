import pygame
from circleShape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

        self.rotation = 0
        self.lineWidth = 2

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), self.position, self.radius, self.lineWidth)

    def update(self, dt):
        self.position += self.velocity * dt
