import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns

np.random.seed(21)


def game_generating(number=100):
    """Generate and return a list of 3-value lists.

    Keyword argument:
    number -- number of 3-value lists in the list (default 100)
    """
    samples = [
        ["Car", "Goat", "Goat"],
        ["Goat", "Car", "Goat"],
        ["Goat", "Goat", "Car"],
    ]
    games = []

    for n in range(number):
        index = np.random.randint(0, 3)
        games.append(samples[index])

    return games


def run_game_without_switch(game):
    """Return result of a game without switching the door.

    Keyword argument:
    game -- a 3-value list
    """
    index = np.random.randint(0, 3)
    result = ""

    if game[index] == "Car":
        result = "Win"
    else:
        result = "Fail"

    return result


def run_game_with_switch(game):
    """Return result of a game with switching the door.

    Keyword argument:
    game -- a 3-value list
    """
    index = np.random.randint(0, 3)
    result = ""

    if game[index] == "Car":
        result = "Fail"
    else:
        result = "Win"

    return result


def run_games(game_type, number=100):
    """Return chance to win in numerous games.

    Keyword arguments:
    game_type -- a string ('Without switch' or 'With switch')
    number -- a number of generating games (default 100)
    """
    games = game_generating(number)
    results = []
    success = 0

    for game in games:
        result = ""
        if game_type == "Without switch":
            result = run_game_without_switch(game)
        else:
            result = run_game_with_switch(game)

        results.append(result)

    for result in results:
        if result == "Win":
            success += 1

    return (success / number) * 100


# Two histograms on one plot
def show_distribution(iterations=500):
    """Show two histograms of distributions of chances to win in generated games.

    Keyword argument:
    iterations -- a number of running numerous games simulations (default 500)
    """
    without_switch_results = []
    with_switch_results = []

    for iteration in range(iterations):
        without_switch_results.append(run_games("Without switch", 500))
        with_switch_results.append(run_games("With switch", 500))

    pyplot.hist(
        without_switch_results,
        bins=30,
        alpha=0.8,
        label="without changing the door",
        color="#9e6a97",
    )
    pyplot.hist(
        with_switch_results,
        bins=30,
        alpha=0.8,
        label="with changing the door",
        color="#756597",
    )
    pyplot.title("Chances to win")
    pyplot.xlabel("Probability")
    pyplot.ylabel("Frequency")
    pyplot.legend(loc="upper center")

    pyplot.show()


show_distribution(500)

# Two histograms on different plots (with Matplotlib library)
def show_distribution_subplot_plt(iterations=500):
    """Show subplot with histograms of distributions of chances to win in generated games.

    Keyword argument:
    iterations -- a number of running numerous games simulations (default 500)
    """
    without_switch_results = []
    with_switch_results = []

    for iteration in range(iterations):
        without_switch_results.append(run_games("Without switch", 500))
        with_switch_results.append(run_games("With switch", 500))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle("Chances to win", size=18)
    fig.tight_layout(pad=2.0)

    ax1.hist(without_switch_results, bins=15, color="#9e6a97", alpha=0.8)
    ax1.set_title("WITHOUT switching the door")
    ax1.set_xlim(25, 40)
    ax1.plot(kind="kde", data=without_switch_results, color="red")

    ax2.hist(with_switch_results, bins=15, color="#756597", alpha=0.8)
    ax2.set_title("WITH switching the door")
    ax2.set_xlim(55, 75)

    for ax in (ax1, ax2):
        ax.set(xlabel="Probability", ylabel="Frequency")
        ax.tick_params(left=False, bottom=False)
        ax.set_yticks([])
        for ax, spine in ax.spines.items():
            spine.set_visible(False)

    plt.show()


show_distribution_subplot_plt(500)

# Two histograms on different plots (with Seaborn library)
def show_distribution_subplot_sns(iterations=500):
    """Show subplot with histograms of distributions of chances to win in generated games.

    Keyword argument:
    iterations -- a number of running numerous games simulations (default 500)
    """
    without_switch_results = []
    with_switch_results = []

    for iteration in range(iterations):
        without_switch_results.append(run_games("Without switch", 500))
        with_switch_results.append(run_games("With switch", 500))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle("Chances to win", size=18)
    fig.tight_layout(pad=2.0)

    sns.histplot(
        without_switch_results,
        ax=ax1,
        bins=15,
        kde=False,
        facecolor="#9e6a97",
        alpha=1,
        edgecolor="#9e6a97",
        stat="density",
    )
    sns.kdeplot(without_switch_results, ax=ax1, color="#660066", linewidth=1)
    ax1.set_title("WITHOUT switching the door")

    sns.histplot(
        with_switch_results,
        ax=ax2,
        bins=15,
        kde=False,
        facecolor="#756597",
        alpha=1,
        edgecolor="#756597",
        stat="density",
    )
    sns.kdeplot(with_switch_results, ax=ax2, color="#660066", linewidth=1)
    ax2.set_title("WITH switching the door")

    for ax in (ax1, ax2):
        ax.set(xlabel="Probability", ylabel="Frequency")
        ax.tick_params(left=False, bottom=False)
        ax.set_yticks([])

    sns.despine(left=True, bottom=True)

    plt.show()


show_distribution_subplot_sns(500)
