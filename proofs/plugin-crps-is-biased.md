Suppose we sample $x^1, x^2, \dots, x^N$ iid from $F$. The plug-in estimator for $\mathrm{CRPS}(F, y)$:

$$
\widehat{\mathrm{CRPS}}(x^1, x^2, \dots, x^N, y) = \frac{1}{N} \sum_{n = 1}^{N} |x^n - y| - \frac{1}{2N^2} \sum_{n, n'} |x^n - x^{n'}|
$$

has bias:

$$
\mathrm{Bias}(\widehat{\mathrm{CRPS}}) = \frac{1}{2N} \mathbb{E}|X - X'|
$$

For iid $X^n \sim F$:

$$
\begin{aligned}
\mathbb{E}\Big[\widehat{\mathrm{CRPS}}(X^1, X^2, \dots, X^N, y)\Big] &= \mathbb{E}\Big[ \frac{1}{N} \sum_{n = 1}^{N} |X^n - y| - \frac{1}{2N^2} \sum_{n, n'} |X^n - X^{n'}|\Big]\\
&= \frac{1}{N} \sum_{n = 1}^N \mathbb{E}|X^n - y| - \frac{1}{2N^2} \sum_{n, n'} \mathbb{E}|X^n - X^{n'}| \\
&= \frac{1}{N} \sum_{n = 1}^N \mathbb{E}|X - y| - \frac{1}{2N^2} \Big( \sum_{n \neq n'} \mathbb{E}|X^n - X^{n'}| + \sum_{n} \mathbb{E}|X^n - X^n|\Big) \\
&= \frac{1}{N} N \mathbb{E}|X - y|  - \frac{1}{2N^2} \Big(N(N - 1) \mathbb{E}|X - X'| + 0\Big) \\
&= \mathbb{E}|X - y| - \frac{1}{2}\Big(1 - \frac{1}{N}\Big)\mathbb{E}|X - X'| \\
\end{aligned}
$$

where $X, X' \sim F$, iid.

Then, by the [alternative form](crps-alternative-form.md):

$$
\begin{aligned}
\mathrm{Bias}(\widehat{\mathrm{CRPS}}) &= \mathbb{E}\big[\widehat{\mathrm{CRPS}}(X^1, X^2, \dots, X^N, y)\big] - \mathrm{CRPS}(F, y) \\
&= \mathbb{E}|X - y| - \frac{1}{2}\Big(1 - \frac{1}{N}\Big)\mathbb{E}|X - X'| - \mathbb{E}|X - y|  + \frac{1}{2}\mathbb{E}|X - X'| \\
&= \frac{1}{2N} \mathbb{E}|X - X'|
\end{aligned}
$$