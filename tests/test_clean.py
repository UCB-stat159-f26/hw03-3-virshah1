import pandas as pd
import pytest

from tennis_analysis.clean import calculate_ages


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
