import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)


    while True:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()