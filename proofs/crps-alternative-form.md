For iid $X, X' \sim F$:

$$
\mathrm{CRPS}(F, y) = \mathbb{E}|X - y| - \tfrac{1}{2}\mathbb{E}|X - X'|
$$


Note that:

$$
\begin{aligned}
&F(z) = \mathbb{E}\big[\mathbb{1}[X \leq z]\big] && (1) \\
&\rule{0pt}{2.2em}\mathbb{1}[a \leq z]\mathbb{1}[b \leq z] = \mathbb{1}[\max(a, b) \leq z] && (2) \\
&\rule{0pt}{2.2em}\int \mathbb{1}[a \leq z] - \mathbb{1}[b \leq z] dz = b - a && (3) \\
&\rule{0pt}{2.2em}2\max(a, b) = |a - b| + a + b && (4)
\end{aligned}
$$

Applying these four identities:

$$
\begin{aligned}
\mathrm{CRPS}(F, y)
&= \int \big(F(z) - \mathbb{1}[y \leq z]\big)^2 dz \\
&= \int \big(F(z)^2 - 2F(z)\mathbb{1}[y \leq z] + \mathbb{1}[y \leq z]\big) dz \\
&= \int \mathbb{E}\big[\mathbb{1}[X \leq z]\mathbb{1}[X' \leq z] - 2\mathbb{1}[X \leq z]\mathbb{1}[y \leq z] + \mathbb{1}[y \leq z]\big] dz && \text{by (1)} \\
&= \int \mathbb{E}\big[\mathbb{1}[\max(X, X') \leq z] - 2\mathbb{1}[\max(X, y) \leq z] + \mathbb{1}[y \leq z]\big] dz && \text{by (2)} \\
&= \int \mathbb{E}\big[\mathbb{1}[\max(X, X') \leq z] - \mathbb{1}[\max(X, y) \leq z] + \mathbb{1}[y \leq z] - \mathbb{1}[\max(X, y) \leq z]\big] dz \\
&= \mathbb{E}\Big[\int \mathbb{1}[\max(X, X') \leq z] - \mathbb{1}[\max(X, y) \leq z] dz + \int \mathbb{1}[y \leq z] - \mathbb{1}[\max(X, y) \leq z] dz \Big] \\
&= \mathbb{E}\big[\max(X, y) - \max(X, X') + \max(X, y) - y\big] && \text{by (3)} \\
&= \mathbb{E}\big[|X - y| + X - \tfrac{1}{2}(|X - X'| + X + X')\big] && \text{by (4)} \\
&= \mathbb{E}\big[|X - y| - \tfrac{1}{2}|X - X'|\big] && \text{by } X, X' \overset{\text{iid}}{\sim} F \\
&= \mathbb{E}|X - y| - \tfrac{1}{2}\mathbb{E}|X - X'| \\
\end{aligned}
$$
