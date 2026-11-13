import pandas as pd
import json
import re


def parse_matches(js_text):
    """Extract match records from Tennis Abstract JavaScript."""
    match = re.search(
        r"var\s+morematchmx\s*=\s*(\[[\s\S]*?\]);",
        js_text
    )

    if not match:
        raise ValueError("Could not find match data in the JS file.")

    return json.loads(match.group(1))
def matches_to_dataframe(matches):
    """Convert raw match records into a DataFrame."""
    if not matches:
        raise ValueError("No match records were provided.")

    df = pd.DataFrame(matches)

    return df
def select_match_columns(df):
    """Select relevant columns from female player match data."""
    cleaned = df[[0, 4, 11, 16]].copy()

    cleaned.columns = [
        "match_date",
        "result",
        "opponent",
        "opponent_dob"
    ]

    return cleaned

def calculate_ages(df, player_dob):
    """Calculate player age, opponent age, and age difference."""
    df = df.copy()

    df["match_date"] = pd.to_datetime(
        df["match_date"], format="%Y%m%d", errors="coerce"
    )
    df["opponent_dob"] = pd.to_datetime(
        df["opponent_dob"], format="%Y%m%d", errors="coerce"
    )
    player_dob = pd.to_datetime(player_dob)

    df["player_age"] = (
        (df["match_date"] - player_dob).dt.days / 365.25
    )
    df["opponent_age"] = (
        (df["match_date"] - df["opponent_dob"]).dt.days / 365.25
    )
    df["age_difference"] = df["player_age"] - df["opponent_age"]

    return df

def select_male_match_columns(df):
    """Select relevant columns from male player match data."""
    cleaned = df[[0, 4, 11, 15]].copy()

    cleaned.columns = [
        "match_date",
        "result",
        "opponent",
        "opponent_age"
    ]

    return cleaned
def calculate_male_ages(df, player_dob):
    """Calculate player age and age difference for male matches."""
    df = df.copy()

    df["match_date"] = pd.to_datetime(
        df["match_date"], format="%Y%m%d", errors="coerce"
    )
    df["opponent_age"] = pd.to_numeric(
        df["opponent_age"], errors="coerce"
    )
    player_dob = pd.to_datetime(player_dob)

    df["player_age"] = (
        (df["match_date"] - player_dob).dt.days / 365.25
    )
    df["age_difference"] = df["player_age"] - df["opponent_age"]

    return df
def clean_player_matches(js, tour, player_dob):
    """Convert raw match data into a cleaned DataFrame."""
    matches = parse_matches(js)
    df = matches_to_dataframe(matches)

    if tour == "atp":
        df = select_male_match_columns(df)
        df = calculate_male_ages(df, player_dob)
    elif tour == "wta":
        df = select_female_match_columns(df)
        df = calculate_female_ages(df, player_dob)
    else:
        raise ValueError("Tour must be 'atp' or 'wta'.")

    return df
