import sys
import json
import pygame
from upgrades import Upgrades
from game_state_management import GameStateManager
from draw import Draw
from assets import AssetsLoader
from buttons import ButtonCreator
from hints import Hints

upgrades = Upgrades(pygame)
game_state_manager = GameStateManager(upgrades)


# draw = Draw


class Game:
    def __init__(self):
        pygame.init()
        self.asset_loader = AssetsLoader(pygame)
        self.hints = Hints(pygame)
        pygame.mixer.init()
        # upgrades.load_or_create_game_state()

        self.click_events = []  # List to store click events (position, time)
        self.click_rate_text_duration = 1000  # milliseconds

        self.timer = pygame.time.get_ticks()
        self.saving_in_progress = False
        self.loading_in_progress = False



        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.button_creator = ButtonCreator(pygame, self.asset_loader, self.screen)
        pygame.display.set_caption("Bacon Factory")

        # Background
        self.background = pygame.image.load("assets/img/background.png")
        self.background.set_colorkey((255, 255, 255))
        self.overlap = pygame.image.load("assets/img/background.png")
        self.overlap.set_colorkey((255, 255, 255))
        self.b_pos = 0
        self.o_pos = 600
        self.speed = .2

        # Load button image and resize it
        self.click_button_image = pygame.image.load("assets/img/baconPog.png")
        button_width, button_height = (self.click_button_image.get_width() // 2,
                                       self.click_button_image.get_height() // 2)
        # Set the initial size and position of the clicker image
        self.button_scale = 0.8
        self.button_image = pygame.transform.scale(self.click_button_image, (
            int(button_width * self.button_scale), int(button_height * self.button_scale)))

        self.button_rect = self.button_image.get_rect()
        self.button_rect.topleft = (210, 180)

        # Load images
        # Logo, Upgrades Title, Separator
        self.logo_image = pygame.image.load("assets/img/logo.png")
        self.logo_image = pygame.transform.scale(self.logo_image, (170 * 1.5, 64 * 1.5))

        self.upgrades_image = pygame.image.load("assets/img/upgrades.png")
        self.separator_image = pygame.image.load("assets/img/separator.png")

        # Load the custom mouse pointer image
        # Hide the default system cursor
        pygame.mouse.set_visible(False)
        self.mouse_pointer_image = pygame.image.load("assets/img/frying_pan.png")
        self.mouse_pointer = pygame.transform.scale(self.mouse_pointer_image, (40, 40))

        # Background
        self.upgrades_background = pygame.Rect(790 - (800 / 3), 0, 800 / 3 + 20, 620)

        # Load sounds
        self.sound_click = pygame.mixer.Sound('assets/sounds/click.wav')
        self.sound_click.set_volume(0.3)

    def draw_mouse_pointer(self):
        # Get the current mouse position and draw it
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.blit(self.mouse_pointer, (mouse_x + -12, mouse_y - 18))

    def draw(self):
        self.update_button_scale()  # Call the update_button_scale method

        # Background Upgrades
        self.screen.blit(self.separator_image, ((800 - (800 / 3) - 55), 0))  # -25

        # Draw button with scaled size
        scaled_button_image = pygame.transform.scale(self.button_image, (
            int(self.button_rect.width * self.button_scale), int(self.button_rect.height * self.button_scale)))
        self.screen.blit(scaled_button_image, self.button_rect)

        # Skill Buttons
        if upgrades.frying_pan_owned >= 5:
            self.button_creator.create_skill_button(upgrades.frying_pan_skill, upgrades.skill_rect, '', (0, 0, 0),
                                                    pygame)
        else:
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect, '', (0, 0, 0),
                                                    pygame)

        if upgrades.pig_owned >= 5:
            self.button_creator.create_skill_button(upgrades.pig_skill, upgrades.skill_rect2, '1', (0, 0, 0), pygame)
        else:
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect2, '', (0, 0, 0),
                                                    pygame)

        if upgrades.upgrade_2_owned >= 5:
            self.button_creator.create_skill_button(upgrades.upgrade_2_skill, upgrades.skill_rect3, '2', (0, 0, 0),
                                                    pygame)
        else:
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect3, '', (0, 0, 0),
                                                    pygame)

        if upgrades.upgrade_3_owned >= 5:
            self.button_creator.create_skill_button(upgrades.upgrade_3_skill, upgrades.skill_rect4, '3', (0, 0, 0),
                                                    pygame)
        else:
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect4, '', (0, 0, 0),
                                                    pygame)

        if upgrades.upgrade_4_owned >= 5:
            self.button_creator.create_skill_button(upgrades.upgrade_4_skill, upgrades.skill_rect5, '4', (0, 0, 0),
                                                    pygame)
        else:
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect5, '', (0, 0, 0),
                                                    pygame)

        if upgrades.upgrade_5_owned >= 5:
            self.button_creator.create_skill_button(upgrades.upgrade_4_skill, upgrades.skill_rect6, '5', (0, 0, 0),
                                                    pygame)
        else:
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect6, '', (0, 0, 0),
                                                    pygame)

        if upgrades.upgrade_6_owned >= 5:
            self.button_creator.create_skill_button(upgrades.upgrade_4_skill, upgrades.skill_rect7, '6', (0, 0, 0),
                                                    pygame)
        else:
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect7, '', (0, 0, 0),
                                                    pygame)

        if upgrades.upgrade_7_owned >= 5:
            self.button_creator.create_skill_button(upgrades.upgrade_4_skill, upgrades.skill_rect8, '7', (0, 0, 0),
                                                    pygame)
        else:
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect8, '', (0, 0, 0),
                                                    pygame)

        if upgrades.balance >= 1000000:  # END BUTTON TODO
            self.button_creator.create_skill_button(upgrades.question_mark_skill, upgrades.skill_rect9, '', (0, 0, 0),
                                                    pygame)

        # Erstellen der Upgrade Buttons

        self.button_creator.create_button(upgrades.buy_pig_button_rect, (209, 50, 36),
                                          "Pig", upgrades.pig_cost, upgrades.pig_increase, upgrades.pig_owned,
                                          upgrades.pig_upgrade, pygame, upgrades)
        self.button_creator.create_button(upgrades.buy_frying_pan_button_rect, (209, 50, 36),
                                          "Frying Pan", upgrades.frying_pan_cost,
                                          upgrades.frying_pan_increase, upgrades.frying_pan_owned, upgrades.frying_pan, pygame,
                                          upgrades)
        if upgrades.pig_owned >= 2:
            self.button_creator.create_button(upgrades.buy_upgrade_2_button_rect, (209, 50, 36),
                                              "Upgrade 2", upgrades.upgrade_2_cost, upgrades.upgrade_2_increase,
                                              upgrades.upgrade_2_owned, upgrades.upgrade_2_upgrade, pygame, upgrades)
        if upgrades.upgrade_2_owned >= 2:
            self.button_creator.create_button(upgrades.buy_upgrade_3_button_rect, (209, 50, 36),
                                              "Upgrade 3", upgrades.upgrade_3_cost,
                                              upgrades.upgrade_3_increase, upgrades.upgrade_3_owned, upgrades.upgrade_3_upgrade, pygame,
                                              upgrades)
        if upgrades.upgrade_3_owned >= 2:
            self.button_creator.create_button(upgrades.buy_upgrade_4_button_rect, (209, 50, 36),
                                              "Upgrade 4", upgrades.upgrade_4_cost,
                                              upgrades.upgrade_4_increase,
                                              upgrades.upgrade_4_owned, upgrades.upgrade_4_upgrade, pygame, upgrades)
        if upgrades.upgrade_4_owned >= 2:
            self.button_creator.create_button(upgrades.buy_upgrade_5_button_rect, (209, 50, 36),
                                              "Upgrade 5", upgrades.upgrade_5_cost,
                                              upgrades.upgrade_5_increase,
                                              upgrades.upgrade_5_owned, upgrades.upgrade_4_upgrade, pygame, upgrades)
        if upgrades.upgrade_5_owned >= 2:
            self.button_creator.create_button(upgrades.buy_upgrade_6_button_rect, (209, 50, 36),
                                              "Upgrade 6", upgrades.upgrade_6_cost,
                                              upgrades.upgrade_6_increase,
                                              upgrades.upgrade_6_owned, upgrades.upgrade_4_upgrade, pygame, upgrades)
        if upgrades.upgrade_6_owned >= 2:
            self.button_creator.create_button(upgrades.buy_upgrade_7_button_rect, (209, 50, 36),
                                              "Upgrade 7", upgrades.upgrade_7_cost,
                                              upgrades.upgrade_7_increase,
                                              upgrades.upgrade_7_owned, upgrades.upgrade_4_upgrade, pygame, upgrades)

        # Balance text
        text_balance = self.asset_loader.font_32.render(f"Bacon: {upgrades.balance:.2f}",
                                                        True, (255, 255, 255))
        text_balance2 = self.asset_loader.font_26.render(f"per second: {upgrades.balance_per_second:.0f}",
                                                         True, (255, 255, 255))
        self.screen.blit(text_balance, (190, 440))
        self.screen.blit(text_balance2, (200, 465))

        # Display hints
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 560, 800, 40))  # 101, 172, 224
        text_hints = self.asset_loader.font_20.render(f"Bacon says: {self.hints.current_hint}", True, (0, 0, 0))
        self.hints.update_hints(pygame)  # TODO Find a way to make the hint update function to work
        self.screen.blit(text_hints, (10, 570))

        # Display Logo and upgrades Title
        self.screen.blit(self.logo_image, (180, 20))
        self.screen.blit(self.upgrades_image, (590, 18))

        # Mouse pointer
        # Draw the custom mouse pointer
        self.draw_mouse_pointer()

        # Draw the click rate text at the end
        for click_event in self.click_events[:]:
            mouse_x, mouse_y, click_time, initial_click_rate_for_event = click_event  # Extract initial_click_rate_for_event from the tuple

            if pygame.time.get_ticks() - click_time < self.click_rate_text_duration:
                current_click_rate = str(initial_click_rate_for_event)
                click_rate_text = self.asset_loader.font_18.render(f"+{current_click_rate}", True, 'white')
                self.screen.blit(click_rate_text, (mouse_x + 15, mouse_y - 10))
            else:
                self.click_events.remove(click_event)

        pygame.display.flip()

    def update_balance_per_second(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.timer

        if elapsed_time >= 1000:  # Update every 1000 milliseconds (1 second)
            upgrades.balance += upgrades.balance_per_second
            self.timer = current_time

    def update_button_scale(self):
        # Update the button scale based on mouse button state
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0] and self.button_rect.collidepoint(
                pygame.mouse.get_pos()):  # Check if left mouse button is down
            self.button_scale -= 0.02  # Adjust the zoom-out speed
        else:
            self.button_scale += 0.02  # Adjust the zoom-in speed

        # Clamp the button scale to avoid negative or too large values
        self.button_scale = max(0.8, min(1.0, self.button_scale))



    def click(self):
        self.sound_click.play()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Store the initial click rate value for this click event
        initial_click_rate_for_event = upgrades.click_rate

        self.click_events.append((mouse_x, mouse_y, pygame.time.get_ticks(), initial_click_rate_for_event))

        if self.button_rect.collidepoint(mouse_x, mouse_y):
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
            self.screen.blit(self.background, (0, self.b_pos))
            self.screen.blit(self.overlap, (0, self.o_pos))

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.button_rect.collidepoint(event.pos):
                        if event.button == 1:
                            self.click()
                    elif upgrades.buy_pig_button_rect.collidepoint(event.pos):
                        upgrades.buy_pig()
                    elif upgrades.buy_upgrade_2_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_2()
                    elif upgrades.buy_upgrade_3_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_3()
                    elif upgrades.buy_upgrade_4_button_rect.collidepoint(event.pos):
                        upgrades.buy_upgrade_4()
                    elif upgrades.buy_frying_pan_button_rect.collidepoint(event.pos):
                        upgrades.buy_frying_pan()
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
    # game_state_manager.load_or_create_game_state(upgrades)  # Turned off for testing purposes
    game.run()

# TODO Abilities to buy that will increase clickrate Events: all 120 seconds make button appear to give click rate boost
# TODO Maximum of 10 per Item, step 5 and 10 give bonuses
# TODO Background diagonal one color, bacon and stars repeatedly, moving
# TODO Arrow that points to bacon and is moving
# TODO Make bacon zoom to its center when clicked
# TODO make pointer to fitting icon
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
