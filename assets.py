class AssetsLoader:
    def __init__(self, pygame):
        # Fonts
        self.font_18 = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 18)
        self.font_20 = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 20)
        self.font_22 = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 22)
        self.font_24 = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 24)
        self.font_26 = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 26)
        self.font_28 = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 28)
        self.font_32 = pygame.font.Font('assets/fonts/LuckiestGuy-Regular.ttf', 32)

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.light_green = (167, 174, 74)
        self.green = (118, 132, 59)
