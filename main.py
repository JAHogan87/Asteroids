import pygame
from constants import *
from logger import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys


def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0.0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player1 = Player (SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	Asteroid.containers = (asteroids, updatable, drawable)


	while True:
		dt = clock.tick(60)/1000
		
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		updatable.update(dt)

		for ast in asteroids:
			if player1.collides_with(ast) == True:
				(log_event("player_hit"))
				print("Game over!")
				sys.exit()

		for obj in drawable:
			obj.draw(screen)
		log_state()
		pygame.display.flip()

		
if __name__ == "__main__":
    main()
