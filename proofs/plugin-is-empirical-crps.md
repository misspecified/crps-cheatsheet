Suppose we sample $x^1, x^2, \dots, x^N$. The empirical distribution of this sample is denoted by $\hat{F}_{N}$. Then, the CRPS of $\hat{F}_N$ is:

$$
\mathrm{CRPS}(\hat{F}_N, y) = \widehat{\mathrm{CRPS}}(x^1, x^2, \dots, x^N, y) = \frac{1}{N} \sum_{n = 1}^{N} |x^n - y| - \frac{1}{2N^2} \sum_{n, n'} |x^n - x^{n'}|
$$

For iid $X, X' \sim \hat{F}_N$:

$$
\mathbb{E}|X - y| = \sum_{n = 1}^N \frac{1}{N} |x^n - y|
$$

and:

$$
\mathbb{E}|X - X'| = \sum_{n' = 1}^N \sum_{n = 1}^N |x^{n} - x^{n'}| \frac{1}{N} \frac{1}{N} = \frac{1}{N^2} \sum_{n, n'} |x^n - x^{n'}|
$$

Then, by the [alternative form](crps-alternative-form.md), applied to $\hat{F}_N$:

$$
\mathrm{CRPS}(\hat{F}_N, y) = \mathbb{E}|X - y| - \frac{1}{2} \mathbb{E}|X - X'| = \frac{1}{N} \sum_{n = 1}^N |x^n - y| - \frac{1}{2N^2} \sum_{n, n'} |x^n - x^{n'}|
$$

