class Hints:
    def __init__(self, pygame):
        self.hints = ['Click the Bacon to progress!',
                      'Get passive income by buying new items!',
                      'Your clickrate increases when you buy 5 and 10 of one item!',
                      'Unlock new items by buying more items.',
                      'Rumors say there is an ending.']
        self.current_hint_index = 0
        self.hint_timer = pygame.time.get_ticks()
        # print(self.hint_timer)
        self.hint_duration = 5000  # Display each hint for 5 seconds
        self.current_hint = self.hints[self.current_hint_index]

    def update_hints(self, pygame):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.hint_timer
        if elapsed_time >= self.hint_duration:
            self.hint_timer = current_time
            self.current_hint_index = (self.current_hint_index + 1) % len(self.hints)
            self.current_hint = self.hints[self.current_hint_index]
