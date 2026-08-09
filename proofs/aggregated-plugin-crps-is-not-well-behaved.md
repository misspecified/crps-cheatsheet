Suppose we have $M$ independent training examples, with $y_m$ observed for example $m$. For each example, we have a predictive distribution $F_m$ and we can draw independent samples $x_m^{1:N} \sim F_m$. Then:

$$
\mathbb{E}\Big[\Big(\frac{1}{M} \sum_{m = 1}^M \widehat{\mathrm{CRPS}}(X^{1:N}_m, y_m) - \frac{1}{M} \sum_{m = 1}^M \mathrm{CRPS}(F_m, y_m)\Big)^2\Big] \nrightarrow 0 \qquad (M \to \infty)
$$

Similarly to the [proof for fCRPS](aggregated-fcrps-is-well-behaved.md), define:

$$
D_m = \widehat{\mathrm{CRPS}}(X^{1:N}_m, y_m) - \mathrm{CRPS}(F_m, y_m)
$$

As in the previous proof:

$$
\begin{aligned}
\mathbb{E}\Big[\Big(\frac{1}{M} \sum_{m = 1}^M \widehat{\mathrm{CRPS}}(X^{1:N}_m, y_m) - \frac{1}{M} \sum_{m = 1}^M \mathrm{CRPS}(F_m, y_m)\Big)^2\Big]
&= \frac{1}{M^2} \mathbb{E} \Big[\sum_{m \neq m'} D_m D_{m'} + \sum_{m = 1}^M D_{m}^2\Big] \\
&= \frac{1}{M^2} \Big(\sum_{m \neq m'} \mathbb{E}[D_m]\mathbb{E}[D_{m'}] + \sum_{m = 1}^M \mathbb{E}[D_{m}^2]\Big) \\
\end{aligned}
$$

using the independence of $D_m$ and $D_{m'}$ to split the cross-terms.

For iid $X_m, X'_m \sim F_m$, define:

$$
b_m = \frac{1}{2N}\mathbb{E}|X_m - X'_m|
$$

By the [biasedness of the plug-in CRPS estimator](plugin-crps-is-biased.md), $\mathbb{E}[D_m] = b_m$. Assume that $b_m \geq b > 0, \forall m$.

Therefore:

$$
\mathbb{E}\Big[\Big(\frac{1}{M} \sum_{m = 1}^M \widehat{\mathrm{CRPS}}(X^{1:N}_m, y_m) - \frac{1}{M} \sum_{m = 1}^M \mathrm{CRPS}(F_m, y_m)\Big)^2\Big] = \frac{1}{M^2} \sum_{m \neq m'} b_m b_{m'} + \frac{1}{M^2} \sum_{m = 1}^M \mathbb{E}[D_{m}^2]
$$

Assuming that $\mathbb{E}[D_m^2] \leq C, \forall m$, the second term tends to $0$ exactly as in the [proof for fCRPS](aggregated-fcrps-is-well-behaved.md).

The first term is a sum of $M(M - 1)$ cross-terms, each at least $b^2$:

$$
\frac{1}{M^2} \sum_{m \neq m'} b_m b_{m'} \geq \frac{M(M - 1)}{M^2}\, b^2 \longrightarrow b^2 > 0 \qquad (M \to \infty)
$$

The sum of the two terms is therefore eventually bounded below by a positive constant, so it does not tend to $0$.
