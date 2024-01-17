import time
from format_numbers import FormattedNumber


def calculate_offline_earnings(last_active_time, current_bps):
    """
    Calculate the earnings generated while the game was closed.

    :param last_active_time: The timestamp when the game was last active.
    :param current_bps: The player's bacon per second rate when the game was closed.
    :return: The total amount of bacon earned offline.
    """
    time_now = time.time()
    time_elapsed = time_now - last_active_time  # Time elapsed in seconds

    one_hour_in_seconds = 3600
    regular_rate_duration = min(time_elapsed, one_hour_in_seconds)
    reduced_rate_duration = max(time_elapsed - one_hour_in_seconds, 0)

    # Earnings for the first hour (5% of BpS)
    regular_earnings = (regular_rate_duration * current_bps) * 0.05

    # Earnings after the first hour (0.5% of BpS)
    reduced_earnings = (reduced_rate_duration * current_bps) * 0.005

    total_earnings = regular_earnings + reduced_earnings
    print(f"You earned {FormattedNumber(total_earnings).formatted()} bacon while you were offline.")
    return total_earnings
