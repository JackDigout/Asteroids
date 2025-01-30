import random
from circleshape import *
from constants import *
from player import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        points = 0

        if self.radius <= ASTEROID_MIN_RADIUS:
            points += 100  # Small asteroids worth more points
        elif self.radius <= ASTEROID_MIN_RADIUS * 2:
            points += 50   # Medium asteroids worth medium points
        else:
            points += 25   # Large asteroids worth fewer points
        
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return points
        else:
            
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(-angle)
            vector2 = self.velocity.rotate(angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2

            return points
            

