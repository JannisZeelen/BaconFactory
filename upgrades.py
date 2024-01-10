class Upgrades:
    def __init__(self, pygame):
        self.frying_pan_owned = 0
        self.frying_pan_initial_cost = 15
        self.frying_pan_cost = 15 * (1 + 1.15) ** self.frying_pan_owned
        self.frying_pan_base_increase = .2
        self.frying_pan_increase = .2

        self.pig_owned = 0
        self.pig_initial_cost = 100
        self.pig_cost = 100
        self.pig_base_increase = 1
        self.pig_increase = 1

        self.upgrade_2_owned = 0
        self.upgrade_2_initial_cost = 500
        self.upgrade_2_cost = 500 * (1 + 1.15) ** self.upgrade_2_owned
        self.upgrade_2_base_increase = 8
        self.upgrade_2_increase = 8

        self.upgrade_3_owned = 0
        self.upgrade_3_initial_cost = 3000
        self.upgrade_3_cost = 3000 * (1 + 1.15) ** self.upgrade_3_owned
        self.upgrade_3_base_increase = 20
        self.upgrade_3_increase = 20

        self.upgrade_4_owned = 0
        self.upgrade_4_initial_cost = 15000
        self.upgrade_4_cost = 15000 * (1 + 1.15) ** self.upgrade_4_owned
        self.upgrade_4_base_increase = 80
        self.upgrade_4_increase = 80

        self.upgrade_5_owned = 0
        self.upgrade_5_initial_cost = 100000
        self.upgrade_5_cost = 100000 * (1 + 1.15) ** self.upgrade_5_owned
        self.upgrade_5_base_increase = 500
        self.upgrade_5_increase = 500

        self.upgrade_6_owned = 0
        self.upgrade_6_initial_cost = 500000
        self.upgrade_6_cost = 500000 * (1 + 1.15) ** self.upgrade_6_owned
        self.upgrade_6_base_increase = 3000
        self.upgrade_6_increase = 3000

        self.upgrade_7_owned = 0
        self.upgrade_7_initial_cost = 2500000
        self.upgrade_7_cost = 2500000 * (1 + 1.15) ** self.upgrade_7_owned
        self.upgrade_7_base_increase = 10000
        self.upgrade_7_increase = 10000

        self.balance = 0
        self.initial_click_rate = 1
        self.click_rate = 1
        self.balance_per_second = 0 + (self.pig_owned * self.pig_base_increase) + (
                self.upgrade_2_owned * self.upgrade_2_base_increase) + (
                                          self.upgrade_3_owned * self.upgrade_3_base_increase) + (
                                          self.upgrade_4_owned * self.upgrade_4_base_increase) + (
                                          self.upgrade_5_owned * self.upgrade_5_base_increase) + (
                                          self.upgrade_6_owned * self.upgrade_6_base_increase) + (
                                          self.upgrade_7_owned * self.upgrade_7_base_increase)
        # Upgrades
        self.pig_image = pygame.image.load("assets/img/pig.png")
        self.pig_upgrade = pygame.transform.scale(self.pig_image, (40, 40))
        self.pig_skill = pygame.transform.scale(self.pig_image, (50 - 10, 50 - 10))

        self.upgrade_2_image = pygame.image.load("assets/img/upgrade_2.png")
        self.upgrade_2_upgrade = pygame.transform.scale(self.upgrade_2_image, (40, 40))
        self.upgrade_2_skill = pygame.transform.scale(self.upgrade_2_image, (50 - 10, 50 - 10))

        self.frying_pan_image = pygame.image.load("assets/img/frying_pan.png")
        self.frying_pan = pygame.transform.scale(self.frying_pan_image, (40, 40))
        self.frying_pan_skill = pygame.transform.scale(self.frying_pan_image, (50 - 10, 50 - 10))

        self.upgrade_3_image = pygame.image.load("assets/img/upgrade_3.png")
        self.upgrade_3_upgrade = pygame.transform.scale(self.upgrade_3_image, (40, 40))
        self.upgrade_3_skill = pygame.transform.scale(self.upgrade_3_image, (50 - 10, 50 - 10))

        self.upgrade_4_image = pygame.image.load("assets/img/upgrade_4.png")
        self.upgrade_4_upgrade = pygame.transform.scale(self.upgrade_4_image, (40, 40))
        self.upgrade_4_skill = pygame.transform.scale(self.upgrade_4_image, (50 - 10, 50 - 10))

        self.question_mark_skill_image = pygame.image.load("assets/img/question_mark.png")
        self.question_mark_skill = pygame.transform.scale(self.question_mark_skill_image, (50 - 10, 50 - 10))

        # Button-geometry / 60 px unterschied untereinander
        self.buy_frying_pan_button_rect = pygame.Rect((550, 65, 230, 50))
        self.buy_pig_button_rect = pygame.Rect(550, 125, 230, 50)
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

    def buy_frying_pan(self):
        if self.balance >= self.frying_pan_cost:
            self.balance -= self.frying_pan_cost
            self.frying_pan_increase = self.frying_pan_base_increase * (1 + 0.15) ** (self.frying_pan_owned + 1)
            self.balance_per_second += self.frying_pan_increase
            self.frying_pan_cost = self.frying_pan_initial_cost * (1 + 0.15) ** (self.frying_pan_owned + 1)
            self.frying_pan_owned += 1
            print(f"Frying Pan bought! You own {self.frying_pan_owned} Frying Pans. Next one costs {self.frying_pan_cost}!")
        else:
            print("Not enough balance to buy a frying pan")

    def buy_pig(self):
        if self.balance >= self.pig_cost:
            self.balance -= self.pig_cost
            self.pig_increase = self.pig_base_increase * (1 + 0.15) ** (self.pig_owned + 1)
            self.balance_per_second += self.pig_increase
            self.pig_cost = self.pig_initial_cost * (1 + 0.15) ** (self.pig_owned + 1)
            self.pig_owned += 1
            # if self.pig_owned == 5:
            #     self.click_rate += 1
            # if self.pig_owned == 10:
            #     self.click_rate += 2
            print(f"Pig bought! You own {self.pig_owned} Pigs. Next one costs {self.pig_cost}!")
        else:
            print("Not enough balance to buy a pig")

    def buy_upgrade_2(self):
        if self.pig_owned >= 2:
            if self.balance >= self.upgrade_2_cost:
                self.balance -= self.upgrade_2_cost
                self.upgrade_2_increase = self.upgrade_2_base_increase * (1 + 0.15) ** (self.upgrade_2_owned + 1)
                self.balance_per_second += self.upgrade_2_increase
                self.upgrade_2_cost += int(50 * (self.upgrade_2_owned + 1) ** 1.5)
                self.upgrade_2_owned += 1
                if self.upgrade_2_owned == 5:
                    self.click_rate += 2
                if self.upgrade_2_owned == 10:
                    self.click_rate += 4
                print(
                    f"Upgrade 2 bought! You own {self.upgrade_2_owned} Upgrade 2. Next one costs {self.upgrade_2_cost}!")
            else:
                print("Not enough balance to buy a upgrade_2")

    def buy_upgrade_3(self):
        if self.upgrade_2_owned >= 2:
            if self.balance >= self.upgrade_3_cost:
                self.balance -= self.upgrade_3_cost
                self.upgrade_3_increase = self.upgrade_3_base_increase * (1 + 0.15) ** (self.upgrade_3_owned + 1)
                self.balance_per_second += self.upgrade_3_increase
                self.upgrade_3_cost += int(50 * (self.upgrade_3_owned + 1) ** 1.5)
                self.upgrade_3_owned += 1
                print(
                    f"Silver bacon bought! You own {self.upgrade_3_owned} silver bacon. "
                    f"Next one costs {self.upgrade_3_cost}!")
            else:
                print("Not enough balance to buy a silver bacon")

    def buy_upgrade_4(self):
        if self.upgrade_3_owned >= 2:
            if self.balance >= self.upgrade_4_cost:
                self.upgrade_4_increase = self.upgrade_4_base_increase * (1 + 0.15) ** (self.upgrade_4_owned + 1)
                self.balance -= self.upgrade_4_cost
                self.balance_per_second += self.upgrade_4_increase
                self.upgrade_4_cost += int(50 * (self.upgrade_4_owned + 1) ** 1.5)
                self.upgrade_4_owned += 1
                print(
                    f"Golden bacon bought! You own {self.upgrade_4_owned} golden bacon. "
                    f"Next one costs {self.upgrade_4_cost}!")
            else:
                print("Not enough balance to buy a upgrade_4")

    def buy_upgrade_5(self):
        if self.upgrade_4_owned >= 2:
            if self.balance >= self.upgrade_5_cost:
                self.balance -= self.upgrade_5_cost
                self.upgrade_5_increase = self.upgrade_5_base_increase * (1 + 0.15) ** (self.upgrade_5_owned + 1)
                self.balance_per_second += self.upgrade_5_increase
                self.upgrade_5_cost += int(50 * (self.upgrade_5_owned + 1) ** 1.5)
                self.upgrade_5_owned += 1
                print(
                    f"Upgrade 6 bought! You own {self.upgrade_5_owned} upgrade 6. "
                    f"Next one costs {self.upgrade_5_cost}!")
            else:
                print("Not enough balance to buy an upgrade 6")

    def buy_upgrade_6(self):
        if self.upgrade_5_owned >= 2:
            if self.balance >= self.upgrade_6_cost:
                self.balance -= self.upgrade_6_cost
                self.upgrade_6_increase = self.upgrade_6_base_increase * (1 + 0.15) ** (self.upgrade_6_owned + 1)
                self.balance_per_second += self.upgrade_6_increase
                self.upgrade_6_cost += int(50 * (self.upgrade_6_owned + 1) ** 1.5)
                self.upgrade_6_owned += 1
                print(
                    f"Upgrade 7 bought! You own {self.upgrade_6_owned} upgrade 7. "
                    f"Next one costs {self.upgrade_6_cost}!")
            else:
                print("Not enough balance to buy an upgrade 7")

    def buy_upgrade_7(self):
        if self.upgrade_6_owned >= 2:
            if self.balance >= self.upgrade_7_cost:
                self.balance -= self.upgrade_7_cost
                self.upgrade_7_increase = self.upgrade_7_base_increase * (1 + 0.15) ** (self.upgrade_7_owned + 1)
                self.balance_per_second += self.upgrade_7_increase
                self.upgrade_7_cost += int(50 * (self.upgrade_7_owned + 1) ** 1.5)
                self.upgrade_7_owned += 1
                print(
                    f"Upgrade 8 bought! You own {self.upgrade_7_owned} upgrade 8. "
                    f"Next one costs {self.upgrade_7_cost}!")
            else:
                print("Not enough balance to buy an upgrade 8")
