# Scrolling Background (init)
self.b_pos = 0
self.o_pos = 720
self.speed = 0.2

# Scrolling Background (draw)
        # if self.b_pos <= -self.height:
        #     self.b_pos = self.height
        # if self.o_pos <= -self.height:
        #     self.o_pos = self.height
        #
        # self.b_pos -= self.speed
        # self.o_pos -= self.speed
        # self.screen.blit(images.background, (0, self.b_pos))
        # self.screen.blit(images.overlap, (0, self.o_pos))



# Skill Buttons (draw)
# Skill Buttons
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
                                                    assets.black, pygame)

# Iwas mit Button creator, scheint redundant, (draw über button creation)
# if upgrades.upgrade_0_owned.value >= 1:
        #     self.button_creator.create_button(upgrades.buy_upgrade_1_button_rect, (209, 50, 36), "Upgrade 1",
        #                                       upgrades.upgrade_1_cost, upgrades.upgrade_1_increase,
        #                                       upgrades.upgrade_1_owned, images.upgrade_1_upgrade, pygame, upgrades,
        #                                       images)



# alte buy funktionen
def buy_upgrade_0(self):
    if self.balance >= self.upgrade_1_cost:
        self.balance -= self.upgrade_1_cost
        self.balance_per_second += self.upgrade_1_increase
        self.upgrade_1_current_bps += self.upgrade_1_increase
        self.upgrade_1_cost.value = self.upgrade_1_initial_cost.value * (
                (1 + 0.15) ** (self.upgrade_1_owned.value + 1))
        self.upgrade_1_owned += 1
        if self.upgrade_1_owned == 10:
            self.click_multiplier.value *= 2
            if self.total_clicks.value >= 50:
                self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
            else:
                self.click_rate.value = 1 * self.click_multiplier.value
            self.balance_per_second.value = self.balance_per_second.value - self.upgrade_1_current_bps.value + (
                    self.upgrade_1_current_bps.value * 2)
            self.upgrade_1_current_bps.value = self.upgrade_1_increase.value * 2
            self.upgrade_1_increase.value *= 2
            self.upgrade_1_current_multiplier.value = 2
        if self.upgrade_1_owned == 25:
            self.balance_per_second.value = self.balance_per_second.value - self.upgrade_1_current_bps.value + (
                    self.upgrade_1_current_bps.value * 4)
            self.upgrade_1_current_bps.value = self.upgrade_1_increase.value * 4
            self.upgrade_1_increase.value *= 4
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
            f"Frying Pan bought! You own {self.upgrade_1_owned.value} Frying Pans. "
            f"Next one costs {self.upgrade_1_cost.formatted()}!")
    else:
        print("Not enough balance to buy a frying pan")


def buy_upgrade_1(self):
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
                self.upgrade_2_increase.value *= 2
                self.upgrade_2_current_multiplier.value = 16
            if self.upgrade_2_owned == 150:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_2_current_bps.value + (
                        self.upgrade_2_current_bps.value * 32)
                self.upgrade_2_current_bps.value = self.upgrade_2_increase.value * 32
                self.upgrade_2_increase.value *= 2
                self.upgrade_2_current_multiplier.value = 32
            print(
                f"Pig bought! You own {self.upgrade_2_owned.value} Pigs. "
                f"Next one costs {self.upgrade_2_cost.formatted()}!")
        else:
            print("Not enough balance to buy a upgrade_1")


def buy_upgrade_2(self):
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
                if self.total_clicks.value >= 50:
                    if self.total_clicks.value >= 50:
                        self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                    else:
                        self.click_rate.value = 1 * self.click_multiplier.value
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
                self.upgrade_3_increase.value *= 2
                self.upgrade_3_current_multiplier.value = 16
            if self.upgrade_3_owned == 150:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_3_current_bps.value + (
                        self.upgrade_3_current_bps.value * 32)
                self.upgrade_3_current_bps.value = self.upgrade_3_increase.value * 32
                self.upgrade_3_increase.value *= 2
                self.upgrade_3_current_multiplier.value = 32
            print(
                f"Upgrade 2 bought! You own {self.upgrade_3_owned.value} Upgrade 2. "
                f"Next one costs {self.upgrade_3_cost.formatted()}!")
        else:
            print("Not enough balance to buy a upgrade_2")


def buy_upgrade_3(self):
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
                self.upgrade_4_increase.value *= 2
                self.upgrade_4_current_multiplier.value = 16
            if self.upgrade_4_owned == 150:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_4_current_bps.value + (
                        self.upgrade_4_current_bps.value * 32)
                self.upgrade_4_current_bps.value = self.upgrade_4_increase.value * 32
                self.upgrade_4_increase.value *= 2
                self.upgrade_4_current_multiplier.value = 32
            print(
                f"Silver bacon bought! You own {self.upgrade_4_owned.value} silver bacon. "
                f"Next one costs {self.upgrade_4_cost.formatted()}!")
        else:
            print("Not enough balance to buy a silver bacon")


def buy_upgrade_4(self):
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
                self.upgrade_5_increase.value *= 2
                self.upgrade_5_current_multiplier.value = 16
            if self.upgrade_5_owned == 150:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_5_current_bps.value + (
                        self.upgrade_5_current_bps.value * 32)
                self.upgrade_5_current_bps.value = self.upgrade_5_increase.value * 32
                self.upgrade_5_increase.value *= 2
                self.upgrade_5_current_multiplier.value = 32
            print(
                f"Golden bacon bought! You own {self.upgrade_5_owned.value} golden bacon. "
                f"Next one costs {self.upgrade_5_cost.formatted()}!")
        else:
            print("Not enough balance to buy a upgrade_4")


def buy_upgrade_5(self):
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
                self.upgrade_6_increase.value *= 2
                self.upgrade_6_current_multiplier.value = 16
            if self.upgrade_6_owned == 150:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_6_current_bps.value + (
                        self.upgrade_6_current_bps.value * 32)
                self.upgrade_6_current_bps.value = self.upgrade_6_increase.value * 32
                self.upgrade_6_increase.value *= 2
                self.upgrade_6_current_multiplier.value = 32
            print(
                f"Upgrade 6 bought! You own {self.upgrade_6_owned.value} upgrade 6. "
                f"Next one costs {self.upgrade_6_cost.formatted()}!")
        else:
            print("Not enough balance to buy an upgrade 6")


def buy_upgrade_6(self):
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
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
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
                self.upgrade_7_increase.value *= 2
                self.upgrade_7_current_multiplier.value = 16
            if self.upgrade_7_owned == 150:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_7_current_bps.value + (
                        self.upgrade_7_current_bps.value * 32)
                self.upgrade_7_current_bps.value = self.upgrade_7_increase.value * 32
                self.upgrade_7_increase.value *= 2
                self.upgrade_7_current_multiplier.value = 32
            print(
                f"Upgrade 7 bought! You own {self.upgrade_7_owned.value} upgrade 7. "
                f"Next one costs {self.upgrade_7_cost.formatted()}!")
        else:
            print("Not enough balance to buy an upgrade 7")


def buy_upgrade_7(self):
    if self.upgrade_7_owned >= 1:
        if self.balance >= self.upgrade_8_cost:
            self.balance -= self.upgrade_8_cost
            self.balance_per_second += self.upgrade_8_increase
            self.upgrade_8_current_bps += self.upgrade_8_increase
            self.upgrade_8_cost.value = self.upgrade_8_initial_cost.value * (
                    (1 + 0.15) ** (self.upgrade_8_owned.value + 1))
            self.upgrade_8_owned += 1
            if self.upgrade_8_owned == 10:
                self.click_multiplier.value *= 2
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_8_current_bps.value + (
                        self.upgrade_8_current_bps.value * 2)
                self.upgrade_8_current_bps.value = self.upgrade_8_increase.value * 2
                self.upgrade_8_increase.value *= 2
                self.upgrade_8_current_multiplier.value = 2
            if self.upgrade_8_owned == 25:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_8_current_bps.value + (
                        self.upgrade_8_current_bps.value * 4)
                self.upgrade_8_current_bps.value = self.upgrade_8_increase.value * 4
                self.upgrade_8_increase.value *= 2
                self.upgrade_8_current_multiplier.value = 4
            if self.upgrade_8_owned == 50:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_8_current_bps.value + (
                        self.upgrade_8_current_bps.value * 8)
                self.upgrade_8_current_bps.value = self.upgrade_8_increase.value * 8
                self.upgrade_8_increase.value *= 2
                self.upgrade_8_current_multiplier.value = 8
            if self.upgrade_8_owned == 100:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_8_current_bps.value + (
                        self.upgrade_8_current_bps.value * 16)
                self.upgrade_8_current_bps.value = self.upgrade_8_increase.value * 16
                self.click_multiplier.value *= 2
                if self.total_clicks.value >= 50:
                    self.click_rate.value = int(self.total_clicks.value / 50) * self.click_multiplier.value
                else:
                    self.click_rate.value = 1 * self.click_multiplier.value
                self.upgrade_8_increase.value *= 2
                self.upgrade_8_current_multiplier.value = 16
            if self.upgrade_8_owned == 150:
                self.balance_per_second.value = self.balance_per_second.value - self.upgrade_8_current_bps.value + (
                        self.upgrade_8_current_bps.value * 32)
                self.upgrade_8_current_bps.value = self.upgrade_8_increase.value * 32
                self.upgrade_8_increase.value *= 2
                self.upgrade_8_current_multiplier.value = 32
            print(
                f"Upgrade 8 bought! You own {self.upgrade_8_owned.value} upgrade 8. "
                f"Next one costs {self.upgrade_8_cost.formatted()}!")
        else:
            print("Not enough balance to buy an upgrade 8")