class Animation:
    def __init__(self, pygame, game):
        self.pygame = pygame
        self.game = game
        self.button_scale = 1.0  # The scale of the button

    def update_button_scale(self):
        # Update the button scale based on mouse button state
        mouse_state = self.pygame.mouse.get_pressed()
        mouse_pos = self.pygame.mouse.get_pos()
        if mouse_state[0] and self.game.is_point_in_circle(mouse_pos):  # Check if left mouse button is down
            print('reach2')
            self.button_scale -= 0.02  # Adjust the zoom-out speed
        else:
            self.button_scale += 0.02  # Adjust the zoom-in speed

        # Clamp the button scale to avoid negative or too large values
        self.button_scale = max(0.8, min(1.0, self.button_scale))
