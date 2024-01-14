class ButtonCreator:
    def __init__(self, pygame, asset_loader, screen, upgrades, images):
        self.pygame = pygame
        self.asset_loader = asset_loader
        self.screen = screen

        # Skill buttons
        self.skill_buttons_data = [
            {"owned": upgrades.upgrade_0_owned, "skill_image": images.upgrade_0_skill, "rect": upgrades.skill_rect,
             "hover_text": '', "fallback_image": images.question_mark_skill},
            {"owned": upgrades.upgrade_1_owned, "skill_image": images.upgrade_1_skill, "rect": upgrades.skill_rect2,
             "hover_text": '1', "fallback_image": images.question_mark_skill},
            {"owned": upgrades.upgrade_2_owned, "skill_image": images.upgrade_2_skill, "rect": upgrades.skill_rect3,
             "hover_text": '2', "fallback_image": images.question_mark_skill},
            {"owned": upgrades.upgrade_3_owned, "skill_image": images.upgrade_3_skill, "rect": upgrades.skill_rect4,
             "hover_text": '3', "fallback_image": images.question_mark_skill},
            {"owned": upgrades.upgrade_4_owned, "skill_image": images.upgrade_4_skill, "rect": upgrades.skill_rect5,
             "hover_text": '4', "fallback_image": images.question_mark_skill},
            {"owned": upgrades.upgrade_5_owned, "skill_image": images.upgrade_4_skill, "rect": upgrades.skill_rect6,
             "hover_text": '5', "fallback_image": images.question_mark_skill},
            {"owned": upgrades.upgrade_6_owned, "skill_image": images.upgrade_4_skill, "rect": upgrades.skill_rect7,
             "hover_text": '6', "fallback_image": images.question_mark_skill},
            {"owned": upgrades.upgrade_7_owned, "skill_image": images.upgrade_4_skill, "rect": upgrades.skill_rect8,
             "hover_text": '7', "fallback_image": images.question_mark_skill},
            # {"owned": upgrades.balance.value >= 1000000, "skill_image": images.upgrade_4_skill,
            # "rect": upgrades.skill_rect9, "hover_text": '', "fallback_image": images.question_mark_skill}, TODO Ending
        ]
        # Upgrade Button
        self.upgrade_buttons_data = [
            {"condition": True, "rect": upgrades.buy_upgrade_0_button_rect, "label": "Upgrade 0",
             "cost": upgrades.upgrade_0_cost, "increase": upgrades.upgrade_0_increase,
             "owned": upgrades.upgrade_0_owned,
             "image": images.upgrade_0_upgrade},
            {"condition": False, "rect": upgrades.buy_upgrade_1_button_rect,
             "label": "Upgrade 1",
             "cost": upgrades.upgrade_1_cost, "increase": upgrades.upgrade_1_increase,
             "owned": upgrades.upgrade_1_owned,
             "image": images.upgrade_1_upgrade},
            {"condition": False, "rect": upgrades.buy_upgrade_2_button_rect,
             "label": "Upgrade 2",
             "cost": upgrades.upgrade_2_cost, "increase": upgrades.upgrade_2_increase,
             "owned": upgrades.upgrade_2_owned,
             "image": images.upgrade_2_upgrade},
            {"condition": False, "rect": upgrades.buy_upgrade_3_button_rect,
             "label": "Upgrade 3",
             "cost": upgrades.upgrade_3_cost, "increase": upgrades.upgrade_3_increase,
             "owned": upgrades.upgrade_3_owned,
             "image": images.upgrade_3_upgrade},
            {"condition": False, "rect": upgrades.buy_upgrade_4_button_rect,
             "label": "Upgrade 4",
             "cost": upgrades.upgrade_4_cost, "increase": upgrades.upgrade_4_increase,
             "owned": upgrades.upgrade_4_owned,
             "image": images.upgrade_4_upgrade},
            {"condition": False, "rect": upgrades.buy_upgrade_5_button_rect,
             "label": "Upgrade 5",
             "cost": upgrades.upgrade_5_cost, "increase": upgrades.upgrade_5_increase,
             "owned": upgrades.upgrade_5_owned,
             "image": images.upgrade_4_upgrade},
            {"condition": False, "rect": upgrades.buy_upgrade_6_button_rect,
             "label": "Upgrade 6",
             "cost": upgrades.upgrade_6_cost, "increase": upgrades.upgrade_6_increase,
             "owned": upgrades.upgrade_6_owned,
             "image": images.upgrade_4_upgrade},
            {"condition": False, "rect": upgrades.buy_upgrade_7_button_rect,
             "label": "Upgrade 7",
             "cost": upgrades.upgrade_7_cost, "increase": upgrades.upgrade_7_increase,
             "owned": upgrades.upgrade_7_owned,
             "image": images.upgrade_4_upgrade},
        ]

    def update_upgrade_button_data(self, upgrade_number, new_cost):
        # This method will update the hover label for the specified upgrade button
        for button_data in self.upgrade_buttons_data:
            if button_data["label"] == f"Upgrade {upgrade_number}":
                button_data["cost"] = new_cost
                break
    def update_skill_button_data(self, upgrade_number, new_label):
        # This method will update the cost data for the specified upgrade button
        for button_data in self.upgrade_buttons_data:
            # if button_data["owned"] == self.upgrades.upgrade_0_owned:
            button_data["hover_text"] = f"Upgrade {upgrade_number} earnings x{new_label}"
            print(button_data["hover_text"])
            break

    def create_skill_button(self, image, rect, hover_text, color, pygame):

        # Borders
        border_thickness = 2  # You can adjust this value according to your preference
        border_color = 'white'  # Choose the color of the border

        # Coordinates
        info_x = rect.right + 10
        info_y = rect.top

        # Draw Button
        pygame.draw.rect(self.screen, color, rect)  # 209, 50, 36

        self.screen.blit(image, (rect.left + 5, rect.top + 5))

        # Check if the mouse is hovering over the skill button
        if rect.collidepoint(pygame.mouse.get_pos()):
            hover_text_rendered = self.asset_loader.font_18.render(hover_text, True, (0, 0, 0))

            # Create a transparent surface for the hover text rectangle
            hover_rect_surface = pygame.Surface((hover_text_rendered.get_width(), hover_text_rendered.get_height()),
                                                pygame.SRCALPHA)
            hover_rect_surface.fill((0, 0, 0, 0))  # 128 is the alpha value for transparency

            # Draw the transparent hover text surface
            self.screen.blit(hover_rect_surface, (info_x, info_y))
            self.screen.blit(hover_text_rendered, (info_x, info_y))
        pygame.draw.rect(self.screen, border_color, rect, border_thickness)

    def create_button(self, rect, color, label, cost, bps_increase, owned, image, pygame, upgrades, images):
        # Borders
        border_thickness = 2  # You can adjust this value according to your preference
        border_color = (255, 255, 255)  # Choose the color of the border

        info_x = rect.right + 10
        info_y = rect.top - 7

        # Check if the mouse is over the button
        mouse_over_button = rect.collidepoint(pygame.mouse.get_pos())

        # Check if the mouse button is pressed
        mouse_pressed = pygame.mouse.get_pressed()[0]

        # Adjust the color based on mouse state
        if mouse_over_button and mouse_pressed:
            color = (214, 80, 69)

        # Draw button
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, border_color, rect, border_thickness)
        text = self.asset_loader.font_22.render(label, True, (255, 255, 255))
        cost_text_color = (58, 189, 2) if upgrades.balance >= cost else (
            184, 180, 180)  # Green if balance >= cost, el red

        cost_text = self.asset_loader.font_18.render(f"{cost.formatted()} +{bps_increase.formatted()}/s", True,
                                                     cost_text_color)
        self.screen.blit(cost_text, (info_x - 165, info_y + 32))
        owned_text = self.asset_loader.font_24.render(f"{owned.value}", True, (201, 201, 201))
        owned_text.set_alpha(150)
        self.screen.blit(images.balance_icon, (info_x - 180, info_y + 36))
        self.screen.blit(owned_text, (info_x - 45, info_y + 8))
        # Position the text next to the button
        self.screen.blit(text, (info_x - 180, info_y + 10))

        # Draw the image
        self.screen.blit(image, (info_x - 230, info_y + 12))
