import time
import sys
import json
import pygame


class Game:
    def __init__(self):
        self.balance = 0
        self.balance_per_second = 0
        self.pig_cost = 15
        self.pig_owned = 0
        self.bubbles_cost = 100
        self.bubbles_owned = 0
        self.silverbacon_cost = 500
        self.silverbacon_owned = 0
        self.goldenbacon_cost = 2000
        self.goldenbacon_owned = 0
        # global_font = pygame.font.Font('') # TODO
        self.timer = pygame.time.get_ticks()

        # Pygame Init
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Bacon Factory")

        # Load button image and resize it
        original_button_image = pygame.image.load("img/baconPog.png")
        button_width, button_height = original_button_image.get_width() // 2, original_button_image.get_height() // 2

        # Set the initial size and position of the button image
        self.button_scale = 1.0
        self.button_image = pygame.transform.scale(original_button_image, (
            int(button_width * self.button_scale), int(button_height * self.button_scale)))

        self.button_rect = self.button_image.get_rect()
        self.button_rect.topleft = (10, 50)

        # Load images
        self.pig_image = pygame.image.load("img/pig.png")
        self.pig_image = pygame.transform.scale(self.pig_image, (40, 40))

        self.bubbles_image = pygame.image.load("img/bubbles.png")
        self.bubbles_image = pygame.transform.scale(self.bubbles_image, (40, 40))

        self.silverbacon_image = pygame.image.load("img/silver.png")
        self.silverbacon_image = pygame.transform.scale(self.silverbacon_image, (40, 40))

        self.goldenbacon_image = pygame.image.load("img/golden.png")
        self.goldenbacon_image = pygame.transform.scale(self.goldenbacon_image, (40, 40))

        # Buttongeometry / 80 px unterschied untereinander
        self.buy_pig_button_rect = pygame.Rect(self.width - 250, 50, 120, 40)
        self.buy_bubbles_button_rect = pygame.Rect(self.width - 250, 130, 120, 40)
        self.buy_silverbacon_button_rect = pygame.Rect(self.width - 250, 210, 120, 40)
        self.buy_goldenbacon_button_rect = pygame.Rect(self.width - 250, 290, 120, 40)

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
        self.draw_button(rect, color, label)

        # Display additional information next to the button
        info_font = pygame.font.Font(None, 20)
        cost_text = info_font.render(f"Cost: {cost}", True, (0, 0, 0))
        bps_increase_text = info_font.render(f"BPS Increase: +{bps_increase}", True, (0, 0, 0))
        owned_text = info_font.render(f"Owned: {owned}", True, (0, 0, 0))

        # Position the text next to the button
        info_x = rect.right + 10
        info_y = rect.top - 7
        self.screen.blit(cost_text, (info_x, info_y))
        self.screen.blit(bps_increase_text, (info_x, info_y + 20))
        self.screen.blit(owned_text, (info_x, info_y + 40))

        # Draw the image
        self.screen.blit(image, (info_x - 175, info_y + 5))

        # # Check for button click
        # if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
        #     buy_function() # TODO change behaviour like in event catcher down at the end of code

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.update_button_scale()  # Call the update_button_scale method

        # Draw button with scaled size
        scaled_button_image = pygame.transform.scale(self.button_image, (
            int(self.button_rect.width * self.button_scale), int(self.button_rect.height * self.button_scale)))
        self.screen.blit(scaled_button_image, self.button_rect)

        # Erstellen der Kauf-Buttons auf
        self.create_button(self.buy_pig_button_rect, (0, 128, 0), "Pig", self.pig_cost, 1, self.pig_owned,
                           self.pig_image, self.buy_pig)
        self.create_button(self.buy_bubbles_button_rect, (0, 128, 0), "Bubbles", self.bubbles_cost, 5,
                           self.bubbles_owned, self.bubbles_image, self.buy_bubbles)
        self.create_button(self.buy_silverbacon_button_rect, (0, 128, 0), "Silver Bacon", self.silverbacon_cost, 20,
                           self.silverbacon_owned, self.silverbacon_image, self.buy_silverbacon)
        self.create_button(self.buy_goldenbacon_button_rect, (0, 128, 0), "Golden Bacon", self.goldenbacon_cost, 50,
                           self.goldenbacon_owned, self.goldenbacon_image, self.buy_goldenbacon)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Bacon: {self.balance} - Bacon per second: {self.balance_per_second}", True, (0, 0, 0))

        self.screen.blit(text, (10, 10))

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

    def draw_button(self, button_rect, color, label):
        pygame.draw.rect(self.screen, color, button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render(label, True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=button_rect.center)
        self.screen.blit(text, text_rect)

    def buy_pig(self):
        if self.balance >= self.pig_cost:
            self.balance -= self.pig_cost
            self.balance_per_second += 1
            self.pig_cost += int(10 * (self.pig_owned + 1) ** 1.5)
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
        self.balance += 1

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

            self.update_balance_per_second()
            self.draw()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:  # Save game state when 'S' key is pressed
                self.save_game_state()

            elif keys[pygame.K_l]:  # Load game state when 'L' key is pressed
                self.load_game_state()

            clock.tick(60)


if __name__ == "__main__":
    game = Game()
    # Load initial game state or create a new one
    game.load_or_create_game_state()
    game.run()
