from .download import download_player_data
from .clean import clean_player_matches
from .player_info import get_player_dob


def get_player_matches(name, tour=None):
    """Retrieve and clean a player's career matches."""
    if tour is not None:
        return _get_matches_for_tour(name, tour)

    for candidate in ("wta", "atp"):
        try:
            return _get_matches_for_tour(name, candidate)
        except ValueError:
            continue

    raise ValueError(f"Could not find career data for player: {name}")


def _get_matches_for_tour(name, tour):
    """Retrieve and process matches for a specified tour."""
    player_dob = get_player_dob(name, tour)
    js = download_player_data(name, tour=tour)
    return clean_player_matches(js, tour, player_dob)
