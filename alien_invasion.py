# James Bailey January 11, 2024
#   Chapter 12 'Python Crash Course' textbook Pg 229.

import sys # Pg. 229
from time import sleep # Pg. 274

import pygame # Pg. 229

#   Adding settings.py to access instance of Settings (pg. 232)
from settings import Settings

from game_stats import GameStats # Pg. 274

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

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()    # Adding Sprite Group to hold fired bullets Pg. 248
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    # Adding organization to the code by bringing the oversaturated bullet settings out of run_game()
        # Pg. 252
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""    
        # Update bullet positions.
        # Get rid of bullets that have disappeared, Pg. 251
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        # add a call to new method _check_bullet_alien_collisions()
        self._check_bullet_alien_collisions()

    ##  Breaking _update_bullets(self) here and refactoring Pg. 271 ##

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions.""" 
        # Check to see if any bullets have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        # Check for no aliens in fleet
        # if not any aliens in fleet, create new fleet
        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()

    # added method to handle gameplay after the ship is hit by aliens Pg. 274
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        ### Added If Else statement and indented all inner code per Game Over! Pg. 276-277
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause game for player ready
            sleep(0.5)
        else:
            self.stats.game_active = False


    def _update_aliens(self):
        """Check if the fleet is at an edge,
                then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Ending the Game Pg. 272
        # Loof for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!")
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen. Pg. 276
        self._check_aliens_bottom()

# for testing            print(len(self.bullets))
                
    # Adding helpter function to create the aliens group sprites (Pg. 258)
        # Make an alien. (Pg. 258)
#        alien = Alien(self)
#        self.aliens.add(alien)

        # Create the first row of aliens. Pg. 260
#        alien = Alien(self)
#        alien_width = alien.rect.width
#        available_space_x = self.settings.screen_width - (2 * alien_width)
#        number_aliens_x = available_space_x // (2 * alien_width)


#        for alien_number in range(number_aliens_x):
#            # Create an alien and place it in the row.
#            alien = Alien(self)
#            alien.x = alien_width + 2 * alien_width * alien_number
#            alien.rect.x = alien.x
#            self.aliens.add(alien)

        # REFACTORING _create_fleet() Pg. 262
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create the first row of aliens.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x): 
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events() # Pg. 236
            self.ship.update() # Pg. 240
            self.bullets.update() # Pg. 249
            self._update_bullets() # Pg. 252
            self._update_aliens() # Pg. 265
            self._update_screen() # Pg. 237
            self.ship.update()
    
    #   Aliens that Reach the Bottom of the Screen Pg. 276
    def _check_aliens_bottom(self):
        """Check if any aliens have reached to bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the ship got hit.
                self._ship_hit()
                break

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