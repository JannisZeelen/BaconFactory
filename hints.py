class Hints:
    def __init__(self, pygame, ticks):
        # Hints
        self.hints = ['Click the Bacon to progress!',
                      'Get passive income by buying new items!',
                      'Your clickrate increases when you buy 5 and 10 of one item!',
                      'Unlock new items by buying more items.',
                      'Rumors say there is an ending.']
        self.current_hint_index = 0
        self.hint_timer = ticks
        self.hint_duration = 5000  # Display each hint for 5 seconds
