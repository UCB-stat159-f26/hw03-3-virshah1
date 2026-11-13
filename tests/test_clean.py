import pandas as pd
import pytest

from tennis_analysis.clean import (
    calculate_ages,
    calculate_male_ages,
    parse_matches,
)

def test_calculate_ages():
    """Verify ages and age differences using known dates."""
    df = pd.DataFrame({
        "match_date": ["20200101"],
        "opponent_dob": ["19900101"]
    })

    result = calculate_ages(df, "2000-01-01")

    assert result["player_age"].iloc[0] == pytest.approx(20, abs=0.01)
    assert result["opponent_age"].iloc[0] == pytest.approx(30, abs=0.01)
    assert result["age_difference"].iloc[0] == pytest.approx(-10, abs=0.01)

def test_calculate_male_ages():
    """Verify ATP age calculations using sample data."""
    df = pd.DataFrame({
        "match_date": ["20200101"],
        "opponent_age": ["25"]
    })

    result = calculate_male_ages(df, "2000-01-01")

    assert result["player_age"].iloc[0] == pytest.approx(20, abs=0.01)
    assert result["opponent_age"].iloc[0] == 25
    assert result["age_difference"].iloc[0] == pytest.approx(-5, abs=0.01)

def test_parse_matches():
    """Test extracting match records from JavaScript."""
    js = 'var morematchmx = [["20200101", "Australian Open", "W"]];'

    matches = parse_matches(js)

    assert len(matches) == 1
    assert matches[0][0] == "20200101"
    assert matches[0][1] == "Australian Open"


def test_parse_matches_invalid():
    """Test that invalid JavaScript produces a useful error."""
    js = "This is not valid match data."

    with pytest.raises(ValueError, match="Could not find match data"):
        parse_matches(js)
