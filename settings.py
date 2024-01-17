import pygame_menu
from game_state_management import GameStateManager


def create_settings_menu(surface, set_volume, save_game, load_game, change_language):
    menu = pygame_menu.Menu('Settings', 600, 400)

    # Adding a volume slider
    menu.add.range_slider('Volume', default=50, onchange=set_volume, range_values=(0, 100), increment=1)

    # Adding buttons for save and load
    menu.add.button('Save Game', save_game)
    menu.add.button('Load Game', load_game)

    # Adding a dropdown for language selection
    menu.add.dropselect('Language', [('English', 'EN'), ('Spanish', 'ES'), ('German', 'DE')], onchange=change_language)

    # Adding a button to close the menu
    menu.add.button('Close', pygame_menu.events.EXIT)
    return menu
