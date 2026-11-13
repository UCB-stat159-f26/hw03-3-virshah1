import requests

from . import format_player_name


def download_player_data(name, tour="wta"):
    """Download a player's career match data from Tennis Abstract."""
    player = format_player_name(name)

    if tour.lower() == "wta":
        player = "".join(word.capitalize() for word in name.split())
    else:
        player = "".join(word.capitalize() for word in name.split())

    url = f"https://www.tennisabstract.com/jsmatches/{player}Career.js"

    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        raise ValueError(f"Could not find career data for {name}.")

    return response.text
