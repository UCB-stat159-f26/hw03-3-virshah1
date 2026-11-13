from .download import download_player_data
from .clean import clean_player_matches


def get_player_matches(name, tour="wta", player_dob=None):
    """Download and clean a player's career match data."""
    if player_dob is None:
        raise ValueError("Please provide the player's date of birth.")

    js = download_player_data(name, tour=tour)
    return clean_player_matches(js, tour, player_dob)
