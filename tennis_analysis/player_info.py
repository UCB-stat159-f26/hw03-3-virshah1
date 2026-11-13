import re
import requests

from . import format_player_name


def get_player_dob(name, tour="wta"):
    """Retrieve a player's birth date from Tennis Abstract."""
    player = "".join(word.capitalize() for word in name.split())
    prefix = "wplayer" if tour.lower() == "wta" else "player"
    url = f"https://www.tennisabstract.com/cgi-bin/{prefix}.cgi?p={player}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as error:
        raise ValueError(f"Could not retrieve profile for {name}.") from error

    match = re.search(r"\bvar\s+dob\s*=\s*['\"]?(\d{8})", response.text)

    if not match:
        raise ValueError(f"Could not find date of birth for {name}.")

    dob = match.group(1)
    return f"{dob[:4]}-{dob[4:6]}-{dob[6:]}"
