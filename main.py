import sys
import pygame
from upgrades import Upgrades
from game_state_management import GameStateManager
from draw import Draw
from assets import AssetsLoader
from buttons import ButtonCreator
from hints import Hints
from animations import Animation
from images import ImageLoader
from sounds import SoundLoader
from format_numbers import FormattedNumber

pygame.init()
pygame.mixer.init()

assets = AssetsLoader(pygame)
upgrades = Upgrades(pygame)
game_state_manager = GameStateManager(upgrades)
images = ImageLoader(pygame)
sounds = SoundLoader(pygame)
hints = Hints(pygame)


class Game:
    def __init__(self):
        self.animations = Animation(pygame, self)

        self.click_events = []  # List to store click events (position, time)
        self.click_rate_text_duration = 1000

        self.timer = pygame.time.get_ticks()
        self.saving_in_progress = False
        self.loading_in_progress = False

        self.width, self.height = 800, 600  # TODO 900, 600 - Add Skills
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.button_creator = ButtonCreator(pygame, assets, self.screen, upgrades, images)
        pygame.display.set_caption("Bacon Factory")
        # Load images

        # Background
        images.background.set_colorkey((255, 255, 255))
        images.overlap.set_colorkey((255, 255, 255))
        self.b_pos = 0
        self.o_pos = 600
        self.speed = .2

        # Hide the default system cursor
        pygame.mouse.set_visible(False)

        # Background
        self.upgrades_background = pygame.Rect(790 - (800 / 3), 0, 800 / 3 + 20, 620)

    def draw_mouse_pointer(self):
        # Get the current mouse position and draw it
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.blit(images.mouse_pointer, (mouse_x + -12, mouse_y - 18))

    def draw(self):

        # Set the initial size and position of the clicker image
        self.click_button_rect = images.click_button_image.get_rect()
        self.click_button_rect.topleft = (210, 180)

        # Scale the button image once
        images.button_image = pygame.transform.scale(images.click_button_image, (
            int(self.click_button_rect.width * self.animations.button_scale),
            int(self.click_button_rect.height * self.animations.button_scale)))

        # Update the button scale based on interactions
        self.animations.update_button_scale()

        # Background Upgrades
        self.screen.blit(images.separator_image, ((800 - (800 / 3) - 55), 0))  # -25

        # Draw button with scaled size
        scaled_button_image = pygame.transform.scale(images.button_image, (
            int(self.click_button_rect.width * self.animations.button_scale),
            int(self.click_button_rect.height * self.animations.button_scale)))
        self.screen.blit(scaled_button_image, self.click_button_rect)

        # Create skill buttons using a loop
        for button_data in self.button_creator.skill_buttons_data: # TODO Skill Buttons if 5 common rarity, 10 uncommon, 15 rare, 20 epic, 25 legendary, 30 heavenly, each other 5 be +1
            image_to_use = button_data["skill_image"] if button_data["owned"] >= 5 else button_data["fallback_image"]
            self.button_creator.create_skill_button(image_to_use, button_data["rect"], button_data["hover_text"],
                                                    (0, 0, 0), pygame)
        if upgrades.upgrade_0_owned.value >= 1:
            self.button_creator.create_button(upgrades.buy_upgrade_1_button_rect, (209, 50, 36), "Upgrade 1",
                                              upgrades.upgrade_1_cost, upgrades.upgrade_1_increase,
                                              upgrades.upgrade_1_owned, images.upgrade_1_upgrade, pygame, upgrades,
                                              images)

        def update_button_conditions(self, upgrades):
            for i, button_data in enumerate(self.button_creator.upgrade_buttons_data):
                if i == 0:
                    button_data["condition"] = True
                else:
                    prev_upgrade_attr = f"upgrade_{i - 1}_owned"
                    button_data["condition"] = getattr(upgrades, prev_upgrade_attr).value >= 1

        update_button_conditions(self, upgrades)

        # Create upgrade buttons using a loop
        for button_data in self.button_creator.upgrade_buttons_data:
            if button_data["condition"]:
                self.button_creator.create_button(button_data["rect"], (209, 50, 36),
                                                  button_data["label"], button_data["cost"],
                                                  button_data["increase"], button_data["owned"],
                                                  button_data["image"], pygame, upgrades, images)

        # Balance text
        text_balance = assets.font_32.render(f"Bacon: {upgrades.balance.formatted()}",
                                             True, (255, 255, 255))
        text_balance2 = assets.font_26.render(f"per second: {upgrades.balance_per_second.formatted()}",
                                              True, (255, 255, 255))
        self.screen.blit(text_balance, (190, 440))
        self.screen.blit(text_balance2, (200, 465))

        # Display hints
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 560, 800, 40))  # 101, 172, 224
        hints.update_hints(pygame)  # Get current hint
        text_hints = assets.font_20.render(f"Bacon says: {hints.current_hint}", True, (0, 0, 0))
        self.screen.blit(text_hints, (10, 570))

        # Display Logo and upgrades Title
        self.screen.blit(images.logo_image, (180, 20))
        self.screen.blit(images.upgrades_image, (590, 18))

        # Draw the custom mouse pointer
        self.draw_mouse_pointer()

        # Draw the click rate text at the end
        for click_event in self.click_events[:]:
            # Extract initial_click_rate_for_event from the tuple
            mouse_x, mouse_y, click_time, initial_click_rate_for_event = click_event

            if pygame.time.get_ticks() - click_time < self.click_rate_text_duration:
                current_click_rate = upgrades.click_rate.value
                click_rate_text = assets.font_18.render(f"+{current_click_rate}", True, 'white')
                self.screen.blit(click_rate_text, (mouse_x + 15, mouse_y - 10))
            else:
                self.click_events.remove(click_event)

        pygame.display.flip()

    def update_balance_per_second(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.timer

        if elapsed_time >= 1000:
            upgrades.balance += upgrades.balance_per_second
            self.timer = current_time

    def click(self):
        sounds.sound_click.play()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Store the initial click rate value for this click event
        initial_click_rate_for_event = upgrades.click_rate

        self.click_events.append((mouse_x, mouse_y, pygame.time.get_ticks(), initial_click_rate_for_event))

        if self.click_button_rect.collidepoint(mouse_x, mouse_y):
            # Increase the click rate based on upgrades, etc.
            upgrades.balance += upgrades.click_rate

        return initial_click_rate_for_event  # Return the initial click rate for this click event

    def run(self):
        clock = pygame.time.Clock()

        while True:
            # Background
            if self.b_pos <= -self.height:
                self.b_pos = self.height
            if self.o_pos <= -self.height:
                self.o_pos = self.height

            self.b_pos -= self.speed
            self.o_pos -= self.speed
            self.screen.blit(images.background, (0, self.b_pos))
            self.screen.blit(images.overlap, (0, self.o_pos))

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.click_button_rect.collidepoint(event.pos):
                        if event.button == 1:
                            self.click()
                    elif upgrades.buy_upgrade_0_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_0()
                    elif upgrades.buy_upgrade_1_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_1()
                    elif upgrades.buy_upgrade_2_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_2()
                    elif upgrades.buy_upgrade_3_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_3()
                    elif upgrades.buy_upgrade_4_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_4()
                    elif upgrades.buy_upgrade_5_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_5()
                    elif upgrades.buy_upgrade_6_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_6()
                    elif upgrades.buy_upgrade_7_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_7()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_s and not self.saving_in_progress:
                    self.saving_in_progress = True  # Set the flag
                    game_state_manager.save_game_state()

                # Check if the 'S' key is released
                if event.type == pygame.KEYUP and event.key == pygame.K_s:
                    self.saving_in_progress = False  # Reset the flag

                if event.type == pygame.KEYDOWN and event.key == pygame.K_l and not self.saving_in_progress:
                    self.loading_in_progress = True  # Set the flag
                    game_state_manager.load_game_state()
                    # upgrades.recalculate_upgrade_costs()

                # Check if the 'S' key is released
                if event.type == pygame.KEYUP and event.key == pygame.K_l:
                    self.loading_in_progress = False  # Reset the flag

            self.update_balance_per_second()
            self.draw()
            # keys = pygame.key.get_pressed()

            clock.tick(120)


if __name__ == "__main__":
    game = Game()
    # Load initial game state or create a new one
    game_state_manager.load_or_create_game_state(upgrades)
    # Turned off for testing purposes
    game.run()

# TODO Upgrades
# TODO Abilities to buy that will increase clickrate Events: all 120 seconds make button appear to give click rate boost
# TODO Maximum of 10 per Item, step 5 and 10 give bonuses
# TODO Arrow that points to bacon and is moving
# TODO Make bacon zoom to its center when clicked
# TODO Textbox für prints
# TODO Sound effects
# TODO Score = mini bacon
# TODO Click auf Bacon = Clickrate als hover
# TODO Koordinatenangaben mit rect.right / rect.left etc
# DONE Tips on button in  list of strings, change all 10-15 seconds

""" Erik Feedback
- Feedback bei Upgrade / animation
- mehr Upgrades
- Bacon Bild verändern je nachdem wie weit man ist
"""
