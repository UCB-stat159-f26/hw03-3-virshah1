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

    result = get_player_matches("Serena Williams")

    assert result == "cleaned data"
    mock_dob.assert_called_once_with("Serena Williams", "wta")
    mock_download.assert_called_once_with("Serena Williams", tour="wta")
    mock_clean.assert_called_once_with(
        "sample JavaScript", "wta", "1981-09-26"
    )
