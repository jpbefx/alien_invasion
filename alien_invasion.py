# James Bailey January 11, 2024
#   Chapter 12 'Python Crash Course' textbook Pg 229.

import sys

import pygame

#   Adding settings.py to access instance of Settings (pg. 232)
from settings import Settings

#   Adding the Ship class from the ship.py module
from ship import Ship

#   Adding the Bullet class from the bullet.py module (pg. 249)
from bullet import Bullet

#   Adding the Alien class from the alien.py module (pg. 258)
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        #   Pg (232)
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width   # rect = new screen rectangle size
        self.settings.screen_height = self.screen.get_rect().height    
        pygame.display.set_caption("Alien Invasion")        #("Alien Invasion", f"{self.settings.screen_width}, {self.settings.screen_height}")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()    # Adding Sprite Group to hold fired bullets Pg. 248
        self.aliens = pygame.sprite.Group()

        
    
    # Adding organization to the code by bringing the oversaturated bullet settings out of run_game()
        # Pg. 252
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""    
        # Update bullet positions.
        # Get rid of bullets that have disappeared, Pg. 251
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
# for testing            print(len(self.bullets))
                
    # Adding helpter function to create the aliens group sprites (Pg. 258)
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        self.aliens.add(alien)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events() # Pg. 236
            self.ship.update() # Pg. 240
            self.bullets.update() # Pg. 249
            self._update_bullets() # Pg. 252
            self._update_screen() # Pg. 237
            self.ship.update()
    
    ### Book has incorrect placement of ""#Redraw the screen during each pass through the loop."" snippet. ###
    def _check_events(self): # Pg. 237
        """Respond to keyboard and mouse events."""
        #   Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Pg. 238
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

                # Move the ship to the right.
                # Deprecated // self.ship.rect.x += 1 
                    # Movement value now located in Settings.py as ship_speed
                
    # Refactoring Key Events Pg. 244
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True # Pg. 239
        elif event.key == pygame.K_LEFT:    # Pg. 241
            self.ship.moving_left = True
        elif event.key == pygame.K_q: # pg. 244 Exit Game with 'Q'
            sys.exit()
        elif event.key == pygame.K_SPACE: # Pg. 249 "Firing Bullets"
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """REspond to keyreleases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:        # Pg. 241
            self.ship.moving_left = False

    # Creating method to fire bullets from the bullet module
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # Instantiate the amount of bullets within an if statement to allow new bullets Pg. 252
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self): # Pg. 237
        """Update images on the screen, and flip to the new screen."""
        #   Redraw the screen during each pass through the loop. (pg 231)
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # update the aliens sprite and draw to the screen (pg. 259)
        self.aliens.draw(self.screen)
        #   Make the most recently drawn screen visible.
        pygame.display.flip()
        

if __name__ == '__main__':
    #   Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()