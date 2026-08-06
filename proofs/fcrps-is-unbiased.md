Suppose we sample $x^1, x^2, \dots, x^N$ iid from $F$. The fair estimator for $\mathrm{CRPS}(F, y)$:

$$
\mathrm{fCRPS}(x^1, x^2, \dots, x^N, y) = \frac{1}{N} \sum_{n = 1}^{N} |x^n - y| - \frac{1}{2N(N - 1)} \sum_{n, n'} |x^n - x^{n'}|
$$

is unbiased.

From the proof that [the plug-in CRPS is biased](plugin-crps-is-biased.md), we have that for iid $X^n \sim F$:

$$
\mathbb{E}\Big[\frac{1}{N} \sum_{n = 1}^{N} |X^n - y|\Big] = \mathbb{E}|X - y|
$$

and

$$
\begin{aligned}
\mathbb{E}\Big[\frac{1}{2N(N - 1)} \sum_{n, n'} |X^n - X^{n'}|\Big] &= \frac{1}{2N(N - 1)} \Big( N(N - 1) \mathbb{E}|X - X'| \Big)\\
&= \frac{1}{2} \mathbb{E}|X - X'|
\end{aligned}
$$

for iid $X, X' \sim F$.

Then, by the [alternative form](crps-alternative-form.md):

$$
\begin{aligned}
\mathrm{Bias}(\mathrm{fCRPS})
&= \mathbb{E}\big[\mathrm{fCRPS}(X^1, X^2, \dots, X^N, y)\big] - \mathrm{CRPS}(F, y) \\
&= \mathbb{E}|X - y| - \frac{1}{2} \mathbb{E}|X - X'| - \mathbb{E}|X - y| + \frac{1}{2} \mathbb{E}|X - X'| \\
&= 0 \\
\end{aligned}
$$