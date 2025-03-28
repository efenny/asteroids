import pygame
from circleShape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_cooldown = 0
        self.lineWidth = 2

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color(255,255,255), self.triangle(), self.lineWidth)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(dt * -1)
        elif keys[pygame.K_SPACE]:
            self.shoot()

        self.shoot_cooldown -= dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        else:
            (x, y) = self.position
            s = Shot(x, y)
            s.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

