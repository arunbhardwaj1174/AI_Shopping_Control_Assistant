from matplotlib.figure import Figure


def build_summary_figure(summary):
    fig = Figure(figsize=(5.4, 3.4), dpi=100)
    ax = fig.add_subplot(111)
    labels = ["No Regret", "Regret"]
    values = [summary.get("no_regret", 0), summary.get("regret", 0)]
    ax.bar(labels, values, color=["#4caf50", "#f44336"])
    ax.set_title("Prediction Summary")
    ax.set_ylabel("Records")
    ax.grid(axis="y", alpha=0.3)
    for index, value in enumerate(values):
        ax.text(index, value + 0.1, str(value), ha="center", va="bottom")
    fig.tight_layout()
    return fig
