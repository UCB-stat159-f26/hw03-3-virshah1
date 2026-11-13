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
