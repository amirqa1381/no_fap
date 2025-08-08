from datetime import datetime
from database.models.streak_model import Streak



def calculate_streak_days(streak: Streak) -> int:
    """
    Calculate the number of days in a streak.

    Args:
        streak (Streak): The streak object containing start and end dates.

    Returns:
        int: The number of days in the streak.
    """
    end = streak.end_date or datetime.now()
    return (end - streak.start_date).days