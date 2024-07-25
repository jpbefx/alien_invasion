# James Bailey January 11, 2024
#   Chapter 12 'Python Crash Course' textbook Pg 231.

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #   Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 6 # Pg. 242
        self.ship_limit = 3 # Pg. 274

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Bullet Settings Pg. 247
        self.bullet_speed = 1.0
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Limiting the amount of bullets to promote accuracy Pg. 251
        self.bullets_allowed = 9


        ## TESTING VARIABLE SHIP_SPEED ON MY OWN: FAIL
#        if self.screen_width >= 1250:
#                self.ship_speed = 6
#        elif self.screen_width <= 1200:
#                self.ship_speed = 1.5