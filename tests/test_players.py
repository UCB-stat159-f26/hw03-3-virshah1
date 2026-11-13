import pytest
from unittest.mock import patch
from tennis_analysis import get_player_matches


@patch("tennis_analysis.players.clean_player_matches")
@patch("tennis_analysis.players.download_player_data")
@patch("tennis_analysis.players.get_player_dob")
def test_get_player_matches(mock_dob, mock_download, mock_clean):
    """Test player retrieval without internet access."""
    mock_dob.return_value = "1981-09-26"
    mock_download.return_value = "sample JavaScript"
    mock_clean.return_value = "cleaned data"

    result = get_player_matches("Serena Williams", tour="wta")

    assert result == "cleaned data"
    mock_dob.assert_called_once_with("Serena Williams", "wta")
    mock_download.assert_called_once_with("Serena Williams", tour="wta")
    mock_clean.assert_called_once_with(
        "sample JavaScript", "wta", "1981-09-26"
    )

def test_automatic_tour_detection():
    """Verify that ATP is tried when WTA data is unavailable."""
    with patch(
        "tennis_analysis.players._get_matches_for_tour"
    ) as mock_get:
        mock_get.side_effect = [
            ValueError("Player not found on WTA"),
            "ATP match data"
        ]

        result = get_player_matches("Rafael Nadal")

        assert result == "ATP match data"
        assert mock_get.call_count == 2
        assert mock_get.call_args_list[0].args == ("Rafael Nadal", "wta")
        assert mock_get.call_args_list[1].args == ("Rafael Nadal", "atp")

def test_invalid_player_name():
    """Verify that unknown players produce a meaningful error."""
    with patch(
        "tennis_analysis.players._get_matches_for_tour"
    ) as mock_get:
        mock_get.side_effect = ValueError("Player not found")

        with pytest.raises(ValueError, match="Gaston Sanchez"):
            get_player_matches("Gaston Sanchez")

        assert mock_get.call_count == 2
