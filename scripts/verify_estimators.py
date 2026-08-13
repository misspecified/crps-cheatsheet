import math

import numpy as np
import pandas as pd
from scipy.stats import norm

SEED = 0
REPLICATIONS = 10_000
ENSEMBLE_SIZES = (2, 3, 5, 10, 20, 50)
MU, SIGMA, Y = 0.3, 1.2, 1.0


class Gaussian:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def crps(self, y):
        z = (y - self.mu) / self.sigma
        return self.sigma * (z * (2 * norm.cdf(z) - 1) + 2 * norm.pdf(z) - 1 / math.sqrt(math.pi))

    def sample(self, shape, rng):
        return rng.normal(self.mu, self.sigma, size=shape)


class CRPSEstimators:
    def __init__(self, distribution):
        self.distribution = distribution

    def plugin(self, y, n_samples, rng, n_replications):
        samples = self.distribution.sample((n_replications, n_samples), rng)
        return self._plugin_scores(samples, y).mean()

    def fair(self, y, n_samples, rng, n_replications):
        samples = self.distribution.sample((n_replications, n_samples), rng)
        return self._fair_scores(samples, y).mean()

    def _plugin_scores(self, samples, y):
        exy = np.abs(samples - y).mean(axis=1)
        exx = np.abs(samples[:, :, None] - samples[:, None, :]).mean(axis=(1, 2))
        return exy - 0.5 * exx

    def _fair_scores(self, samples, y):
        n_samples = samples.shape[1]
        exy = np.abs(samples - y).mean(axis=1)
        exx = np.abs(samples[:, :, None] - samples[:, None, :]).sum(axis=(1, 2)) / (n_samples * (n_samples - 1))
        return exy - 0.5 * exx


def gaussian_crps(mu, sigma, y, sample_sizes, rng, n_replications):
    distribution = Gaussian(mu, sigma)
    estimators = CRPSEstimators(distribution)
    exact = distribution.crps(y)

    rows = [
        {
            "n_samples": n,
            "exact": exact,
            "plugin": estimators.plugin(y, n, rng, n_replications),
            "fair": estimators.fair(y, n, rng, n_replications),
        }
        for n in sample_sizes
    ]

    df = pd.DataFrame(rows)
    n = df["n_samples"]
    df["plugin_error"] = df["plugin"] - df["exact"]
    df["exact_plugin_bias"] = sigma / (n * math.sqrt(math.pi))
    df["fair_error"] = df["fair"] - df["exact"]
    df["exact_fair_bias"] = 0.0
    return df


def run_experiment(rng):
    return {
        "Bias against the closed form": gaussian_crps(MU, SIGMA, Y, ENSEMBLE_SIZES, rng, REPLICATIONS),
    }


def main():
    rng = np.random.default_rng(SEED)
    for heading, df in run_experiment(rng).items():
        print(f"## {heading}\n")
        print(df.to_markdown(index=False))
        print()


if __name__ == "__main__":
    main()
