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

where $z = \frac{y - \mu}{\sigma}$.

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

Using the plug-in estimator as a training loss slightly rewards underdispersion, since shrinking the spread reduces $\mathbb{E}|X - X'|$. The smaller the sample, the larger the bias.

An alternative estimator is the fair CRPS ($\mathrm{fCRPS}$):

$$
\mathrm{fCRPS}(x^1, x^2, \dots, x^N, y) = \frac{1}{N} \sum_{n = 1}^{N} |x^n - y| - \frac{1}{2N(N - 1)} \sum_{n, n'} |x^n - x^{n'}|
$$

This is an unbiased estimator for the CRPS of the true distribution $F$. [Proof](proofs/fcrps-is-unbiased.md)

This is a fair scoring rule: it incentivises drawing $x^{1:N}$ from the same distribution as $Y$. [Proof](proofs/fcrps-is-fair.md)

Suppose we have $M$ independent training examples, with $y_m$ observed for example $m$. For each example, we have a predictive distribution $F_m$ and we can draw independent samples $x_m^{1:N} \sim F_m$.

We can aggregate the fair CRPS estimates over all of these examples:

$$
\frac{1}{M} \sum_{m = 1}^M \mathrm{fCRPS}(x^{1:N}_m, y_m)
$$

This is well-behaved for large $M$:

$$
\mathbb{E}\Big[\Big(\frac{1}{M} \sum_{m = 1}^M \mathrm{fCRPS}(X^{1:N}_m, y_m) - \frac{1}{M} \sum_{m = 1}^M \mathrm{CRPS}(F_m, y_m)\Big)^2\Big] \longrightarrow 0 \qquad (M \to \infty)
$$

[Proof](proofs/aggregated-fcrps-is-well-behaved.md)

This behaviour justifies using small $N$ (even as small as $N = 2$) if $M$ is large.

Aggregated plug-in CRPS does not behave well:

$$
\mathbb{E}\Big[\Big(\frac{1}{M} \sum_{m = 1}^M \widehat{\mathrm{CRPS}}(X^{1:N}_m, y_m) - \frac{1}{M} \sum_{m = 1}^M \mathrm{CRPS}(F_m, y_m)\Big)^2\Big] \nrightarrow 0 \qquad (M \to \infty)
$$

[Proof](proofs/aggregated-plugin-crps-is-not-well-behaved.md)

These results are checked against simulation in the [numerical verification](verification.md).
