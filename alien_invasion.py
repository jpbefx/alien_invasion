# James Bailey January 11, 2024
#   Chapter 12 'Python Crash Course' textbook Pg 229.

import sys

import pygame

#   Adding settings.py to access instance of Settings (pg. 232)
from settings import Settings

#   Adding the Ship class from the ship.py module
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        #   Pg (232)
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #   Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #   Redraw the screen during each pass through the loop. (pg 231)
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #   Make the most recently drawn screen visible.
            pygame.display.flip()
        

if __name__ == '__main__':
    #   Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()