from format_numbers import FormattedNumber

class Upgrades:
    def __init__(self, pygame):
        self.upgrade_0_owned = FormattedNumber(0)  #228
        self.upgrade_0_initial_cost = FormattedNumber(15)
        self.upgrade_0_cost = FormattedNumber(15 * (1 + 0.15) ** self.upgrade_0_owned.value) # TODO
        self.upgrade_0_base_increase = FormattedNumber(.2)
        self.upgrade_0_increase = FormattedNumber(.2)

        self.upgrade_1_owned = FormattedNumber(5)
        self.upgrade_1_initial_cost = FormattedNumber(100)
        self.upgrade_1_cost = FormattedNumber(100 * (1 + 1.15) ** self.upgrade_1_owned.value)
        self.upgrade_1_base_increase = FormattedNumber(1)
        self.upgrade_1_increase = FormattedNumber(1)

        self.upgrade_2_owned = FormattedNumber(5)
        self.upgrade_2_initial_cost = FormattedNumber(500)
        self.upgrade_2_cost = FormattedNumber(500 * (1 + 1.15) ** self.upgrade_2_owned.value)
        self.upgrade_2_base_increase = FormattedNumber(8)
        self.upgrade_2_increase = FormattedNumber(8)

        self.upgrade_3_owned = FormattedNumber(5)
        self.upgrade_3_initial_cost = FormattedNumber(3000)
        self.upgrade_3_cost = FormattedNumber(3000 * (1 + 1.15) ** self.upgrade_3_owned.value)
        self.upgrade_3_base_increase = FormattedNumber(20)
        self.upgrade_3_increase = FormattedNumber(20)

        self.upgrade_4_owned = FormattedNumber(5)
        self.upgrade_4_initial_cost = FormattedNumber(15000)
        self.upgrade_4_cost = FormattedNumber(150900 * (1 + 1.15) ** self.upgrade_4_owned.value)
        self.upgrade_4_base_increase = FormattedNumber(80)
        self.upgrade_4_increase = FormattedNumber(80)

        self.upgrade_5_owned = FormattedNumber(5)
        self.upgrade_5_initial_cost = FormattedNumber(100000)
        self.upgrade_5_cost = FormattedNumber(100000 * (1 + 1.15) ** self.upgrade_5_owned.value)
        self.upgrade_5_base_increase = FormattedNumber(500)
        self.upgrade_5_increase = FormattedNumber(500)

        self.upgrade_6_owned = FormattedNumber(5)
        self.upgrade_6_initial_cost = FormattedNumber(500000)
        self.upgrade_6_cost = FormattedNumber(500000 * (1 + 1.15) ** self.upgrade_6_owned.value)
        self.upgrade_6_base_increase = FormattedNumber(3000)
        self.upgrade_6_increase = FormattedNumber(3000)

        self.upgrade_7_owned = FormattedNumber(5)
        self.upgrade_7_initial_cost = FormattedNumber(2500000)
        self.upgrade_7_cost = FormattedNumber(2500000 * (1 + 1.15) ** self.upgrade_7_owned.value)
        self.upgrade_7_base_increase = FormattedNumber(10000)
        self.upgrade_7_increase = FormattedNumber(10000)

        self.balance = FormattedNumber(1111111)
        self.initial_click_rate = FormattedNumber(1)
        self.click_rate = FormattedNumber(1)
        self.balance_per_second = FormattedNumber(
            0.00 + (self.upgrade_1_owned.value * self.upgrade_1_base_increase.value) + (
                    self.upgrade_2_owned.value * self.upgrade_2_base_increase.value) + (
                    self.upgrade_3_owned.value * self.upgrade_3_base_increase.value) + (
                    self.upgrade_4_owned.value * self.upgrade_4_base_increase.value) + (
                    self.upgrade_5_owned.value * self.upgrade_5_base_increase.value) + (
                    self.upgrade_6_owned.value * self.upgrade_6_base_increase.value) + (
                    self.upgrade_7_owned.value * self.upgrade_7_base_increase.value))
        # Images

        # Button-geometry / 60 px unterschied untereinander
        self.buy_upgrade_0_button_rect = pygame.Rect((550, 65, 230, 50))
        self.buy_upgrade_1_button_rect = pygame.Rect(550, 125, 230, 50)
        self.buy_upgrade_2_button_rect = pygame.Rect(550, 185, 230, 50)
        self.buy_upgrade_3_button_rect = pygame.Rect(550, 245, 230, 50)
        self.buy_upgrade_4_button_rect = pygame.Rect(550, 305, 230, 50)
        self.buy_upgrade_5_button_rect = pygame.Rect(550, 365, 230, 50)
        self.buy_upgrade_6_button_rect = pygame.Rect(550, 425, 230, 50)
        self.buy_upgrade_7_button_rect = pygame.Rect(550, 485, 230, 50)

        self.skill_rect = pygame.Rect(20, 65, 50, 50)
        self.skill_rect2 = pygame.Rect(20, 120, 50, 50)
        self.skill_rect3 = pygame.Rect(20, 175, 50, 50)
        self.skill_rect4 = pygame.Rect(20, 230, 50, 50)
        self.skill_rect5 = pygame.Rect(20, 285, 50, 50)
        self.skill_rect6 = pygame.Rect(20, 340, 50, 50)
        self.skill_rect7 = pygame.Rect(20, 395, 50, 50)
        self.skill_rect8 = pygame.Rect(20, 450, 50, 50)
        self.skill_rect9 = pygame.Rect(85, 230, 105, 105)

    def buy_upgrade_0(self):
        if self.balance >= self.upgrade_0_cost:
            self.balance -= self.upgrade_0_cost
            self.balance_per_second += self.upgrade_0_increase
            self.upgrade_0_cost = self.upgrade_0_cost
            # self.upgrade_0_cost += 15 * (0 + .15 ** (self.upgrade_0_owned.value +1))
            self.upgrade_0_owned += 1

            print(
                f"Frying Pan bought! You own {self.upgrade_0_owned.value} Frying Pans. Next one costs {FormattedNumber(self.upgrade_0_cost).formatted()}!")
        else:
            print("Not enough balance to buy a frying pan")

    def buy_upgrade_1(self):
        if self.balance >= self.upgrade_1_cost:
            self.balance -= self.upgrade_1_cost
            self.balance_per_second += self.upgrade_1_increase
            self.upgrade_1_cost = FormattedNumber(self.upgrade_1_initial_cost.value * (1 + 0.15) ** (self.upgrade_1_owned.value + 1))
            self.upgrade_1_owned += 1
            print(
                f"Pig bought! You own {self.upgrade_1_owned.value} Pigs. Next one costs {FormattedNumber(self.upgrade_1_cost).formatted()}!")
        else:
            print("Not enough balance to buy a upgrade_1")

    def buy_upgrade_2(self):
        if self.upgrade_1_owned >= 2:
            if self.balance >= self.upgrade_2_cost:
                self.balance -= self.upgrade_2_cost
                self.balance_per_second += self.upgrade_2_increase
                self.upgrade_2_cost += FormattedNumber(self.upgrade_2_initial_cost.value * (1 + 0.15) ** (self.upgrade_2_owned.value + 1))
                self.upgrade_2_owned += 1
                print(
                    f"Upgrade 2 bought! You own {self.upgrade_2_owned.value} Upgrade 2. Next one costs {FormattedNumber(self.upgrade_2_cost).formatted()}!")
            else:
                print("Not enough balance to buy a upgrade_2")

    def buy_upgrade_3(self):
        if self.upgrade_2_owned >= 2:
            if self.balance >= self.upgrade_3_cost:
                self.balance -= self.upgrade_3_cost
                self.balance_per_second += self.upgrade_3_increase
                self.upgrade_3_cost += FormattedNumber(self.upgrade_3_initial_cost.value * (1 + 0.15) ** (self.upgrade_3_owned.value + 1))
                self.upgrade_3_owned += 1
                print(
                    f"Silver bacon bought! You own {self.upgrade_3_owned.value} silver bacon. "
                    f"Next one costs {FormattedNumber(self.upgrade_3_cost).formatted()}!")
            else:
                print("Not enough balance to buy a silver bacon")

    def buy_upgrade_4(self):
        if self.upgrade_3_owned >= 2:
            if self.balance >= self.upgrade_4_cost:
                self.balance -= self.upgrade_4_cost
                self.balance_per_second += self.upgrade_4_increase
                self.upgrade_4_cost += FormattedNumber(self.upgrade_4_initial_cost.value * (1 + 0.15) ** (self.upgrade_4_owned.value + 1))
                self.upgrade_4_owned += 1
                print(
                    f"Golden bacon bought! You own {self.upgrade_4_owned.value} golden bacon. "
                    f"Next one costs {FormattedNumber(self.upgrade_4_cost).formatted()}!")
            else:
                print("Not enough balance to buy a upgrade_4")

    def buy_upgrade_5(self):
        if self.upgrade_4_owned >= 2:
            if self.balance >= self.upgrade_5_cost:
                self.balance -= self.upgrade_5_cost
                self.balance_per_second += self.upgrade_5_increase
                self.upgrade_5_cost += FormattedNumber(self.upgrade_5_initial_cost.value * (1 + 0.15) ** (self.upgrade_5_owned.value + 1))
                self.upgrade_5_owned += 1
                print(
                    f"Upgrade 6 bought! You own {self.upgrade_5_owned.value} upgrade 6. "
                    f"Next one costs {FormattedNumber(self.upgrade_5_cost).formatted()}!")
            else:
                print("Not enough balance to buy an upgrade 6")

    def buy_upgrade_6(self):
        if self.upgrade_5_owned >= 2:
            if self.balance >= self.upgrade_6_cost:
                self.balance -= self.upgrade_6_cost
                self.balance_per_second += self.upgrade_6_increase
                self.upgrade_6_cost += FormattedNumber(self.upgrade_6_initial_cost.value * (1 + 0.15) ** (self.upgrade_6_owned.value + 1))
                self.upgrade_6_owned += 1
                print(
                    f"Upgrade 7 bought! You own {self.upgrade_6_owned.value} upgrade 7. "
                    f"Next one costs {FormattedNumber(self.upgrade_6_cost).formatted()}!")
            else:
                print("Not enough balance to buy an upgrade 7")

    def buy_upgrade_7(self):
        if self.upgrade_6_owned >= 2:
            if self.balance >= self.upgrade_7_cost:
                self.balance -= self.upgrade_7_cost
                self.balance_per_second += self.upgrade_7_increase
                self.upgrade_7_cost += FormattedNumber(self.upgrade_7_initial_cost.value * (1 + 0.15) ** (self.upgrade_7_owned.value + 1))
                self.upgrade_7_owned += 1
                print(
                    f"Upgrade 8 bought! You own {self.upgrade_7_owned.value} upgrade 8. "
                    f"Next one costs {self.upgrade_7_cost.formatted()}!")
            else:
                print("Not enough balance to buy an upgrade 8")