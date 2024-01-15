import sys
import warnings
import pygame
from upgrades import Upgrades
from game_state_management import GameStateManager
from assets import AssetsLoader
from buttons import ButtonCreator
from hints import Hints
from animations import Animation
from images import ImageLoader
from sounds import SoundLoader

# Suppress lib png warning
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP: known incorrect sRGB profile.*")

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

        self.bps_timer = pygame.time.get_ticks()
        self.autosave_timer = pygame.time.get_ticks()
        self.saving_in_progress = False
        self.loading_in_progress = False

        self.width, self.height = 1280, 720  # TODO 900, 600 - Add Skills
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
        # self.upgrades_background = pygame.Rect(1280 - (1280 / 3), 0, 800 / 3 + 20, 620) TODO WHAT THE FUCK IS THIS

    def draw_mouse_pointer(self):
        # Get the current mouse position and draw it
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.blit(images.mouse_pointer, (mouse_x + -12, mouse_y - 18))

    def draw(self):
        # Set the initial size and position of the clicker image
        circle_radius = 226  #226
        circle_x = 250  #250
        circle_y = 250  #250

        # Create a circular surface (same size as the circle's bounding box)
        self.circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.circle_surface, (0, 0, 0, 0), (circle_radius, circle_radius), circle_radius)
        self.circle_rect = self.circle_surface.get_rect(center=(circle_x, circle_y))

        # Load and scale your button image to fit inside the circle
        button_image = pygame.transform.scale(images.click_button_image, (circle_radius * 1, circle_radius * 1))

        # Draw the button image onto the circle_surface
        self.circle_surface.blit(button_image, (420, 180))

        # self.animations.update_button_scale()
        #
        # # Calculate the scaled dimensions
        # scaled_width = int(circle_radius * 2 * self.animations.button_scale)
        # scaled_height = int(circle_radius * 2 * self.animations.button_scale)
        #
        # # Scale the circular surface
        # scaled_circle_surface = pygame.transform.scale(self.circle_surface, (scaled_width, scaled_height))
        #
        # # Calculate the new top-left position for the scaled surface
        # scaled_x = circle_x - scaled_width // 2
        # scaled_y = circle_y - scaled_height // 2
        #
        # # Draw the scaled circular surface
        # self.screen.blit(scaled_circle_surface, (scaled_x, scaled_y))
        self.screen.blit(images.click_button_image, (420, 180))
        # Background Upgrades
        self.screen.blit(images.separator_image, ((1280 - (1280 / 3) - 55), 0))  # -25

        # Create skill buttons using a loop
        for button_data in self.button_creator.skill_buttons_data:
            owned = button_data["owned"]
            hover_text_to_use = button_data["hover_text"]
            image_to_use = button_data["skill_image"]

            # Adjust hover_text_to_use and image_to_use based on owned value
            if owned >= 200:
                hover_text_to_use = 'not implemented(still x32)'  # TODO
                # image_to_use = some_heavenly_image
            elif owned >= 150:
                hover_text_to_use = 'Earnings x32'
                # image_to_use = some_legendary_image
            elif owned >= 100:
                hover_text_to_use = 'Earnings x16'
                # image_to_use = some_epic_image
            elif owned >= 50:
                hover_text_to_use = 'Earnings x8'
                # image_to_use = some_rare_image
            elif owned >= 25:
                hover_text_to_use = 'Earnings x4'
                # upgrades.upgrade_0_increase *= 4
                # image_to_use = some_uncommon_image
            elif owned >= 10:
                hover_text_to_use = 'Earnings x2'
                # upgrades.upgrade_0_increase.value *= 4
                # image_to_use = some_common_image
            else:
                image_to_use = button_data["fallback_image"]

            self.button_creator.create_skill_button(image_to_use, button_data["rect"], hover_text_to_use,
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
        text_balance = assets.font_32.render(f"{upgrades.balance.formatted()}",
                                             True, (255, 255, 255))
        text_balance2 = assets.font_26.render(f"Bps: {upgrades.balance_per_second.formatted()}",
                                              True, (255, 255, 255))
        # calculate how many clicks are left until the next bacon per click upgrade
        clicks_left = -1 * ((upgrades.total_clicks.value % 50) - 50)
        text_balance3 = assets.font_26.render(f"+1/Click in {clicks_left} clicks", True, (255, 255, 255))
        text_balance4 = assets.font_26.render(f"Total clicks: {upgrades.total_clicks.value}", True, (255, 255, 255))
        self.screen.blit(images.balance_img, (450, 503))
        self.screen.blit(text_balance, (480, 500))
        self.screen.blit(text_balance2, (440, 525))
        self.screen.blit(text_balance3, (380, 550))
        self.screen.blit(text_balance4, (420, 575))

        # Display hints
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 680, 1280, 40))  # 101, 172, 224
        hints.update_hints(pygame)  # Get current hint
        text_hints = assets.font_20.render(f"Bacon says: {hints.current_hint}", True, (0, 0, 0))
        v_num = assets.font_20.render(f"v.0.1", True, (0, 0, 0))
        self.screen.blit(text_hints, (10, 690))
        self.screen.blit(v_num, (1220, 690))

        # Display Logo and upgrades Title
        self.screen.blit(images.logo_image, (380, 20))
        self.screen.blit(images.upgrades_image, (1050, 18))

        # Draw the custom mouse pointer
        self.draw_mouse_pointer()

        # Draw the click rate text at the end
        for click_event in self.click_events[:]:
            # Extract initial_click_rate_for_event from the tuple
            mouse_x, mouse_y, click_time, initial_click_rate_for_event = click_event

            if pygame.time.get_ticks() - click_time < self.click_rate_text_duration:
                current_click_rate = upgrades.click_rate.value
                click_rate_text = assets.font_26.render(f"+{current_click_rate}", True, 'white')
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

    def autosave_every_30s(self):
        current_time2 = pygame.time.get_ticks()
        elapsed_time2 = current_time2 - self.autosave_timer
        if elapsed_time2 >= 30000:
            game_state_manager.save_game_state()
            self.autosave_timer = current_time2

    def click(self):
        sounds.sound_click.play()
        upgrades.total_clicks.value += 1
        if upgrades.total_clicks.value % 50 == 0:
            upgrades.click_rate.value = int(upgrades.total_clicks.value / 50) * upgrades.click_multiplier.value
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Store the initial click rate value for this click event
        initial_click_rate_for_event = upgrades.click_rate

        self.click_events.append((mouse_x, mouse_y, pygame.time.get_ticks(), initial_click_rate_for_event))

        if self.circle_rect.collidepoint(mouse_x, mouse_y):
            # Increase the click rate based on upgrades, etc.
            # self.animations.update_button_scale()
            upgrades.balance += upgrades.click_rate

        return initial_click_rate_for_event  # Return the initial click rate for this click event

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
                    # game_state_manager.save_game_state()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.is_point_in_circle(event.pos):
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
            # self.autosave_every_30s()
            self.draw()
            # keys = pygame.key.get_pressed()

            clock.tick(120)


if __name__ == "__main__":
    game = Game()
    # Load initial game state or create a new one
    # game_state_manager.load_or_create_game_state(upgrades)
    # Turned off for testing purposes
    game.run()
