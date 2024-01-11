class SoundLoader:
    def __init__(self, pygame):
        self.pygame = pygame
        # Load sounds
        self.sound_click = pygame.mixer.Sound('assets/sounds/click.wav')
        self.sound_click.set_volume(0.3)