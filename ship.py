# James Bailey January 11, 2024
#   Chapter 12 'Python Crash Course' textbook Pg 233-234

import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings    # Pg. 242
        self.screen_rect = ai_game.screen.get_rect()

        #   Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #   Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
                # Pg. 239
        
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x) # Pg. 242

        # Movement flag 
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the sip's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: # self.moving_right: // Test Code to move the ship, but not limit the range # Pg. 243
            self.x += self.settings.ship_speed  # self.rect.x += 1 \\ Test Code moving only the rectangle (rect) Pg. 242
        if self.moving_left and self.rect.left > 0: # self.moving_left: # Pg. 240    // Test Code to move the ship, but not limit the range # Pg. 243
            self.x -= self.settings.ship_speed  # self.rect.x -= 1 \\ Test Code moving only the rectangle (rect) Pg. 242
        
        # Update rectangle (rect) object from self.x
        self.rect.x = self.x    # Pg. 242

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    # Recenter ship when hit by aliens, called in alien_invasion._ship_hit() Pg. 275
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)