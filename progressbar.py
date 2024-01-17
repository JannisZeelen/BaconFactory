import pygame


def draw_progress_bar(screen, x, y, width, height, progress, bg_color):
    """
    Draws a progress bar with a color that changes from red to green based on the progress.

    :param screen: Pygame screen to draw on.
    :param x, y: Position of the progress bar.
    :param width, height: Size of the progress bar.
    :param progress: Current progress (0.0 to 1.0).
    :param bg_color: Background color of the progress bar.
    """
    # Draw the background
    pygame.draw.rect(screen, bg_color, [x, y, width, height])

    # Calculate the width of the progress part
    progress_width = int(width * progress)

    # Calculate color based on progress (transition from red to green)
    fg_color = (255 * (1 - progress), 255 * progress, 0)

    # Draw the progress part
    pygame.draw.rect(screen, fg_color, [x, y, progress_width, height])


def draw_upgrade_progress_bar(screen, upgrade_owned, upgrade_targets, x, y, width, height, bg_color, fg_color):
    """
    Draws a progress bar for an upgrade based on its current 'owned' level.

    :param screen: Pygame screen to draw on.
    :param upgrade_owned: Current 'owned' level of the upgrade.
    :param upgrade_targets: List of target levels for the upgrade.
    :param x, y: Position of the progress bar.
    :param width, height: Size of the progress bar.
    :param bg_color, fg_color: Background and foreground colors of the progress bar.
    """
    # Find the next target level
    next_target = next((target for target in upgrade_targets if upgrade_owned < target), upgrade_targets[-1])

    # Calculate progress
    last_target = 0 if upgrade_targets.index(next_target) == 0 else upgrade_targets[
        upgrade_targets.index(next_target) - 1]
    progress = (upgrade_owned - last_target) / (next_target - last_target)

    # Draw the progress bar
    draw_progress_bar(screen, x, y, width, height, progress, bg_color)
