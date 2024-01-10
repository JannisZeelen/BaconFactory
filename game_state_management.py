from upgrades import Upgrades
import json


class GameStateManager:
    def __init__(self, upgrades):
        self.upgrades = upgrades
        print("Current balance in Upgrades:", upgrades.balance)

    def load_or_create_game_state(self, upgrades):
        try:
            # Attempt to load the game state from the save file
            print("Current balance in Upgrades:", upgrades.balance)
            self.load_game_state()
            print("Current balance in Upgrades after:", upgrades.balance)
        except FileNotFoundError:
            # If the save file is not found, continue with the initial state
            pass

    def save_game_state(self, filename='save/baconfactory_savestate.json'):
        # Convert the selected attributes to a dictionary
        save_data = GameStateManager.to_dict(self, self.upgrades)
        print(save_data)

        # Save the dictionary to a JSON file
        with open(filename, 'w') as file:
            json.dump(save_data, file)
            print('Game saved!')

    def load_game_state(self, filename='save/baconfactory_savestate.json'):
        # Load the dictionary from the JSON file
        with open(filename, 'r') as file:
            load_data = json.load(file)
            print('Existing save loaded!')

        # Update the object's attributes from the loaded dictionary
        GameStateManager.from_dict(self, load_data, self.upgrades)

    def to_dict(self, upgrades):
        # Create a dictionary with only the attributes you want to save
        print("Debug: balance =", upgrades.balance, type(upgrades.balance))
        print("Debug: balance_per_second =", upgrades.balance_per_second)
        save_data = {
            'balance': upgrades.balance,
            'balance_per_second': upgrades.balance_per_second,
            'click_rate': upgrades.click_rate,
            'pig_cost': upgrades.pig_cost,
            'pig_owned': upgrades.pig_owned,
            'upgrade_2_cost': upgrades.upgrade_2_cost,
            'upgrade_2_owned': upgrades.upgrade_2_owned,
            'upgrade_3_cost': upgrades.upgrade_3_cost,
            'upgrade_3_owned': upgrades.upgrade_3_owned,
            'upgrade_4_cost': upgrades.upgrade_4_cost,
            'upgrade_4_owned': upgrades.upgrade_4_owned,
            'upgrade_5_cost': upgrades.upgrade_5_cost,
            'upgrade_5_owned': upgrades.upgrade_5_owned,
            'upgrade_6_cost': upgrades.upgrade_6_cost,
            'upgrade_6_owned': upgrades.upgrade_6_owned,
            'upgrade_7_cost': upgrades.upgrade_7_cost,
            'upgrade_7_owned': upgrades.upgrade_7_owned,
        }
        return save_data

    def from_dict(self, data, upgrades):
        # Update the object's attributes from the provided dictionary
        upgrades.balance = data['balance']
        upgrades.balance_per_second = data['balance_per_second']
        upgrades.click_rate = data['click_rate']
        upgrades.pig_cost = data['pig_cost']
        upgrades.pig_owned = data['pig_owned']
        upgrades.upgrade_2_cost = data['upgrade_2_cost']
        upgrades.upgrade_2_owned = data['upgrade_2_owned']
        upgrades.upgrade_3_cost = data['upgrade_3_cost']
        upgrades.upgrade_3_owned = data['upgrade_3_owned']
        upgrades.upgrade_4_cost = data['upgrade_4_cost']
        upgrades.upgrade_4_owned = data['upgrade_4_owned']
        upgrades.upgrade_5_cost = data['upgrade_5_cost']
        upgrades.upgrade_5_owned = data['upgrade_5_owned']
        upgrades.upgrade_6_cost = data['upgrade_6_cost']
        upgrades.upgrade_6_owned = data['upgrade_6_owned']
        upgrades.upgrade_7_cost = data['upgrade_7_cost']
        upgrades.upgrade_7_owned = data['upgrade_7_owned']
