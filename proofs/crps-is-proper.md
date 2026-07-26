If $Y \sim G$, then $\mathbb{E}_{Y}\big[\mathrm{CRPS}(F, Y)\big]$ is minimised at $F = G$.

First, consider the Brier score $\big(F(z) - \mathbb{1}[y \leq z]\big)^2$, for a fixed value of $z$. This is minimised (in expectation) at $F(z) = G(z)$:

$$
\begin{aligned}
\mathbb{E}_{Y}\big[\big(F(z) - \mathbb{1}[Y \leq z]\big)^2\big]
&= F(z)^2 - 2F(z)\mathbb{E}_{Y}\big[\mathbb{1}[Y \leq z]\big] + \mathbb{E}_{Y}\big[\mathbb{1}[Y \leq z]^2\big] \\
&= F(z)^2 - 2F(z)G(z) + \mathbb{E}_{Y}\big[\mathbb{1}[Y \leq z]\big] \\
&= F(z)^2 - 2F(z)G(z) + G(z) \\
&= (F(z) - G(z))^2 - G(z)^2 + G(z)
\end{aligned}
$$

$G(z)$ is fixed, so we minimise in expectation by picking $F(z) = G(z)$.

CRPS is obtained by integrating the Brier score over $z$.

$$
\begin{aligned}
\mathbb{E}_Y\big[\mathrm{CRPS}(F, Y)\big]
&= \mathbb{E}_Y\big[\int\big(F(z) - \mathbb{1}[Y \leq z]\big)^2 dz \big] \\
&= \int \mathbb{E}_{Y}\big[\big(F(z) - \mathbb{1}[Y \leq z]\big)^2\big] dz \\
&= \int (F(z) - G(z))^2 - G(z)^2 + G(z) dz
\end{aligned}
$$

We can simply minimise the integrand pointwise. The pointwise minimum is attained at $G(z)$ for each value of $z$. $G$ is an admissible CDF, so is a legitimate minimiser for the expected CRPS.
