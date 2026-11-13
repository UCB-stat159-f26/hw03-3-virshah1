import matplotlib.pyplot as plt


def plot_player_matches(df):
    """Plot player age against opponent age difference."""
    fig, ax = plt.subplots(figsize=(11, 6))

    colors = {"W": "blue", "L": "purple"}

    for result, group in df.groupby("result"):
        ax.scatter(
            group["player_age"],
            group["age_difference"],
            color=colors.get(result, "gray"),
            label="Win" if result == "W" else "Loss",
            alpha=0.6,
            s=15
        )

    ax.set_xlabel("Player Age")
    ax.set_ylabel("Player Age Minus Opponent Age")
    ax.set_title("Career Tennis Matches")
    ax.grid(alpha=0.2)
    ax.legend()

    return fig
