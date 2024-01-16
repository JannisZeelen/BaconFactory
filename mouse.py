class Mouse:
    def __init__(self):
        pass

    def draw_mouse_pointer(self, pygame, images, screen):
        # Get the current mouse position and draw it
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(images.mouse_pointer, (mouse_x + -12, mouse_y - 18))

    def click(self, game, sounds, upgrades, pygame):
        sounds.sound_click.play()
        upgrades.total_clicks.value += 1
        if upgrades.total_clicks.value % 50 == 0:
            upgrades.click_rate.value = int(upgrades.total_clicks.value / 50) * upgrades.click_multiplier.value
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Store the initial click rate value for this click event
        initial_click_rate_for_event = upgrades.click_rate

        game.click_events.append((mouse_x, mouse_y, pygame.time.get_ticks(), initial_click_rate_for_event))

        if game.circle_rect.collidepoint(mouse_x, mouse_y):
            # Increase the click rate based on upgrades, etc.
            upgrades.balance += upgrades.click_rate

        return initial_click_rate_for_event  # Return the initial click rate for this click event
