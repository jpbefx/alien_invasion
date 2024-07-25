# James Bailey July 24, 2024
#   Chapter 13 'Python Crash Course' textbook Pg 273

class GameStats:
    """Track statistics for Alioen Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit

        # Start Alien Invasion in an active state. Pg. 276
        self.game_active = True