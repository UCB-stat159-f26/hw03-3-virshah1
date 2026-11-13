import requests


def download_player_data(name, tour="wta"):
    """Download a player's career match data from Tennis Abstract."""
    player = "".join(
        word.capitalize() if word.islower() else word
        for word in name.split()
    )
    url = f"https://www.tennisabstract.com/jsmatches/{player}Career.js"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as error:
        raise ValueError(
            f"Could not retrieve career data for {name}."
        ) from error

    if "morematchmx" not in response.text:
        raise ValueError(f"Invalid career data for {name}.")

    return response.text
