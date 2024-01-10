class ButtonCreator:
    def __init__(self, pygame, asset_loader, screen):
        self.pygame = pygame
        self.asset_loader = asset_loader
        self.screen = screen

    def create_skill_button(self, image, rect, hover_text, color, pygame):
        # Borders
        border_thickness = 2  # You can adjust this value according to your preference
        border_color = 'white'  # Choose the color of the border

        # Coordinates
        info_x = rect.right + 10
        info_y = rect.top - 7

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

    def create_button(self, rect, color, label, cost, bps_increase, owned, image, pygame, upgrades):
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



        cost_text = self.asset_loader.font_18.render(f"B {cost:.2f} +{bps_increase:.2f}/s", True,
                                                     cost_text_color)
        self.screen.blit(cost_text, (info_x - 180, info_y + 32))
        owned_text = self.asset_loader.font_24.render(f"{owned}", True, (201, 201, 201))
        owned_text.set_alpha(150)
        self.screen.blit(owned_text, (info_x - 36, info_y + 16))
        # Position the text next to the button
        self.screen.blit(text, (info_x - 180, info_y + 10))

        # Draw the image
        self.screen.blit(image, (info_x - 230, info_y + 12))