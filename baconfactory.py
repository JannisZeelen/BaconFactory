import time
import sys
import pygame


class Game:
    def __init__(self):
        self.balance = 0
        self.balance_per_second = 0
        self.pig_cost = 15
        self.pig_owned = 0
        # global_font = pygame.font.Font('')
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

        self.buy_pig_button_rect = pygame.Rect(self.width - 250, 50, 120, 40)

    def update_balance_per_second(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.timer

        if elapsed_time >= 1000:  # Update every 1000 milliseconds (1 second)
            self.balance += self.balance_per_second
            self.timer = current_time

    def update_button_scale(self):
        # Update the button scale based on mouse button state
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0] and self.button_rect.collidepoint(pygame.mouse.get_pos()):  # Check if left mouse button is down and clicked on the left button:  # Check if left mouse button is down
            self.button_scale -= 0.02  # Adjust the zoom-out speed
        else:
            self.button_scale += 0.02  # Adjust the zoom-in speed

        # Clamp the button scale to avoid negative or too large values
        self.button_scale = max(0.8, min(1.0, self.button_scale))

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.update_button_scale()  # Call the update_button_scale method

        # Draw button with scaled size
        scaled_button_image = pygame.transform.scale(self.button_image, (
            int(self.button_rect.width * self.button_scale), int(self.button_rect.height * self.button_scale)))
        self.screen.blit(scaled_button_image, self.button_rect)

        # Draw Buy Pig button
        buy_pig_label = f"Buy Pig\nCost: {self.pig_cost}\nBPS Increase: +1\nPigs Owned: {self.pig_owned}" if self.balance >= self.pig_cost else "Not enough balance"
        self.draw_button(self.buy_pig_button_rect, (0, 128, 0), "Buy Pig")
        # Display additional information next to the button
        info_font = pygame.font.Font(None, 20)
        cost_text = info_font.render(f"Cost: {self.pig_cost}", True, (0, 0, 0))
        bps_increase_text = info_font.render("BPS Increase: +1", True, (0, 0, 0))
        pigs_owned_text = info_font.render(f"Pigs Owned: {self.pig_owned}", True, (0, 0, 0))

        # Position the text next to the button
        info_x = self.buy_pig_button_rect.right + 10
        info_y = self.buy_pig_button_rect.top
        self.screen.blit(cost_text, (info_x, info_y))
        self.screen.blit(bps_increase_text, (info_x, info_y + 20))
        self.screen.blit(pigs_owned_text, (info_x, info_y + 40))

        font = pygame.font.Font(None, 36)
        text = font.render(f"Bacon: {self.balance} - Bacon per second: {self.balance_per_second}", True, (0, 0, 0))

        self.screen.blit(text, (10, 10))

        pygame.display.flip()

    def draw_button(self, button_rect, color, label):
        pygame.draw.rect(self.screen, color, button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render(label, True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=button_rect.center)
        self.screen.blit(text, text_rect)

    def buy_pig(self):
        if self.balance >= self.pig_cost:
            self.balance -= self.balance
            self.balance_per_second += 1
            self.pig_cost += int(10 * (self.pig_owned + 1) ** 1.5)
            self.pig_owned += 1
            print(f"Pig Bought! You own {self.pig_owned} Pigs. Next one costs {self.pig_cost}!")
        else:
            print("Not enough balance to buy a pig")

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

            self.update_balance_per_second()
            self.draw()
            clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()

# TODO: Font
