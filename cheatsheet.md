# CRPS Cheatsheet

## Definition

The Continuous Ranked Probability Score (or CRPS) is given by:

$$
\mathrm{CRPS}(F, y) = \int \big(F(z) - \mathbb{1}[y \leq z]\big)^2 dz
$$

Note that $\big(F(z) - \mathbb{1}[y \leq z]\big)^2$
is the Brier score for a fixed value of $z$. CRPS integrates over all choices of $z$.

### Intuition

CRPS is the integral of the squared distance between the predicted cumulative distribution function (CDF) and the empirical CDF of a single observation, $y$. If $y$ is known, it is minimised by a point mass at $y$. CRPS rewards sharp, calibrated predictions. 

![CRPS as the squared gap between two CDFs](figures/crps-empirical-cdf-gap.png)

## Properties

CRPS is a *proper scoring rule*. If the distribution of $Y$ is known, $Y \sim G$, then the expected value of the CRPS is minimised by $F = G$.

[Proof](proofs/crps-is-proper.md)

CRPS can be reframed as a difference of expectations. For iid $X, X' \sim F$:

$$
\mathrm{CRPS}(F, y) = \mathbb{E}|X - y| - \tfrac{1}{2}\mathbb{E}|X - X'|
$$

[Proof](proofs/crps-alternative-form.md)

For $X \sim N(\mu, \sigma^2)$:

$$
\mathrm{CRPS}(F, y) = \sigma\bigg(z\big(2\Phi(z) - 1\big) + 2\varphi(z) - \frac{1}{\sqrt{\pi}}\bigg)
$$

[Proof](proofs/gaussian-crps.md)

## Estimators

We may wish to estimate CRPS in the case where we do not know $F$, but we can sample from it.

Suppose we sample $x^1, x^2, \dots, x^N$ iid from $F$. The naive "plug-in" estimator for the CRPS of $F$ is:

$$
\widehat{\mathrm{CRPS}}(x^1, x^2, \dots, x^N, y) = \frac{1}{N} \sum_{n = 1}^{N} |x^n - y| - \frac{1}{2N^2} \sum_{n, n'} |x^n - x^{n'}|
$$

This is the exact CRPS of the empirical distribution of the sample, $\hat{F}_N$. [Proof](proofs/plugin-is-empirical-crps.md)

This is a biased estimator for the CRPS of the true distribution, $F$, with:

$$
\mathrm{Bias}(\widehat{\mathrm{CRPS}}) = \frac{1}{2N} \mathbb{E}|X - X'|
$$

[Proof](proofs/plugin-crps-is-biased.md)

