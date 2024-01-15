from format_numbers import FormattedNumber


class Upgrades:
    def __init__(self, pygame):
        self.upgrade_0_owned = FormattedNumber(10)
        self.upgrade_0_initial_cost = FormattedNumber(15)
        self.upgrade_0_cost = FormattedNumber(15)
        self.upgrade_0_base_increase = FormattedNumber(.2)
        self.upgrade_0_increase = FormattedNumber(.2)
        self.upgrade_0_current_bps = FormattedNumber(0)
        self.upgrade_0_current_multiplier = FormattedNumber(1)

        self.upgrade_1_owned = FormattedNumber(1)
        self.upgrade_1_initial_cost = FormattedNumber(100)
        self.upgrade_1_cost = FormattedNumber(100)
        self.upgrade_1_base_increase = FormattedNumber(1)
        self.upgrade_1_increase = FormattedNumber(1)
        self.upgrade_1_current_bps = FormattedNumber(0)
        self.upgrade_1_current_multiplier = FormattedNumber(1)

        self.upgrade_2_owned = FormattedNumber(1)
        self.upgrade_2_initial_cost = FormattedNumber(500)
        self.upgrade_2_cost = FormattedNumber(500)
        self.upgrade_2_base_increase = FormattedNumber(8)
        self.upgrade_2_increase = FormattedNumber(8)
        self.upgrade_2_current_bps = FormattedNumber(0)
        self.upgrade_2_current_multiplier = FormattedNumber(1)

        self.upgrade_3_owned = FormattedNumber(1)
        self.upgrade_3_initial_cost = FormattedNumber(3000)
        self.upgrade_3_cost = FormattedNumber(3000)
        self.upgrade_3_base_increase = FormattedNumber(20)
        self.upgrade_3_increase = FormattedNumber(20)
        self.upgrade_3_current_bps = FormattedNumber(0)
        self.upgrade_3_current_multiplier = FormattedNumber(1)

        self.upgrade_4_owned = FormattedNumber(1)
        self.upgrade_4_initial_cost = FormattedNumber(15000)
        self.upgrade_4_cost = FormattedNumber(15000)
        self.upgrade_4_base_increase = FormattedNumber(80)
        self.upgrade_4_increase = FormattedNumber(80)
        self.upgrade_4_current_bps = FormattedNumber(0)
        self.upgrade_4_current_multiplier = FormattedNumber(1)

        self.upgrade_5_owned = FormattedNumber(1)
        self.upgrade_5_initial_cost = FormattedNumber(100000)
        self.upgrade_5_cost = FormattedNumber(100000)
        self.upgrade_5_base_increase = FormattedNumber(500)
        self.upgrade_5_increase = FormattedNumber(500)
        self.upgrade_5_current_bps = FormattedNumber(0)
        self.upgrade_5_current_multiplier = FormattedNumber(1)

        self.upgrade_6_owned = FormattedNumber(1)
        self.upgrade_6_initial_cost = FormattedNumber(500000)
        self.upgrade_6_cost = FormattedNumber(500000)
        self.upgrade_6_base_increase = FormattedNumber(3000)
        self.upgrade_6_increase = FormattedNumber(3000)
        self.upgrade_6_current_bps = FormattedNumber(0)
        self.upgrade_6_current_multiplier = FormattedNumber(1)

        self.upgrade_7_owned = FormattedNumber(1)
        self.upgrade_7_initial_cost = FormattedNumber(2500000)
        self.upgrade_7_cost = FormattedNumber(2500000)
        self.upgrade_7_base_increase = FormattedNumber(10000)
        self.upgrade_7_increase = FormattedNumber(10000)
        self.upgrade_7_current_bps = FormattedNumber(0)
        self.upgrade_7_current_multiplier = FormattedNumber(1)

        # Calculating multiplier
        upgrades = [
            self.upgrade_0_owned, self.upgrade_1_owned, self.upgrade_2_owned,
            self.upgrade_3_owned, self.upgrade_4_owned, self.upgrade_5_owned,
            self.upgrade_6_owned, self.upgrade_7_owned
        ]

        for i, upgrade in enumerate(upgrades):
            setattr(self, f"upgrade_{i}_current_multiplier", self.calculate_multiplier(upgrade))

        # recalculating upgrade costs
        self.recalculate_upgrade_costs()

        self.balance = FormattedNumber(0)
        self.initial_click_rate = FormattedNumber(1)
        self.click_rate = FormattedNumber(1)
        self.click_multiplier = FormattedNumber(1)
        self.total_clicks = FormattedNumber(0)
        self.balance_per_second = FormattedNumber(
            0.00 + (self.upgrade_0_owned.value * self.upgrade_0_base_increase.value) *
            self.upgrade_0_current_multiplier.value +
            (
                        self.upgrade_1_owned.value * self.upgrade_1_base_increase.value) * self.upgrade_1_current_multiplier.value + (
                    self.upgrade_2_owned.value * self.upgrade_2_base_increase.value) * self.upgrade_2_current_multiplier.value + (
                    self.upgrade_3_owned.value * self.upgrade_3_base_increase.value) * self.upgrade_3_current_multiplier.value + (
                    self.upgrade_4_owned.value * self.upgrade_4_base_increase.value) * self.upgrade_4_current_multiplier.value + (
                    self.upgrade_5_owned.value * self.upgrade_5_base_increase.value) * self.upgrade_5_current_multiplier.value + (
                    self.upgrade_6_owned.value * self.upgrade_6_base_increase.value) * self.upgrade_6_current_multiplier.value + (
                    self.upgrade_7_owned.value * self.upgrade_7_base_increase.value) * self.upgrade_7_current_multiplier.value)


        # Images

        # Button-geometry / 60+10 px unterschied untereinander
        self.buy_upgrade_0_button_rect = pygame.Rect((980, 65, 280, 60))
        self.buy_upgrade_1_button_rect = pygame.Rect(980, 135, 280, 60)
        self.buy_upgrade_2_button_rect = pygame.Rect(980, 205, 280, 60)
        self.buy_upgrade_3_button_rect = pygame.Rect(980, 275, 280, 60)
        self.buy_upgrade_4_button_rect = pygame.Rect(980, 345, 280, 60)
        self.buy_upgrade_5_button_rect = pygame.Rect(980, 415, 280, 60)
        self.buy_upgrade_6_button_rect = pygame.Rect(980, 485, 280, 60)
        self.buy_upgrade_7_button_rect = pygame.Rect(980, 555, 280, 60)

        self.skill_rect = pygame.Rect(20, 65, 50, 50)
        self.skill_rect2 = pygame.Rect(20, 120, 50, 50)
        self.skill_rect3 = pygame.Rect(20, 175, 50, 50)
        self.skill_rect4 = pygame.Rect(20, 230, 50, 50)
        self.skill_rect5 = pygame.Rect(20, 285, 50, 50)
        self.skill_rect6 = pygame.Rect(20, 340, 50, 50)
        self.skill_rect7 = pygame.Rect(20, 395, 50, 50)
        self.skill_rect8 = pygame.Rect(20, 450, 50, 50)
        self.skill_rect9 = pygame.Rect(85, 230, 105, 105)

    def calculate_multiplier(self, owned):
        if owned >= 150:
            return FormattedNumber(32)
        elif owned >= 100:
            return FormattedNumber(16)
        elif owned >= 50:
            return FormattedNumber(8)
        elif owned >= 25:
            return FormattedNumber(4)
        elif owned >= 10:
            return FormattedNumber(2)
        else:
            return FormattedNumber(1)

    def recalculate_upgrade_costs(self):
        # Recalculate the costs of all upgrades based on the number owned
        self.upgrade_0_cost.value = self.upgrade_0_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_0_owned.value))
        self.upgrade_0_increase.value = self.upgrade_0_base_increase.value * self.upgrade_0_current_multiplier.value
        self.upgrade_1_cost.value = self.upgrade_1_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_1_owned.value))
        self.upgrade_1_increase.value = self.upgrade_1_base_increase.value * self.upgrade_1_current_multiplier.value
        self.upgrade_2_cost.value = self.upgrade_2_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_2_owned.value))
        self.upgrade_2_increase.value = self.upgrade_2_base_increase.value * self.upgrade_2_current_multiplier.value
        self.upgrade_3_cost.value = self.upgrade_3_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_3_owned.value))
        self.upgrade_3_increase.value = self.upgrade_3_base_increase.value * self.upgrade_3_current_multiplier.value
        self.upgrade_4_cost.value = self.upgrade_4_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_4_owned.value))
        self.upgrade_4_increase.value = self.upgrade_4_base_increase.value * self.upgrade_4_current_multiplier.value
        self.upgrade_5_cost.value = self.upgrade_5_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_5_owned.value))
        self.upgrade_5_increase.value = self.upgrade_5_base_increase.value * self.upgrade_5_current_multiplier.value
        self.upgrade_6_cost.value = self.upgrade_6_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_6_owned.value))
        self.upgrade_6_increase.value = self.upgrade_6_base_increase.value * self.upgrade_6_current_multiplier.value
        self.upgrade_7_cost.value = self.upgrade_7_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_7_owned.value))
        self.upgrade_7_increase.value = self.upgrade_7_base_increase.value * self.upgrade_7_current_multiplier.value

    def buy_upgrade_0(self):
        if self.balance >= self.upgrade_0_cost:
            self.balance -= self.upgrade_0_cost
            self.balance_per_second += self.upgrade_0_increase
            self.upgrade_0_current_bps += self.upgrade_0_increase
            self.upgrade_0_cost.value = self.upgrade_0_initial_cost.value * (
                    (1 + 0.15) ** (self.upgrade_0_owned.value + 1))
            self.upgrade_0_owned += 1
            if self.upgrade_0_owned == 10:
                self.click_multiplier.value *= 2
                self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_0_current_bps.value + (
                        self.upgrade_0_current_bps.value * 2)
                self.upgrade_0_current_bps.value = self.upgrade_0_increase.value * 2
                self.upgrade_0_increase.value *= 2
                self.upgrade_0_current_multiplier.value = 2
            if self.upgrade_0_owned == 25:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_0_current_bps.value + (
                        self.upgrade_0_current_bps.value * 4)
                self.upgrade_0_current_bps.value = self.upgrade_0_increase.value * 4
                self.upgrade_0_increase.value *= 4
                self.upgrade_0_current_multiplier.value = 4
            if self.upgrade_0_owned == 50:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_0_current_bps.value + (
                        self.upgrade_0_current_bps.value * 8)
                self.upgrade_0_current_bps.value = self.upgrade_0_increase.value * 8
                self.upgrade_0_increase.value *= 2
                self.upgrade_0_current_multiplier.value = 8
            if self.upgrade_0_owned == 100:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_0_current_bps.value + (
                        self.upgrade_0_current_bps.value * 16)
                self.upgrade_0_current_bps.value = self.upgrade_0_increase.value * 16
                self.click_multiplier.value *= 2
                self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                self.upgrade_0_increase.value *= 2
                self.upgrade_0_current_multiplier.value = 16
            if self.upgrade_0_owned == 150:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_0_current_bps.value + (
                        self.upgrade_0_current_bps.value * 32)
                self.upgrade_0_current_bps.value = self.upgrade_0_increase.value * 32
                self.upgrade_0_increase.value *= 2
                self.upgrade_0_current_multiplier.value = 32
            print(
                f"Frying Pan bought! You own {self.upgrade_0_owned.value} Frying Pans. "
                f"Next one costs {self.upgrade_0_cost.formatted()}!")
        else:
            print("Not enough balance to buy a frying pan")

    def buy_upgrade_1(self):
        if self.upgrade_0_owned >= 1:
            if self.balance >= self.upgrade_1_cost:
                self.balance -= self.upgrade_1_cost
                self.balance_per_second += self.upgrade_1_increase
                self.upgrade_1_current_bps += self.upgrade_1_increase
                self.upgrade_1_cost.value = self.upgrade_1_initial_cost.value * (
                        (1 + 0.15) ** (self.upgrade_1_owned.value + 1))
                self.upgrade_1_owned += 1
                if self.upgrade_1_owned == 10:
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_1_current_bps.value + (
                            self.upgrade_1_current_bps.value * 2)
                    self.upgrade_1_current_bps.value = self.upgrade_1_increase.value * 2
                    self.upgrade_1_increase.value *= 2
                    self.upgrade_1_current_multiplier.value = 2
                if self.upgrade_1_owned == 25:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_1_current_bps.value + (
                            self.upgrade_1_current_bps.value * 4)
                    self.upgrade_1_current_bps.value = self.upgrade_1_increase.value * 4
                    self.upgrade_1_increase.value *= 2
                    self.upgrade_1_current_multiplier.value = 4
                if self.upgrade_1_owned == 50:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_1_current_bps.value + (
                            self.upgrade_1_current_bps.value * 8)
                    self.upgrade_1_current_bps.value = self.upgrade_1_increase.value * 8
                    self.upgrade_1_increase.value *= 2
                    self.upgrade_1_current_multiplier.value = 8
                if self.upgrade_1_owned == 100:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_1_current_bps.value + (
                            self.upgrade_1_current_bps.value * 16)
                    self.upgrade_1_current_bps.value = self.upgrade_1_increase.value * 16
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.upgrade_1_increase.value *= 2
                    self.upgrade_1_current_multiplier.value = 16
                if self.upgrade_1_owned == 150:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_1_current_bps.value + (
                            self.upgrade_1_current_bps.value * 32)
                    self.upgrade_1_current_bps.value = self.upgrade_1_increase.value * 32
                    self.upgrade_1_increase.value *= 2
                    self.upgrade_1_current_multiplier.value = 32
                print(
                    f"Pig bought! You own {self.upgrade_1_owned.value} Pigs. "
                    f"Next one costs {self.upgrade_1_cost.formatted()}!")
            else:
                print("Not enough balance to buy a upgrade_1")

    def buy_upgrade_2(self):
        if self.upgrade_1_owned >= 1:
            if self.balance >= self.upgrade_2_cost:
                self.balance -= self.upgrade_2_cost
                self.balance_per_second += self.upgrade_2_increase
                self.upgrade_2_current_bps += self.upgrade_2_increase
                self.upgrade_2_cost.value = self.upgrade_2_initial_cost.value * (
                        (1 + 0.15) ** (self.upgrade_2_owned.value + 1))
                self.upgrade_2_owned += 1
                if self.upgrade_2_owned == 10:
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_2_current_bps.value + (
                            self.upgrade_2_current_bps.value * 2)
                    self.upgrade_2_current_bps.value = self.upgrade_2_increase.value * 2
                    self.upgrade_2_increase.value *= 2
                    self.upgrade_2_current_multiplier.value = 2
                if self.upgrade_2_owned == 25:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_2_current_bps.value + (
                            self.upgrade_2_current_bps.value * 4)
                    self.upgrade_2_current_bps.value = self.upgrade_2_increase.value * 4
                    self.upgrade_2_increase.value *= 2
                    self.upgrade_2_current_multiplier.value = 4
                if self.upgrade_2_owned == 50:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_2_current_bps.value + (
                            self.upgrade_2_current_bps.value * 8)
                    self.upgrade_2_current_bps.value = self.upgrade_2_increase.value * 8
                    self.upgrade_2_increase.value *= 2
                    self.upgrade_2_current_multiplier.value = 8
                if self.upgrade_2_owned == 100:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_2_current_bps.value + (
                            self.upgrade_2_current_bps.value * 16)
                    self.upgrade_2_current_bps.value = self.upgrade_2_increase.value * 16
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.upgrade_2_increase.value *= 2
                    self.upgrade_2_current_multiplier.value = 16
                if self.upgrade_2_owned == 150:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_2_current_bps.value + (
                            self.upgrade_2_current_bps.value * 32)
                    self.upgrade_2_current_bps.value = self.upgrade_2_increase.value * 32
                    self.upgrade_2_increase.value *= 2
                    self.upgrade_2_current_multiplier.value = 32
                print(
                    f"Upgrade 2 bought! You own {self.upgrade_2_owned.value} Upgrade 2. "
                    f"Next one costs {self.upgrade_2_cost.formatted()}!")
            else:
                print("Not enough balance to buy a upgrade_2")

    def buy_upgrade_3(self):
        if self.upgrade_2_owned >= 1:
            if self.balance >= self.upgrade_3_cost:
                self.balance -= self.upgrade_3_cost
                self.balance_per_second += self.upgrade_3_increase
                self.upgrade_3_current_bps += self.upgrade_3_increase
                self.upgrade_3_cost.value = self.upgrade_3_initial_cost.value * (
                        (1 + 0.15) ** (self.upgrade_3_owned.value + 1))
                self.upgrade_3_owned += 1
                if self.upgrade_3_owned == 10:
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_3_current_bps.value + (
                            self.upgrade_3_current_bps.value * 2)
                    self.upgrade_3_current_bps.value = self.upgrade_3_increase.value * 2
                    self.upgrade_3_increase.value *= 2
                    self.upgrade_3_current_multiplier.value = 2
                if self.upgrade_3_owned == 25:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_3_current_bps.value + (
                            self.upgrade_3_current_bps.value * 4)
                    self.upgrade_3_current_bps.value = self.upgrade_3_increase.value * 4
                    self.upgrade_3_increase.value *= 2
                    self.upgrade_3_current_multiplier.value = 4
                if self.upgrade_3_owned == 50:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_3_current_bps.value + (
                            self.upgrade_3_current_bps.value * 8)
                    self.upgrade_3_current_bps.value = self.upgrade_3_increase.value * 8
                    self.upgrade_3_increase.value *= 2
                    self.upgrade_3_current_multiplier.value = 8
                if self.upgrade_3_owned == 100:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_3_current_bps.value + (
                            self.upgrade_3_current_bps.value * 16)
                    self.upgrade_3_current_bps.value = self.upgrade_3_increase.value * 16
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.upgrade_3_increase.value *= 2
                    self.upgrade_3_current_multiplier.value = 16
                if self.upgrade_3_owned == 150:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_3_current_bps.value + (
                            self.upgrade_3_current_bps.value * 32)
                    self.upgrade_3_current_bps.value = self.upgrade_3_increase.value * 32
                    self.upgrade_3_increase.value *= 2
                    self.upgrade_3_current_multiplier.value = 32
                print(
                    f"Silver bacon bought! You own {self.upgrade_3_owned.value} silver bacon. "
                    f"Next one costs {self.upgrade_3_cost.formatted()}!")
            else:
                print("Not enough balance to buy a silver bacon")

    def buy_upgrade_4(self):
        if self.upgrade_3_owned >= 1:
            if self.balance >= self.upgrade_4_cost:
                self.balance -= self.upgrade_4_cost
                self.balance_per_second += self.upgrade_4_increase
                self.upgrade_4_current_bps += self.upgrade_4_increase
                self.upgrade_4_cost.value = self.upgrade_4_initial_cost.value * (
                        (1 + 0.15) ** (self.upgrade_4_owned.value + 1))
                self.upgrade_4_owned += 1
                if self.upgrade_4_owned == 10:
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_4_current_bps.value + (
                            self.upgrade_4_current_bps.value * 2)
                    self.upgrade_4_current_bps.value = self.upgrade_4_increase.value * 2
                    self.upgrade_4_increase.value *= 2
                    self.upgrade_4_current_multiplier.value = 2
                if self.upgrade_4_owned == 25:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_4_current_bps.value + (
                            self.upgrade_4_current_bps.value * 4)
                    self.upgrade_4_current_bps.value = self.upgrade_4_increase.value * 4
                    self.upgrade_4_increase.value *= 2
                    self.upgrade_4_current_multiplier.value = 4
                if self.upgrade_4_owned == 50:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_4_current_bps.value + (
                            self.upgrade_4_current_bps.value * 8)
                    self.upgrade_4_current_bps.value = self.upgrade_4_increase.value * 8
                    self.upgrade_4_increase.value *= 2
                    self.upgrade_4_current_multiplier.value = 8
                if self.upgrade_4_owned == 100:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_4_current_bps.value + (
                            self.upgrade_4_current_bps.value * 16)
                    self.upgrade_4_current_bps.value = self.upgrade_4_increase.value * 16
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.upgrade_4_increase.value *= 2
                    self.upgrade_4_current_multiplier.value = 16
                if self.upgrade_4_owned == 150:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_4_current_bps.value + (
                            self.upgrade_4_current_bps.value * 32)
                    self.upgrade_4_current_bps.value = self.upgrade_4_increase.value * 32
                    self.upgrade_4_increase.value *= 2
                    self.upgrade_4_current_multiplier.value = 32
                print(
                    f"Golden bacon bought! You own {self.upgrade_4_owned.value} golden bacon. "
                    f"Next one costs {self.upgrade_4_cost.formatted()}!")
            else:
                print("Not enough balance to buy a upgrade_4")

    def buy_upgrade_5(self):
        if self.upgrade_4_owned >= 1:
            if self.balance >= self.upgrade_5_cost:
                self.balance -= self.upgrade_5_cost
                self.balance_per_second += self.upgrade_5_increase
                self.upgrade_5_current_bps += self.upgrade_5_increase
                self.upgrade_5_cost.value = self.upgrade_5_initial_cost.value * (
                        (1 + 0.15) ** (self.upgrade_5_owned.value + 1))
                self.upgrade_5_owned += 1
                if self.upgrade_5_owned == 10:
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_5_current_bps.value + (
                            self.upgrade_5_current_bps.value * 2)
                    self.upgrade_5_current_bps.value = self.upgrade_5_increase.value * 2
                    self.upgrade_5_increase.value *= 2
                    self.upgrade_5_current_multiplier.value = 2
                if self.upgrade_5_owned == 25:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_5_current_bps.value + (
                            self.upgrade_5_current_bps.value * 4)
                    self.upgrade_5_current_bps.value = self.upgrade_5_increase.value * 4
                    self.upgrade_5_increase.value *= 2
                    self.upgrade_5_current_multiplier.value = 4
                if self.upgrade_5_owned == 50:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_5_current_bps.value + (
                            self.upgrade_5_current_bps.value * 8)
                    self.upgrade_5_current_bps.value = self.upgrade_5_increase.value * 8
                    self.upgrade_5_increase.value *= 2
                    self.upgrade_5_current_multiplier.value = 8
                if self.upgrade_5_owned == 100:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_5_current_bps.value + (
                            self.upgrade_5_current_bps.value * 16)
                    self.upgrade_5_current_bps.value = self.upgrade_5_increase.value * 16
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.upgrade_5_increase.value *= 2
                    self.upgrade_5_current_multiplier.value = 16
                if self.upgrade_5_owned == 150:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_5_current_bps.value + (
                            self.upgrade_5_current_bps.value * 32)
                    self.upgrade_5_current_bps.value = self.upgrade_5_increase.value * 32
                    self.upgrade_5_increase.value *= 2
                    self.upgrade_5_current_multiplier.value = 32
                print(
                    f"Upgrade 6 bought! You own {self.upgrade_5_owned.value} upgrade 6. "
                    f"Next one costs {self.upgrade_5_cost.formatted()}!")
            else:
                print("Not enough balance to buy an upgrade 6")

    def buy_upgrade_6(self):
        if self.upgrade_5_owned >= 1:
            if self.balance >= self.upgrade_6_cost:
                self.balance -= self.upgrade_6_cost
                self.balance_per_second += self.upgrade_6_increase
                self.upgrade_6_current_bps += self.upgrade_6_increase
                self.upgrade_6_cost.value = self.upgrade_6_initial_cost.value * (
                        (1 + 0.15) ** (self.upgrade_6_owned.value + 1))
                self.upgrade_6_owned += 1
                if self.upgrade_6_owned == 10:
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_6_current_bps.value + (
                            self.upgrade_6_current_bps.value * 2)
                    self.upgrade_6_current_bps.value = self.upgrade_6_increase.value * 2
                    self.upgrade_6_increase.value *= 2
                    self.upgrade_6_current_multiplier.value = 2
                if self.upgrade_6_owned == 25:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_6_current_bps.value + (
                            self.upgrade_6_current_bps.value * 4)
                    self.upgrade_6_current_bps.value = self.upgrade_6_increase.value * 4
                    self.upgrade_6_increase.value *= 2
                    self.upgrade_6_current_multiplier.value = 4
                if self.upgrade_6_owned == 50:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_6_current_bps.value + (
                            self.upgrade_6_current_bps.value * 8)
                    self.upgrade_6_current_bps.value = self.upgrade_6_increase.value * 8
                    self.upgrade_6_increase.value *= 2
                    self.upgrade_6_current_multiplier.value = 8
                if self.upgrade_6_owned == 100:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_6_current_bps.value + (
                            self.upgrade_6_current_bps.value * 16)
                    self.upgrade_6_current_bps.value = self.upgrade_6_increase.value * 16
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.upgrade_6_increase.value *= 2
                    self.upgrade_6_current_multiplier.value = 16
                if self.upgrade_6_owned == 150:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_6_current_bps.value + (
                            self.upgrade_6_current_bps.value * 32)
                    self.upgrade_6_current_bps.value = self.upgrade_6_increase.value * 32
                    self.upgrade_6_increase.value *= 2
                    self.upgrade_6_current_multiplier.value = 32
                print(
                    f"Upgrade 7 bought! You own {self.upgrade_6_owned.value} upgrade 7. "
                    f"Next one costs {self.upgrade_6_cost.formatted()}!")
            else:
                print("Not enough balance to buy an upgrade 7")

    def buy_upgrade_7(self):
        if self.upgrade_6_owned >= 1:
            if self.balance >= self.upgrade_7_cost:
                self.balance -= self.upgrade_7_cost
                self.balance_per_second += self.upgrade_7_increase
                self.upgrade_7_current_bps += self.upgrade_7_increase
                self.upgrade_7_cost.value = self.upgrade_7_initial_cost.value * (
                        (1 + 0.15) ** (self.upgrade_7_owned.value + 1))
                self.upgrade_7_owned += 1
                if self.upgrade_7_owned == 10:
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_7_current_bps.value + (
                            self.upgrade_7_current_bps.value * 2)
                    self.upgrade_7_current_bps.value = self.upgrade_7_increase.value * 2
                    self.upgrade_7_increase.value *= 2
                    self.upgrade_7_current_multiplier.value = 2
                if self.upgrade_7_owned == 25:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_7_current_bps.value + (
                            self.upgrade_7_current_bps.value * 4)
                    self.upgrade_7_current_bps.value = self.upgrade_7_increase.value * 4
                    self.upgrade_7_increase.value *= 2
                    self.upgrade_7_current_multiplier.value = 4
                if self.upgrade_7_owned == 50:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_7_current_bps.value + (
                            self.upgrade_7_current_bps.value * 8)
                    self.upgrade_7_current_bps.value = self.upgrade_7_increase.value * 8
                    self.upgrade_7_increase.value *= 2
                    self.upgrade_7_current_multiplier.value = 8
                if self.upgrade_7_owned == 100:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_7_current_bps.value + (
                            self.upgrade_7_current_bps.value * 16)
                    self.upgrade_7_current_bps.value = self.upgrade_7_increase.value * 16
                    self.click_multiplier.value *= 2
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    self.upgrade_7_increase.value *= 2
                    self.upgrade_7_current_multiplier.value = 16
                if self.upgrade_7_owned == 150:
                    self.balance_per_second.value = self.balance_per_second.value - self.upgrade_7_current_bps.value + (
                            self.upgrade_7_current_bps.value * 32)
                    self.upgrade_7_current_bps.value = self.upgrade_7_increase.value * 32
                    self.upgrade_7_increase.value *= 2
                    self.upgrade_7_current_multiplier.value = 32
                print(
                    f"Upgrade 8 bought! You own {self.upgrade_7_owned.value} upgrade 8. "
                    f"Next one costs {self.upgrade_7_cost.formatted()}!")
            else:
                print("Not enough balance to buy an upgrade 8")
