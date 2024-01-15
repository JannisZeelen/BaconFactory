class ImageLoader:
    def __init__(self, pygame):
        self.pygame = pygame

        # Click Image
        self.click_button_image = pygame.image.load("assets/img/clicker.png")
        self.click_button_image2 = pygame.image.load("assets/img/clicker2.png")
        # self.click_button_image = pygame.transform.scale(self.click_button_image, (180, 270))
        self.click_button_image2 = pygame.transform.scale(self.click_button_image2, (180, 180))

        # Logo, Upgrades Title, Separator, Balance Icon
        self.logo_image = pygame.image.load("assets/img/logo.png")
        self.logo_image = pygame.transform.scale(self.logo_image, (170 * 1.5, 64 * 1.5))

        self.upgrades_image = pygame.image.load("assets/img/upgrades.png")
        self.separator_image = pygame.image.load("assets/img/separator.png")
        self.balance_icon_image = pygame.image.load("assets/img/balance.png")
        self. balance_icon = pygame.transform.scale(self.balance_icon_image, (16, 16))
        self.balance_img = pygame.transform.scale(self.balance_icon_image, (25, 25))

        # Mouse Pointer
        self.mouse_pointer_image = pygame.image.load("assets/img/upgrade_0.png")
        self.mouse_pointer = pygame.transform.scale(self.mouse_pointer_image, (40, 40))

        # Background
        self.background = pygame.image.load("assets/img/background.png")
        self.overlap = pygame.image.load("assets/img/background.png")

        # Upgrades / Skills
        self.upgrade_0_image = pygame.image.load("assets/img/upgrade_0.png")
        self.upgrade_0_upgrade = pygame.transform.scale(self.upgrade_0_image, (50, 50))
        self.upgrade_0_skill = pygame.transform.scale(self.upgrade_0_image, (50 - 10, 50 - 10))

        self.upgrade_1_image = pygame.image.load("assets/img/upgrade_1.png")
        self.upgrade_1_upgrade = pygame.transform.scale(self.upgrade_1_image, (50, 50))
        self.upgrade_1_skill = pygame.transform.scale(self.upgrade_1_image, (50 - 10, 50 - 10))

        self.upgrade_2_image = pygame.image.load("assets/img/upgrade_2.png")
        self.upgrade_2_upgrade = pygame.transform.scale(self.upgrade_2_image, (50, 50))
        self.upgrade_2_skill = pygame.transform.scale(self.upgrade_2_image, (50 - 10, 50 - 10))

        self.upgrade_3_image = pygame.image.load("assets/img/upgrade_3.png")
        self.upgrade_3_upgrade = pygame.transform.scale(self.upgrade_3_image, (50, 50))
        self.upgrade_3_skill = pygame.transform.scale(self.upgrade_3_image, (50 - 10, 50 - 10))

        self.upgrade_4_image = pygame.image.load("assets/img/upgrade_4.png")
        self.upgrade_4_upgrade = pygame.transform.scale(self.upgrade_4_image, (50, 50))
        self.upgrade_4_skill = pygame.transform.scale(self.upgrade_4_image, (50 - 10, 50 - 10))

        self.question_mark_skill_image = pygame.image.load("assets/img/question_mark.png")
        self.question_mark_skill = pygame.transform.scale(self.question_mark_skill_image, (50 - 10, 50 - 10))
