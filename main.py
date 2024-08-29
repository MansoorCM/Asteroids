import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    updatable_group.add(asteroid_field)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        for obj in updatable_group:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.has_collided(player):
                print("Game Over!")
                return
        for obj in drawable_group:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__== "__main__":
    main()