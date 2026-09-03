Suppose $Y \sim G$, and $X^{1:N} \sim F$ iid.

$\mathrm{fCRPS}(x^{1:N}, y)$ is a fair scoring rule if $\mathbb{E}_{X, Y}\big[\mathrm{fCRPS}(X^{1:N}, Y)\big]$ is minimised when $F = G$.

Assume $Y$ and $X^{1:N}$ are independent. Then:

$$
\mathbb{E}_{X, Y}\big[\mathrm{fCRPS}(X^{1:N}, Y)\big] = \mathbb{E}_{Y}\big[\mathbb{E}_{X}\big[\mathrm{fCRPS}(X^{1:N}, Y)\big]\big]
$$

[fCRPS is unbiased](fcrps-is-unbiased.md), therefore:

$$
\mathbb{E}_{Y}\big[\mathbb{E}_{X}\big[\mathrm{fCRPS}(X^{1:N}, Y)\big]\big] = \mathbb{E}_Y\big[\mathrm{CRPS}(F, Y)\big]
$$

[CRPS is a proper scoring rule](crps-is-proper.md), so $\mathbb{E}_Y\big[\mathrm{CRPS}(F, Y)\big]$ is minimised when $F = G$, hence $\mathrm{fCRPS}$ is fair.
