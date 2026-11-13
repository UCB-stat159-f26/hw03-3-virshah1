def format_player_name(name):
    """Convert a player name into Tennis Abstract's filename format."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Please provide a valid player name.")

    return "".join(name.split()).lower()
