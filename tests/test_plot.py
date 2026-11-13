import matplotlib
matplotlib.use("Agg")

import pandas as pd
from tennis_analysis import plot_player_matches


def test_plot_player_matches():
    """Test plotting with sample data, without internet access."""
    df = pd.DataFrame({
        "player_age": [20, 21, 22, 23],
        "age_difference": [-2, 3, -1, 4],
        "result": ["W", "L", "W", "L"]
    })

    fig = plot_player_matches(df)
    ax = fig.axes[0]

    assert ax.get_xlabel() == "Player Age"
    assert ax.get_ylabel() == "Player Age Minus Opponent Age"
    assert len(ax.collections) == 2
