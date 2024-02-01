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


        ## TESTING VARIABLE SHIP_SPEED ON MY OWN: FAIL
#        if self.screen_width >= 1250:
#                self.ship_speed = 6
#        elif self.screen_width <= 1200:
#                self.ship_speed = 1.5