from format_numbers import FormattedNumber


class Upgrades:
    def __init__(self, pygame):
        self.upgrade_1_owned = FormattedNumber(0)
        self.upgrade_1_initial_cost = FormattedNumber(15)
        self.upgrade_1_cost = FormattedNumber(15)
        self.upgrade_1_base_increase = FormattedNumber(.2)
        self.upgrade_1_increase = FormattedNumber(.2)
        self.upgrade_1_current_bps = FormattedNumber(0)
        self.upgrade_1_current_multiplier = self.calculate_multiplier(self.upgrade_1_owned.value)

        self.upgrade_2_owned = FormattedNumber(0)
        self.upgrade_2_initial_cost = FormattedNumber(100)
        self.upgrade_2_cost = FormattedNumber(100)
        self.upgrade_2_base_increase = FormattedNumber(1)
        self.upgrade_2_increase = FormattedNumber(1)
        self.upgrade_2_current_bps = FormattedNumber(0)
        self.upgrade_2_current_multiplier = self.calculate_multiplier(self.upgrade_2_owned.value)

        self.upgrade_3_owned = FormattedNumber(0)
        self.upgrade_3_initial_cost = FormattedNumber(500)
        self.upgrade_3_cost = FormattedNumber(500)
        self.upgrade_3_base_increase = FormattedNumber(8)
        self.upgrade_3_increase = FormattedNumber(8)
        self.upgrade_3_current_bps = FormattedNumber(0)
        self.upgrade_3_current_multiplier = self.calculate_multiplier(self.upgrade_3_owned.value)

        self.upgrade_4_owned = FormattedNumber(0)
        self.upgrade_4_initial_cost = FormattedNumber(3000)
        self.upgrade_4_cost = FormattedNumber(3000)
        self.upgrade_4_base_increase = FormattedNumber(20)
        self.upgrade_4_increase = FormattedNumber(20)
        self.upgrade_4_current_bps = FormattedNumber(0)
        self.upgrade_4_current_multiplier = self.calculate_multiplier(self.upgrade_4_owned.value)

        self.upgrade_5_owned = FormattedNumber(0)
        self.upgrade_5_initial_cost = FormattedNumber(15000)
        self.upgrade_5_cost = FormattedNumber(15000)
        self.upgrade_5_base_increase = FormattedNumber(80)
        self.upgrade_5_increase = FormattedNumber(80)
        self.upgrade_5_current_bps = FormattedNumber(0)
        self.upgrade_5_current_multiplier = self.calculate_multiplier(self.upgrade_5_owned.value)

        self.upgrade_6_owned = FormattedNumber(0)
        self.upgrade_6_initial_cost = FormattedNumber(100000)
        self.upgrade_6_cost = FormattedNumber(100000)
        self.upgrade_6_base_increase = FormattedNumber(500)
        self.upgrade_6_increase = FormattedNumber(500)
        self.upgrade_6_current_bps = FormattedNumber(0)
        self.upgrade_6_current_multiplier = self.calculate_multiplier(self.upgrade_6_owned.value)

        self.upgrade_7_owned = FormattedNumber(0)
        self.upgrade_7_initial_cost = FormattedNumber(500000)
        self.upgrade_7_cost = FormattedNumber(500000)
        self.upgrade_7_base_increase = FormattedNumber(3000)
        self.upgrade_7_increase = FormattedNumber(3000)
        self.upgrade_7_current_bps = FormattedNumber(0)
        self.upgrade_7_current_multiplier = self.calculate_multiplier(self.upgrade_7_owned.value)

        self.upgrade_8_owned = FormattedNumber(0)
        self.upgrade_8_initial_cost = FormattedNumber(2500000)
        self.upgrade_8_cost = FormattedNumber(2500000)
        self.upgrade_8_base_increase = FormattedNumber(10000)
        self.upgrade_8_increase = FormattedNumber(10000)
        self.upgrade_8_current_bps = FormattedNumber(0)
        self.upgrade_8_current_multiplier = self.calculate_multiplier(self.upgrade_8_owned.value)

        # Calculating multiplier
        upgrades = [
            self.upgrade_1_owned, self.upgrade_2_owned, self.upgrade_3_owned,
            self.upgrade_4_owned, self.upgrade_5_owned, self.upgrade_6_owned,
            self.upgrade_7_owned, self.upgrade_8_owned
        ]

        for i, upgrade in enumerate(upgrades):  # TODO NOT WORKING but overall it does
            setattr(self, f"upgrade_{i+1}_current_multiplier", self.calculate_multiplier(upgrade))
            print(f"Upgrade {i+1} multiplier: {getattr(self, f'upgrade_{i+1}_current_multiplier').value}")

        # self.recalculate_upgrade_costs()

        self.balance = FormattedNumber(500000000000000000000000)
        self.initial_click_rate = FormattedNumber(1)
        self.click_rate = FormattedNumber(1)
        self.click_multiplier = FormattedNumber(1)
        self.total_clicks = FormattedNumber(0)
        self.balance_per_second = FormattedNumber(
            0.00 + (self.upgrade_1_owned.value * self.upgrade_1_base_increase.value) *
            self.upgrade_1_current_multiplier.value +
            (
                    self.upgrade_2_owned.value * self.upgrade_2_base_increase.value) * self.upgrade_2_current_multiplier.value + (
                    self.upgrade_3_owned.value * self.upgrade_3_base_increase.value) * self.upgrade_3_current_multiplier.value + (
                    self.upgrade_4_owned.value * self.upgrade_4_base_increase.value) * self.upgrade_4_current_multiplier.value + (
                    self.upgrade_5_owned.value * self.upgrade_5_base_increase.value) * self.upgrade_5_current_multiplier.value + (
                    self.upgrade_6_owned.value * self.upgrade_6_base_increase.value) * self.upgrade_6_current_multiplier.value + (
                    self.upgrade_7_owned.value * self.upgrade_7_base_increase.value) * self.upgrade_7_current_multiplier.value + (
                    self.upgrade_8_owned.value * self.upgrade_8_base_increase.value) * self.upgrade_8_current_multiplier.value)

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
        if owned >= 1000:
            return FormattedNumber(2 ** 14)  # Multiplier for 1000
        elif owned >= 900:
            return FormattedNumber(2 ** 13)  # Multiplier for 900
        elif owned >= 800:
            return FormattedNumber(2 ** 12)  # Multiplier for 800
        elif owned >= 700:
            return FormattedNumber(2 ** 11)  # Multiplier for 700
        elif owned >= 600:
            return FormattedNumber(2 ** 10)  # Multiplier for 600
        elif owned >= 500:
            return FormattedNumber(2 ** 9)  # Multiplier for 500
        elif owned >= 400:
            return FormattedNumber(2 ** 8)  # Multiplier for 400
        elif owned >= 300:
            return FormattedNumber(2 ** 7)  # Multiplier for 300
        elif owned >= 200:
            return FormattedNumber(2 ** 6)  # Multiplier for 200
        elif owned >= 150:
            return FormattedNumber(2 ** 5)  # Multiplier for 150
        elif owned >= 100:
            return FormattedNumber(2 ** 4)  # Multiplier for 100
        elif owned >= 50:
            return FormattedNumber(2 ** 3)  # Multiplier for 50
        elif owned >= 25:
            return FormattedNumber(2 ** 2)  # Multiplier for 25
        elif owned >= 10:
            return FormattedNumber(2)  # Multiplier for 10
        else:
            return FormattedNumber(1)  # Default multiplier


    def recalculate_upgrade_costs(self):
        # Recalculate the costs of all upgrades based on the number owned
        self.upgrade_1_cost.value = self.upgrade_1_initial_cost.value * (
                (1 + 0.15) ** self.upgrade_1_owned.value)
        self.upgrade_1_increase.value = self.upgrade_1_base_increase.value * self.upgrade_1_current_multiplier.value
        self.upgrade_2_cost.value = self.upgrade_2_initial_cost.value * (
                (1 + 0.15) ** self.upgrade_2_owned.value)
        self.upgrade_2_increase.value = self.upgrade_2_base_increase.value * self.upgrade_2_current_multiplier.value
        self.upgrade_3_cost.value = self.upgrade_3_initial_cost.value * (
                (1 + 0.15) ** self.upgrade_3_owned.value)
        self.upgrade_3_increase.value = self.upgrade_3_base_increase.value * self.upgrade_3_current_multiplier.value
        self.upgrade_4_cost.value = self.upgrade_4_initial_cost.value * (
                (1 + 0.15) ** self.upgrade_4_owned.value)
        self.upgrade_4_increase.value = self.upgrade_4_base_increase.value * self.upgrade_4_current_multiplier.value
        self.upgrade_5_cost.value = self.upgrade_5_initial_cost.value * (
                (1 + 0.15) ** self.upgrade_5_owned.value)
        self.upgrade_5_increase.value = self.upgrade_5_base_increase.value * self.upgrade_5_current_multiplier.value
        self.upgrade_6_cost.value = self.upgrade_6_initial_cost.value * (
                (1 + 0.15) ** self.upgrade_6_owned.value)
        self.upgrade_6_increase.value = self.upgrade_6_base_increase.value * self.upgrade_6_current_multiplier.value
        self.upgrade_7_cost.value = self.upgrade_7_initial_cost.value * (
                (1 + 0.15) ** self.upgrade_7_owned.value)
        self.upgrade_7_increase.value = self.upgrade_7_base_increase.value * self.upgrade_7_current_multiplier.value
        self.upgrade_8_cost.value = self.upgrade_8_initial_cost.value * (
                (1 + 0.15) ** self.upgrade_8_owned.value)
        self.upgrade_8_increase.value = self.upgrade_8_base_increase.value * self.upgrade_8_current_multiplier.value

    def buy_upgrade(self, upgrade_number):
        owned_attr = f'upgrade_{upgrade_number}_owned'
        cost_attr = f'upgrade_{upgrade_number}_cost'
        increase_attr = f'upgrade_{upgrade_number}_increase'
        current_bps_attr = f'upgrade_{upgrade_number}_current_bps'
        initial_cost_attr = f'upgrade_{upgrade_number}_initial_cost'
        current_multiplier_attr = f'upgrade_{upgrade_number}_current_multiplier'

        # Check if the upgrade attributes exist
        if hasattr(self, owned_attr) and hasattr(self, cost_attr) and hasattr(self, increase_attr):
            owned = getattr(self, owned_attr)
            cost = getattr(self, cost_attr)
            increase = getattr(self, increase_attr)
            current_bps = getattr(self, current_bps_attr)
            initial_cost = getattr(self, initial_cost_attr)
            current_multiplier = getattr(self, current_multiplier_attr)

            # Check if the previous upgrade is owned or if it's the first upgrade
            if upgrade_number == 1 or getattr(self, f'upgrade_{upgrade_number - 1}_owned').value >= 1:
                if self.balance.value >= cost.value:
                    # Upgrade purchase logic
                    self.balance.value -= cost.value
                    self.balance_per_second.value += increase.value
                    current_bps.value += increase.value
                    cost.value = initial_cost.value * ((1 + 0.15) ** (owned.value + 1))
                    owned.value += 1

                    # Special conditions for multipliers at certain levels
                    if owned.value in [10, 25, 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
                        if owned.value == 1000:
                            multiplier = 2 ** 14  # 2^14 für 1000
                        elif owned.value == 900:
                            multiplier = 2 ** 13  # 2^13 für 900
                        elif owned.value == 800:
                            multiplier = 2 ** 12  # 2^12 für 800
                        elif owned.value == 700:
                            multiplier = 2 ** 11  # 2^11 für 700
                        elif owned.value == 600:
                            multiplier = 2 ** 10  # 2^10 für 600
                        elif owned.value == 500:
                            multiplier = 2 ** 9  # 2^9 für 500
                        elif owned.value == 400:
                            multiplier = 2 ** 8  # 2^8 für 400
                        elif owned.value == 300:
                            multiplier = 2 ** 7  # 2^7 für 300
                        elif owned.value == 200:
                            multiplier = 2 ** 6  # 2^6 für 200
                        elif owned.value == 150:
                            multiplier = 2 ** 5  # 2^5 für 150
                        elif owned.value == 100:
                            multiplier = 2 ** 4  # 2^4 für 100
                        elif owned.value == 50:
                            multiplier = 2 ** 3  # 2^3 für 50
                        elif owned.value == 25:
                            multiplier = 2 ** 2  # 2^2 für 25
                        elif owned.value == 10:
                            multiplier = 2  # 2^1 für 10
                    else:
                        multiplier = 1
                    print(multiplier)
                    if self.total_clicks.value >= 50:
                        self.click_rate.value = int(
                            self.total_clicks.value / 50) * self.click_multiplier.value * multiplier
                    else:
                        self.click_rate.value = self.click_multiplier.value * multiplier
                    print(self.click_multiplier.value)
                    self.click_multiplier.value = self.click_multiplier.value * multiplier
                    current_multiplier.value = multiplier
                    print(self.click_multiplier.value)
                    increase.value = increase.value * multiplier
                    current_bps.value = current_bps.value * multiplier
                    current_multiplier.value = multiplier

                    self.balance_per_second.value = self.balance_per_second.value - (current_bps.value / multiplier) + current_bps.value

                    print(
                        f"Multiplier applied! New click rate: {self.click_rate.formatted()}, Upgrade {upgrade_number} BPS: {current_bps.formatted()}")

                    print(
                        f"Upgrade {upgrade_number} bought! You now own {owned.formatted()}. Next one costs {cost.formatted()}!")
                else:
                    print(f"Not enough balance to buy Upgrade {upgrade_number}")
            else:
                print(f"Cannot buy Upgrade {upgrade_number}: prerequisite not met.")
        else:
            print(f"Upgrade {upgrade_number} does not exist.")


