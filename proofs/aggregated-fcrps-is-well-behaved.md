
Suppose we have $M$ independent training examples, with $y_m$ observed for example $m$. For each example, we have a predictive distribution $F_m$ and we can draw independent samples $x_m^{1:N} \sim F_m$. Then:

$$
\mathbb{E}\Big[\Big(\frac{1}{M} \sum_{m = 1}^M \mathrm{fCRPS}(X^{1:N}_m, y_m) - \frac{1}{M} \sum_{m = 1}^M \mathrm{CRPS}(F_m, y_m)\Big)^2\Big] \longrightarrow 0 \qquad (M \to \infty)
$$

Define:

$$
D_m = \mathrm{CRPS}(F_m, y_m) - \mathrm{fCRPS}(X^{1:N}_m, y_m)
$$

Then:

$$
\begin{aligned}
\mathbb{E}\Big[\Big(\frac{1}{M} \sum_{m = 1}^M \mathrm{fCRPS}(X^{1:N}_m, y_m) - \frac{1}{M} \sum_{m = 1}^M \mathrm{CRPS}(F_m, y_m)\Big)^2\Big]
&= \frac{1}{M^2} \mathbb{E} \Big[\Big(\sum_{m = 1}^M D_m\Big)^2\Big] \\
&= \frac{1}{M^2} \mathbb{E} \Big[\sum_{m = 1}^M D_m \sum_{m' = 1}^M D_{m'}\Big] \\
&= \frac{1}{M^2} \mathbb{E} \Big[\sum_{m \neq m'} D_m D_{m'} + \sum_{m = 1}^M D_{m}^2\Big] \\
\end{aligned}
$$

Note that $\mathbb{E}[D_m] = 0$ by [unbiasedness of $\mathrm{fCRPS}$](fcrps-is-unbiased.md). Hence, the cross terms are zero in expectation by independence of $D_m$ and $D_{m'}$.

Therefore:

$$
\mathbb{E}\Big[\Big(\frac{1}{M} \sum_{m = 1}^M \mathrm{fCRPS}(X^{1:N}_m, y_m) - \frac{1}{M} \sum_{m = 1}^M \mathrm{CRPS}(F_m, y_m)\Big)^2\Big] = \frac{1}{M^2} \mathbb{E} \Big[\sum_{m = 1}^M D_{m}^2\Big]
$$

Assuming that $\mathbb{E}[D_m^2] \leq C, \forall m$:

$$
\frac{1}{M^2} \mathbb{E}\Big[\sum_{m = 1}^{M} D_m^2\Big] \leq \frac{C}{M} \longrightarrow 0 \qquad (M \to \infty)
$$