from .download import download_player_data
from .clean import clean_player_matches
from .player_info import get_player_dob


def get_player_matches(name, tour="wta"):
    """Download and clean a player's career match data."""
    player_dob = get_player_dob(name, tour)
    js = download_player_data(name, tour=tour)
    return clean_player_matches(js, tour, player_dob)
