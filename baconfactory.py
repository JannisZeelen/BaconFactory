# import time
import sys
import json
import pygame


class Game:
    def __init__(self):
        # Pygame Init
        pygame.init()

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

        self.balance = 1000000
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
                      'You get a bonus when you reach 5 and 10 of one item!',
                      'Unlock new items by buying more items.',
                      'Rumors say there is an ending.']
        self.current_hint_index = 0
        self.hint_timer = pygame.time.get_ticks()
        self.hint_duration = 5000  # Display each hint for 5 seconds

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bacon Factory")

        # Load button image and resize it
        original_button_image = pygame.image.load("assets/img/baconPog.png")
        button_width, button_height = original_button_image.get_width() // 2, original_button_image.get_height() // 2

        # Set the initial size and position of the button image
        self.button_scale = 1.0
        self.button_image = pygame.transform.scale(original_button_image, (
            int(button_width * self.button_scale), int(button_height * self.button_scale)))

        self.button_rect = self.button_image.get_rect()
        self.button_rect.topleft = (10, 80)

        # Load images
        self.pig_image = pygame.image.load("assets/img/pig.png")
        self.pig_image = pygame.transform.scale(self.pig_image, (40, 40))

        self.bubbles_image = pygame.image.load("assets/img/bubbles.png")
        self.bubbles_image = pygame.transform.scale(self.bubbles_image, (40, 40))

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

    def create_button(self, rect, color, label, cost, bps_increase, owned, image, buy_function):
        # Draw button
        pygame.draw.rect(self.screen, color, rect)
        # Display additional information next to the button
        info_x = rect.right + 10
        info_y = rect.top - 7

        text = self.font_22.render(label, True, (255, 255, 255))
        cost_text_color = (58, 189, 2) if self.balance >= cost else (184, 180, 180)  # Green if balance >= cost, el red
        if bps_increase == 'frying_pan':
            cost_text = self.font_18.render(f"Cost: {cost} +1 click", True, cost_text_color)
        else:
            cost_text = self.font_18.render(f"Cost: {cost} +{bps_increase}/s", True, cost_text_color)
            owned_text = self.font_24.render(f"{owned}", True, (201, 201, 201))
            owned_text.set_alpha(150)
            self.screen.blit(owned_text, (info_x - 36, info_y + 16))

        # Position the text next to the button
        self.screen.blit(text, (info_x - 180, info_y + 10))
        self.screen.blit(cost_text, (info_x - 180, info_y + 32))

        # Draw the image
        self.screen.blit(image, (info_x - 230, info_y + 12))

    def draw(self):
        self.screen.fill((245, 155, 66))  # 36, 148, 209
        self.update_button_scale()  # Call the update_button_scale method

        # Draw button with scaled size
        scaled_button_image = pygame.transform.scale(self.button_image, (
            int(self.button_rect.width * self.button_scale), int(self.button_rect.height * self.button_scale)))
        self.screen.blit(scaled_button_image, self.button_rect)

        # Erstellen der Kauf-Buttons auf
        self.create_button(self.buy_pig_button_rect, (209, 50, 36), "Pig", self.pig_cost, 1, self.pig_owned,
                           self.pig_image, self.buy_pig)
        if self.pig_owned >= 2:
            self.create_button(self.buy_bubbles_button_rect, (209, 50, 36), "Bubbles", self.bubbles_cost, 5,
                               self.bubbles_owned, self.bubbles_image, self.buy_bubbles)
            if self.frying_pan_owned:
                self.create_button(self.buy_frying_pan_button_rect, (179, 181, 177), "Frying Pan", self.frying_pan_cost,
                                   'frying_pan', self.frying_pan_owned, self.pig_image, self.buy_frying_pan)
            else:
                self.create_button(self.buy_frying_pan_button_rect, (209, 50, 36), "Frying Pan", self.frying_pan_cost,
                                   'frying_pan', self.frying_pan_owned, self.pig_image, self.buy_frying_pan)
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
        text_balance = self.font_32.render(f"Bacon: {self.balance}", True, (0, 0, 0))
        text_balance2 = self.font_26.render(f"per second: {self.balance_per_second}", True, (0, 0, 0))
        self.screen.blit(text_balance, (10, 10))
        self.screen.blit(text_balance2, (20, 35))

        # Display hints
        self.update_hints()
        current_hint = self.hints[self.current_hint_index]
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
            print(f"Pig bought! You own {self.pig_owned} Pigs. Next one costs {self.pig_cost}!")
        else:
            print("Not enough balance to buy a pig")

    def buy_bubbles(self):
        if self.balance >= self.bubbles_cost:
            self.balance -= self.bubbles_cost
            self.balance_per_second += 5
            self.bubbles_cost += int(50 * (self.bubbles_owned + 1) ** 1.5)
            self.bubbles_owned += 1
            print(f"Bubbles bought! You own {self.bubbles_owned} Bubbles. Next one costs {self.bubbles_cost}!")
        else:
            print("Not enough balance to buy a bubbles")

    def buy_frying_pan(self):
        if self.balance >= self.frying_pan_cost:
            self.click_rate += 1
            self.frying_pan_owned = True
            print(f"Frying pan bought!")
        else:
            print("Not enough balance to buy a frying pan")

    def buy_silverbacon(self):
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

    def run(self):
        clock = pygame.time.Clock()

        while True:
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

# TODO Abilities to buy that will increase clickrate
# TODO Maximum of 10 per Item, step 5 and 10 give bonusses
# TODO Change Frame Size accordingly
# TODO Background diagonal one color, bacon and stars repeatedly, moving
# TODO Arrow that points to bacon and is moving
# TODO Make bacon zoom to its center when clicked
# TODO Events: all 120 seconds make button appear to give click rate boost
# TODO make pointer to fitting icon
# TODO Textbox für prints
# DONE Tips on button in  list of strings, change all 10-15 seconds
