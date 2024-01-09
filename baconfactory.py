import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import json
import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.pig_cost = 15
        self.pig_owned = 0
        self.bubbles_cost = 100
        self.bubbles_owned = 0
        self.frying_pan_cost = 350
        self.frying_pan_owned = False
        self.silverbacon_cost = 500
        self.silverbacon_owned = 0
        self.goldenbacon_cost = 2000
        self.goldenbacon_owned = 0

        self.balance = 100000000
        self.click_rate = 1
        self.balance_per_second = 0 + (self.pig_owned * 1) + (
                self.bubbles_owned * 5) + (self.silverbacon_owned * 20) + (
                                          self.goldenbacon_owned * 50)
        self.font_18 = pygame.font.Font('assets/fonts/DM_Mono.ttf', 18)
        self.font_20 = pygame.font.Font('assets/fonts/DM_Mono.ttf', 20)
        self.font_22 = pygame.font.Font('assets/fonts/DM_Mono.ttf', 22)
        self.font_24 = pygame.font.Font('assets/fonts/DM_Mono.ttf', 24)
        self.font_26 = pygame.font.Font('assets/fonts/DM_Mono.ttf', 26)
        self.font_28 = pygame.font.Font('assets/fonts/DM_Mono.ttf', 28)
        self.font_32 = pygame.font.Font('assets/fonts/DM_Mono.ttf', 32)
        self.timer = pygame.time.get_ticks()
        self.saving_in_progress = False
        self.loading_in_progress = False

        self.hints = ['Click the Bacon to progress!',
                      'Get passive income by buying new items!',
                      'Your clickrate increases when you buy 5 and 10 of one item!',
                      'Unlock new items by buying more items.',
                      'Rumors say there is an ending.']
        self.current_hint_index = 0
        self.hint_timer = pygame.time.get_ticks()
        self.hint_duration = 5000  # Display each hint for 5 seconds

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bacon Factory")
        self.screen.fill((103, 117, 108))  # 36, 148, 209
        # Background
        self.background = pygame.image.load("assets/img/background.png")
        self.background.set_colorkey((255, 255, 255))
        self.overlap = pygame.image.load("assets/img/background.png")
        self.overlap.set_colorkey((255, 255, 255))
        self.b_pos = 0
        self.o_pos = 600
        self.speed = .3

        # Load button image and resize it
        self.click_button_image = pygame.image.load("assets/img/baconPog.png")
        button_width, button_height = self.click_button_image.get_width() // 2, self.click_button_image.get_height() // 2

        # Set the initial size and position of the button image
        self.button_scale = 1.0
        self.button_image = pygame.transform.scale(self.click_button_image, (
            int(button_width * self.button_scale), int(button_height * self.button_scale)))

        self.button_rect = self.button_image.get_rect()
        self.button_rect.topleft = (10, 80)

        # Load images
        self.pig_image = pygame.image.load("assets/img/pig.png")
        self.pig_image = pygame.transform.scale(self.pig_image, (40, 40))

        self.bubbles_image = pygame.image.load("assets/img/bubbles.png")
        self.bubbles_image = pygame.transform.scale(self.bubbles_image, (40, 40))

        self.frying_pan_image = pygame.image.load("assets/img/frying_pan.png")
        self.frying_pan = pygame.transform.scale(self.frying_pan_image, (40, 40))
        # self.frying_pan.set_colorkey((145, 209, 222))

        self.frying_pan_skill_image = pygame.image.load("assets/img/frying_pan.png")
        self.frying_pan_skill = pygame.transform.scale(self.frying_pan_skill_image, (60, 60))
        # self.frying_pan_skill.set_colorkey((145, 209, 222))

        self.question_mark_skill_image = pygame.image.load("assets/img/question_mark.png")
        self.question_mark_skill = pygame.transform.scale(self.question_mark_skill_image, (60, 60))

        self.silverbacon_image = pygame.image.load("assets/img/silver.png")
        self.silverbacon_image = pygame.transform.scale(self.silverbacon_image, (40, 40))

        self.goldenbacon_image = pygame.image.load("assets/img/golden.png")
        self.goldenbacon_image = pygame.transform.scale(self.goldenbacon_image, (40, 40))

        # Buttongeometry / 60 px unterschied untereinander
        self.buy_pig_button_rect = pygame.Rect(self.width - 260, 50, 230, 50)
        self.buy_bubbles_button_rect = pygame.Rect(self.width - 260, 110, 230, 50)
        self.buy_frying_pan_button_rect = pygame.Rect(self.width - 260, 170, 230, 50)
        self.buy_silverbacon_button_rect = pygame.Rect(self.width - 260, 230, 230, 50)
        self.buy_goldenbacon_button_rect = pygame.Rect(self.width - 260, 290, 230, 50)

        # Skill Buttons
        self.skill_rect = pygame.Rect(self.width - 520, 110, 70, 70)
        self.skill_rect2 = pygame.Rect(self.width - 440, 110, 70, 70)
        self.skill_rect3 = pygame.Rect(self.width - 360, 110, 70, 70)
        self.skill_rect4 = pygame.Rect(self.width - 520, 190, 70, 70)
        self.skill_rect5 = pygame.Rect(self.width - 440, 190, 70, 70)
        self.skill_rect6 = pygame.Rect(self.width - 360, 190, 70, 70)

        # Load sounds
        self.sound_click = pygame.mixer.Sound('assets/sounds/click.wav')
        self.sound_click.set_volume(0.3)

    def save_game_state(self, filename='save/baconfactory_savestate.json'):
        # Convert the selected attributes to a dictionary
        save_data = self.to_dict()

        # Save the dictionary to a JSON file
        with open(filename, 'w') as file:
            json.dump(save_data, file)
            print('Game saved!')

    def load_game_state(self, filename='save/baconfactory_savestate.json'):
        # Load the dictionary from the JSON file
        with open(filename, 'r') as file:
            load_data = json.load(file)

        # Update the object's attributes from the loaded dictionary
        self.from_dict(load_data)
        print('Existing save loaded!')

    def to_dict(self):
        # Create a dictionary with only the attributes you want to save
        save_data = {
            'balance': self.balance,
            'balance_per_second': self.balance_per_second,
            'pig_cost': self.pig_cost,
            'pig_owned': self.pig_owned,
            'bubbles_cost': self.bubbles_cost,
            'bubbles_owned': self.bubbles_owned,
            'silverbacon_cost': self.silverbacon_cost,
            'silverbacon_owned': self.silverbacon_owned,
            'goldenbacon_cost': self.goldenbacon_cost,
            'goldenbacon_owned': self.goldenbacon_owned,
            # Add more attributes as needed
        }

        return save_data

    def from_dict(self, data):
        # Update the object's attributes from the provided dictionary
        self.balance = data['balance']
        self.balance_per_second = data['balance_per_second']
        self.pig_cost = data['pig_cost']
        self.pig_owned = data['pig_owned']
        self.bubbles_cost = data['bubbles_cost']
        self.bubbles_owned = data['bubbles_owned']
        self.silverbacon_cost = data['silverbacon_cost']
        self.silverbacon_owned = data['silverbacon_owned']
        self.goldenbacon_cost = data['goldenbacon_cost']
        self.goldenbacon_owned = data['goldenbacon_owned']
        # Update more attributes as needed

    def load_or_create_game_state(self):
        try:
            # Attempt to load the game state from the save file
            self.load_game_state()
        except FileNotFoundError:
            # If the save file is not found, continue with the initial state
            pass

    def create_skill_button(self, image, rect, hover_text):
        # Borders
        border_thickness = 2  # You can adjust this value according to your preference
        border_color = 'white'  # Choose the color of the border

        # coords
        info_x = rect.right + 10
        info_y = rect.top - 7

        # Draw Button
        button_height = 80
        button_width = 80
        pygame.draw.rect(self.screen, (0, 0, 0, 155), rect)  # 209, 50, 36
        self.screen.blit(image, (info_x - 78, info_y + 12))

        # Check if the mouse is hovering over the skill button
        if rect.collidepoint(pygame.mouse.get_pos()):
            hover_text_rendered = self.font_18.render(hover_text, True, (0, 0, 0))

            # Create a transparent surface for the hover text rectangle
            hover_rect_surface = pygame.Surface((hover_text_rendered.get_width(), hover_text_rendered.get_height()),
                                                pygame.SRCALPHA)
            hover_rect_surface.fill((0, 0, 0, 0))  # 128 is the alpha value for transparency

            # Draw the transparent hover text surface
            self.screen.blit(hover_rect_surface, (info_x, info_y))
            self.screen.blit(hover_text_rendered, (info_x, info_y))
        pygame.draw.rect(self.screen, border_color, rect, border_thickness)

    def create_button(self, rect, color, label, cost, bps_increase, owned, image, buy_function):
        # Borders
        border_thickness = 2  # You can adjust this value according to your preference
        border_color = (255, 255, 255)  # Choose the color of the border

        # coords
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
        text = self.font_22.render(label, True, (255, 255, 255))
        cost_text_color = (58, 189, 2) if self.balance >= cost else (184, 180, 180)  # Green if balance >= cost, el red
        if bps_increase == 'frying_pan':
            if not self.frying_pan_owned:
                cost_text = self.font_18.render(f"Cost: {cost} +5 click", True, cost_text_color)
                self.screen.blit(cost_text, (info_x - 180, info_y + 32))
                self.screen.blit(text, (info_x - 180, info_y + 10))
            else:
                self.screen.blit(text, (info_x - 180, info_y + 10))
                cost_text_color = 'black'
                cost_text = self.font_18.render(f"Bought!", True, cost_text_color)
                self.screen.blit(cost_text, (info_x - 180, info_y + 32))
        else:
            cost_text = self.font_18.render(f"Cost: {cost} +{bps_increase}/s", True, cost_text_color)
            self.screen.blit(cost_text, (info_x - 180, info_y + 32))
            owned_text = self.font_24.render(f"{owned}", True, (201, 201, 201))
            owned_text.set_alpha(150)
            self.screen.blit(owned_text, (info_x - 36, info_y + 16))
            # Position the text next to the button
            self.screen.blit(text, (info_x - 180, info_y + 10))

        # Draw the image
        self.screen.blit(image, (info_x - 230, info_y + 12))

    def draw(self):
        # self.screen.fill((245, 155, 66))  # 36, 148, 209
        self.update_button_scale()  # Call the update_button_scale method

        # Draw button with scaled size
        scaled_button_image = pygame.transform.scale(self.button_image, (
            int(self.button_rect.width * self.button_scale), int(self.button_rect.height * self.button_scale)))
        self.screen.blit(scaled_button_image, self.button_rect)

        # Skill Buttons
        self.create_skill_button(self.question_mark_skill, self.skill_rect,
                                 '+5 per Click')
        self.create_skill_button(self.question_mark_skill, self.skill_rect2,
                                 '+5 per Click')
        self.create_skill_button(self.question_mark_skill, self.skill_rect3,
                                 '+5 per Click')
        self.create_skill_button(self.question_mark_skill, self.skill_rect4,
                                 '+5 per Click')
        self.create_skill_button(self.question_mark_skill, self.skill_rect5,
                                 '+5 per Click')
        self.create_skill_button(self.question_mark_skill, self.skill_rect6,
                                 '+5 per Click')

        # Erstellen der Kauf-Buttons auf
        self.create_button(self.buy_pig_button_rect, (209, 50, 36), "Pig", self.pig_cost, 1, self.pig_owned,
                           self.pig_image, self.buy_pig)
        if self.pig_owned >= 2:
            self.create_button(self.buy_bubbles_button_rect, (209, 50, 36), "Bubbles", self.bubbles_cost, 5,
                               self.bubbles_owned, self.bubbles_image, self.buy_bubbles)
            if self.frying_pan_owned:
                self.create_button(self.buy_frying_pan_button_rect, (179, 181, 177), "Frying Pan", self.frying_pan_cost,
                                   'frying_pan', self.frying_pan_owned, self.frying_pan, self.buy_frying_pan)
                self.create_skill_button(self.frying_pan_skill, self.skill_rect,
                                         '+5 per Click')  # Skill Button
            else:
                self.create_button(self.buy_frying_pan_button_rect, (209, 50, 36), "Frying Pan", self.frying_pan_cost,
                                   'frying_pan', self.frying_pan_owned, self.frying_pan, self.buy_frying_pan)
        if self.bubbles_owned >= 2:
            self.create_button(self.buy_silverbacon_button_rect, (209, 50, 36), "Silver Bacon", self.silverbacon_cost,
                               20,
                               self.silverbacon_owned, self.silverbacon_image, self.buy_silverbacon)
        if self.silverbacon_owned >= 2:
            self.create_button(self.buy_goldenbacon_button_rect, (209, 50, 36), "Golden Bacon", self.goldenbacon_cost,
                               50,
                               self.goldenbacon_owned, self.goldenbacon_image, self.buy_goldenbacon)

        font = pygame.font.Font(None, 36)

        # Balance text
        text_balance = self.font_32.render(f"Bacon: {self.balance}", True, (255, 255, 255))
        text_balance2 = self.font_26.render(f"per second: {self.balance_per_second}", True, (255, 255, 255))
        self.screen.blit(text_balance, (10, 10))
        self.screen.blit(text_balance2, (20, 35))

        # Display hints
        self.update_hints()
        current_hint = self.hints[self.current_hint_index]
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 560, 800, 40))  # 101, 172, 224
        text_hints = self.font_20.render(f"Bacon says: {current_hint}", True, (0, 0, 0))
        self.screen.blit(text_hints, (10, 570))

        pygame.display.flip()

    def update_balance_per_second(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.timer

        if elapsed_time >= 1000:  # Update every 1000 milliseconds (1 second)
            self.balance += self.balance_per_second
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

    def update_hints(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.hint_timer

        if elapsed_time >= self.hint_duration:
            self.hint_timer = current_time
            self.current_hint_index = (self.current_hint_index + 1) % len(self.hints)

    def buy_pig(self):
        if self.balance >= self.pig_cost:
            self.balance -= self.pig_cost
            self.balance_per_second += 1
            self.pig_cost += int(15 * (self.pig_owned + 1) ** 1.5)
            self.pig_owned += 1
            if self.pig_owned == 5:
                self.click_rate += 1
            if self.pig_owned == 10:
                self.click_rate += 2
            print(f"Pig bought! You own {self.pig_owned} Pigs. Next one costs {self.pig_cost}!")
        else:
            print("Not enough balance to buy a pig")

    def buy_bubbles(self):
        if self.pig_owned >= 2:
            if self.balance >= self.bubbles_cost:
                self.balance -= self.bubbles_cost
                self.balance_per_second += 5
                self.bubbles_cost += int(50 * (self.bubbles_owned + 1) ** 1.5)
                self.bubbles_owned += 1
                if self.bubbles_owned == 5:
                    self.click_rate += 2
                if self.bubbles_owned == 10:
                    self.click_rate += 4
                print(f"Bubbles bought! You own {self.bubbles_owned} Bubbles. Next one costs {self.bubbles_cost}!")
            else:
                print("Not enough balance to buy a bubbles")

    def buy_frying_pan(self):
        if self.bubbles_owned >= 2:
            if self.balance >= self.frying_pan_cost:
                self.click_rate += 5
                self.frying_pan_owned = True
                print(f"Frying pan bought!")
            else:
                print("Not enough balance to buy a frying pan")

    def buy_silverbacon(self):
        if self.bubbles_owned >= 2:
            if self.balance >= self.silverbacon_cost:
                self.balance -= self.silverbacon_cost
                self.balance_per_second += 20
                self.silverbacon_cost += int(50 * (self.silverbacon_owned + 1) ** 1.5)
                self.silverbacon_owned += 1
                print(
                    f"Silver bacon bought! You own {self.silverbacon_owned} silver bacon. Next one costs {self.silverbacon_cost}!")
            else:
                print("Not enough balance to buy a silver bacon")

    def buy_goldenbacon(self):
        if self.silverbacon_owned >= 2:
            if self.balance >= self.goldenbacon_cost:
                self.balance -= self.goldenbacon_cost
                self.balance_per_second += 50
                self.goldenbacon_cost += int(50 * (self.goldenbacon_owned + 1) ** 1.5)
                self.goldenbacon_owned += 1
                print(
                    f"Golden bacon bought! You own {self.goldenbacon_owned} golden bacon. Next one costs {self.goldenbacon_cost}!")
            else:
                print("Not enough balance to buy a goldenbacon")

    def click(self):
        self.balance += self.click_rate
        self.sound_click.play()

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
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.button_rect.collidepoint(event.pos):
                        self.click()
                    elif self.buy_pig_button_rect.collidepoint(event.pos):
                        self.buy_pig()
                    elif self.buy_bubbles_button_rect.collidepoint(event.pos):
                        self.buy_bubbles()
                    elif self.buy_silverbacon_button_rect.collidepoint(event.pos):
                        self.buy_silverbacon()
                    elif self.buy_goldenbacon_button_rect.collidepoint(event.pos):
                        self.buy_goldenbacon()
                    elif self.buy_frying_pan_button_rect.collidepoint(event.pos) and not self.frying_pan_owned:
                        self.buy_frying_pan()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_s and not self.saving_in_progress:
                    self.saving_in_progress = True  # Set the flag
                    self.save_game_state()

                # Check if the 'S' key is released
                if event.type == pygame.KEYUP and event.key == pygame.K_s:
                    self.saving_in_progress = False  # Reset the flag

                if event.type == pygame.KEYDOWN and event.key == pygame.K_l and not self.saving_in_progress:
                    self.loading_in_progress = True  # Set the flag
                    self.load_game_state()

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
    # game.load_or_create_game_state()  # Turned off for testing purposes
    game.run()

# TODO Abilities to buy that will increase clickrate Events: all 120 seconds make button appear to give click rate boost
# TODO Maximum of 10 per Item, step 5 and 10 give bonusses
# TODO Change Frame Size accordingly
# TODO Background diagonal one color, bacon and stars repeatedly, moving
# TODO Arrow that points to bacon and is moving
# TODO Make bacon zoom to its center when clicked
# TODO make pointer to fitting icon
# TODO Textbox für prints
# TODO Sound effects
# DONE Tips on button in  list of strings, change all 10-15 seconds

""" Erik Feedback
- Feedback bei Upgrade / animation
- mehr Upgrades
- Bacon Bild verändern je nachdem wie weit man ist
"""
