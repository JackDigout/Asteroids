import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys
import pygame.font


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)  # None uses default font, 36 is size
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    afield = AsteroidField()
    
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        

        for asteroid in asteroids:
            if player1.collision(asteroid):
                print("Game Over!")
                
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    points = asteroid.split()
                    score += points
                    
            
        # Clear the screen by filling it with black color
        screen.fill("black")
        
        # Draw all objects in the `drawable` group
        for drawable_object in drawable:
            drawable_object.draw(screen)
        
        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White text
        screen.blit(score_text, (10, 10))  # Position in top-left corner
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()