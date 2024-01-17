import sys
import os
import warnings
import pygame
import pygame_menu
import time

import mouse
import settings
from upgrades import Upgrades
from game_state_management import GameStateManager
from assets import AssetsLoader
from buttons import ButtonCreator
from hints import Hints
from animations import Animation
from images import ImageLoader
from sounds import SoundLoader
from mouse import Mouse
from settings import create_settings_menu
from format_numbers import FormattedNumber
from progressbar import draw_progress_bar, draw_upgrade_progress_bar

# Constants
WINDOW_X_POSITION = 1270
WINDOW_Y_POSITION = 400
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Suppress lib png warning
warnings.filterwarnings("ignore", category=UserWarning, module="PIL", message=".*known incorrect sRGB profile.*")

# Set the window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WINDOW_X_POSITION, WINDOW_Y_POSITION)


def initialize_game():
    """Initializes the game and returns the game components."""
    pygame.init()
    pygame.mixer.init()
    # Set the window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{WINDOW_X_POSITION},{WINDOW_Y_POSITION}"
    # Set the window title
    pygame.display.set_caption("Bacon Factory")

    assets_instance = AssetsLoader(pygame)
    upgrades_instance = Upgrades(pygame)
    game_state_manager_instance = GameStateManager(upgrades_instance)
    images_instance = ImageLoader(pygame)
    mouse_instance = Mouse()
    sounds_instance = SoundLoader(pygame)
    hints_instance = Hints(pygame)

    return (assets_instance, upgrades_instance, game_state_manager_instance,
            images_instance, sounds_instance, hints_instance, mouse_instance)


class Game:
    def __init__(self):
        self.settings_menu = None
        self.last_active_time = None
        self.circle_rect = None
        self.circle_surface = None
        self.animations = Animation(pygame, self)
        self.click_events = []  # List to store click events (position, time)
        self.click_rate_text_duration = 1000

        self.bps_timer = pygame.time.get_ticks()
        self.autosave_timer = [pygame.time.get_ticks()]
        self.saving_in_progress = False
        self.loading_in_progress = False
        self.progress = 0.0

        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.button_creator = ButtonCreator(pygame, assets, self.screen, upgrades, images)

        # Hide the default system cursor
        pygame.mouse.set_visible(False)

    def draw(self):
        # Background
        self.screen.blit(images.background, (0, 0))

        # Create the settings menu
        set_volume, save_game, load_game, change_language = (None, None, None, None)
        self.settings_menu = create_settings_menu(self.screen, set_volume, save_game, load_game, change_language)

        # Clicker
        # Initial size and position of the clicker image
        circle_radius = 200  # 226
        circle_x = (WINDOW_WIDTH / 2)  #- WINDOW_WIDTH / 3 / 2
        circle_y = WINDOW_HEIGHT / 3 - 20

        self.circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.circle_surface, (0, 0, 0, 0), (circle_radius, circle_radius), circle_radius)
        self.circle_rect = self.circle_surface.get_rect(center=(circle_x, circle_y))

        # Load and scale your button image to fit inside the circle
        button_image = pygame.transform.scale(images.click_button_image, (221, 350))

        # Draw the button image onto the circle_surface
        self.circle_surface.blit(button_image, (90, 25))
        self.animations.update_button_scale()

        # Calculate the scaled dimensions
        scaled_width = int(circle_radius * 2 * self.animations.button_scale)
        scaled_height = int(circle_radius * 2 * self.animations.button_scale)

        # Scale the circular surface
        scaled_circle_surface = pygame.transform.scale(self.circle_surface, (scaled_width, scaled_height))

        # Calculate the new top-left position for the scaled surface
        scaled_x = circle_x - scaled_width // 2
        scaled_y = circle_y - scaled_height // 2

        # Draw the scaled circular surface
        self.screen.blit(scaled_circle_surface, (scaled_x, scaled_y))

        # Update the 1s progress bar
        draw_progress_bar(self.screen, 20, 80, 200, 4, self.progress, (assets.white))
        # Draw progress bar for the first upgrade


        # Upgrades
        # Upgrades Background / Separator
        # self.screen.blit(images.separator_image, ((WINDOW_WIDTH - (WINDOW_WIDTH / 3 + 55)), 0))

        self.button_creator.update_button_conditions(upgrades)

        # Create upgrade buttons using a loop
        for button_data in self.button_creator.upgrade_buttons_data:
            if button_data["condition"]:
                self.button_creator.create_button(button_data["rect"], (209, 50, 36),
                                                  button_data["label"], button_data["cost"],
                                                  button_data["increase"], button_data["owned"],
                                                  button_data["image"], pygame, upgrades, images)

        upgrade_targets = [10, 25, 50, 100, 150, 200, 300]  # Define the targets for this upgrade
        draw_upgrade_progress_bar(self.screen, upgrades.upgrade_1_owned.value, upgrade_targets, 32, 542, 280, 10,
                                  (255, 255, 255), (0, 255, 0))
        # Balance Texts
        text_balance = assets.font_32.render(f"{upgrades.balance.formatted()}",
                                             True, assets.black)
        text_bps = assets.font_26.render(f"Bps: {upgrades.balance_per_second.formatted()}",
                                         True, assets.black)
        # calculate how many clicks are left until the next bacon per click upgrade
        clicks_left = -1 * ((upgrades.total_clicks.value % 50) - 50)
        text_progress = assets.font_26.render(f"+1/Click in {clicks_left} clicks", True, assets.white)
        text_total_clicks = assets.font_26.render(f"Total clicks: {upgrades.total_clicks.value}", True, assets.white)
        # self.screen.blit(images.balance_img, (450, 503))
        self.screen.blit(text_balance, (50, 25))
        # self.screen.blit(text_bps, (440, 525))
        self.screen.blit(text_bps, (50, 55))
        # self.screen.blit(text_progress, (380, 550))
        # self.screen.blit(text_total_clicks, (420, 575))

        # Hints
        pygame.draw.rect(self.screen, (105, 38, 49), (0, 680, 1280, 40))  # 101, 172, 224
        pygame.draw.rect(self.screen, (105, 38, 49), (0, 680, 1280, 20))  # 101, 172, 224
        hints.update_hints(pygame)  # Get current hint
        text_hints = assets.font_20.render(f"Bacon says: {hints.current_hint}", True, assets.white)
        v_num = assets.font_20.render(f"v.0.1", True, assets.white)
        self.screen.blit(text_hints, (10, 690))
        self.screen.blit(v_num, (1220, 690))
        # print("Pygame version:", pygame.__version__)

        # Display Logo and upgrades Title
        # self.screen.blit(images.logo_image, (380, 20))
        # self.screen.blit(images.upgrades_image, (1050, 18))

        # Draw the custom mouse pointer
        mouse.draw_mouse_pointer(pygame, images, self.screen)

        # Draw the click rate text at the end
        for click_event in self.click_events[:]:
            # Extract initial_click_rate_for_event from the tuple
            mouse_x, mouse_y, click_time, initial_click_rate_for_event = click_event

            if pygame.time.get_ticks() - click_time < self.click_rate_text_duration:
                current_click_rate = upgrades.click_rate.value
                click_rate_text = assets.font_26.render(f"+{upgrades.click_rate.formatted()}", True, 'white')
                self.screen.blit(images.balance_img, (mouse_x + 20, mouse_y - 10))
                self.screen.blit(click_rate_text, (mouse_x + 45, mouse_y - 10))
            else:
                self.click_events.remove(click_event)

        pygame.display.flip()

    def update_balance_per_second(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.bps_timer

        if elapsed_time >= 1000:
            upgrades.balance += upgrades.balance_per_second
            self.bps_timer = current_time

    def is_point_in_circle(self, point):
        if self.circle_rect.collidepoint(point):
            # Transform point to circle_surface's coordinates
            local_point = (point[0] - self.circle_rect.left, point[1] - self.circle_rect.top)
            # Check if the clicked pixel's alpha value is not transparent
            return self.circle_surface.get_at(local_point)[3] != 0
        return False

    def run(self):
        clock = pygame.time.Clock()
        while True:
            # Update progress
            self.progress += 0.01
            if self.progress > 1.0:
                self.progress = 0.0
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # game_state_manager.save_game_state()

                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.is_point_in_circle(event.pos):
                        mouse.click(game, sounds, upgrades, pygame)
                    elif upgrades.buy_upgrade_0_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade(1)
                        print("Debug: self.settings_menu is", self.settings_menu)
                        if self.settings_menu is not None:
                            self.settings_menu.mainloop(self.screen)
                    elif upgrades.buy_upgrade_1_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade(2)
                    elif upgrades.buy_upgrade_2_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade(3)
                    elif upgrades.buy_upgrade_3_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade(4)
                    elif upgrades.buy_upgrade_4_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade(5)
                    elif upgrades.buy_upgrade_5_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade(6)
                    elif upgrades.buy_upgrade_6_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade(7)
                    elif upgrades.buy_upgrade_7_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade(8)

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
            game_state_manager.autosave_every_30s(pygame, self.autosave_timer)
            self.draw()
            # keys = pygame.key.get_pressed()

            clock.tick(120)


if __name__ == "__main__":
    assets, upgrades, game_state_manager, images, sounds, hints, mouse = initialize_game()
    game = Game()

    # Load initial game state or create a new one
    game_state_manager.load_or_create_game_state(upgrades)  # Turned off for testing purposes
    # upgrades.recalculate_upgrade_costs()

    game.run()
