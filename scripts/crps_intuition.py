"""
Generate the CRPS intuition figures into ../figures/.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

FIGURE_DIRECTORY = Path(__file__).resolve().parent.parent / "figures"

def figure_empirical_cdf_gap():
    """
    Plot the gap between the predictive CDF and the observation's empirical CDF.
    """
    y = 0.8
    z = np.linspace(-5, 5, 1200)
    F = norm.cdf(z)
    G = (z >= y).astype(float)

    fig, ax = plt.subplots(figsize=(7, 4), dpi=200)
    ax.plot(z, F, lw=2, label="Φ(z)")
    ax.step(z, G, where="post", ls="--", label="𝟙[z ≥ y]")
    ax.fill_between(z, F, G, alpha=0.15)
    ax.legend(loc="upper left", frameon=False)
    ax.set(xlim=(-5, 5), ylim=(0, 1.1), xlabel="z")
    fig.savefig(FIGURE_DIRECTORY / "crps-empirical-cdf-gap.png")
    plt.close(fig)

def main():
    figure_empirical_cdf_gap()

if __name__ == "__main__":
    main()

