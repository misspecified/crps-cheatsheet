For $X \sim N(\mu, \sigma^2)$:

$$
\mathrm{CRPS}(F, y) = \sigma\bigg(z\big(2\Phi(z) - 1\big) + 2\varphi(z) - \frac{1}{\sqrt{\pi}}\bigg)
$$

where $z = \frac{y - \mu}{\sigma}$.

We use the alternative form of the CRPS:

$$
\mathrm{CRPS}(F, y) = \mathbb{E}|X - y| - \tfrac{1}{2}\mathbb{E}|X - X'|
$$

Note that:

$$
f(x) = \frac{1}{\sigma} \varphi\bigg(\frac{x - \mu}{\sigma}\bigg)
$$

$$
F(x) = \Phi\bigg(\frac{x - \mu}{\sigma}\bigg)
$$

$$
\int_{a}^{b} \frac{x}{\sigma} \varphi\bigg(\frac{x - \mu}{\sigma}\bigg) dx
= \Big[ \mu \Phi\big(\tfrac{x - \mu}{\sigma}\big) - \sigma \varphi\big(\tfrac{x - \mu}{\sigma}\big) \Big]_{a}^{b}
$$


Then:

$$
\begin{aligned}
\mathbb{E}|X - y| &= \int_{-\infty}^{y} \frac{(y - x)}{\sigma} \varphi\bigg(\frac{x - \mu}{\sigma} \bigg) dx + \int_{y}^{\infty} \frac{(x - y)}{\sigma} \varphi\bigg(\frac{x - \mu}{\sigma} \bigg) dx \\ 
&= \int_{-\infty}^{y} \frac{y}{\sigma} \varphi\bigg(\frac{x - \mu}{\sigma} \bigg) dx - \int_{-\infty}^{y} \frac{x}{\sigma} \varphi\bigg(\frac{x - \mu}{\sigma} \bigg) dx + \int_{y}^{\infty} \frac{x}{\sigma} \varphi\bigg(\frac{x - \mu}{\sigma} \bigg) dx - \int_{y}^{\infty} \frac{y}{\sigma} \varphi\bigg(\frac{x - \mu}{\sigma} \bigg) dx \\
&= y\Phi\big(\tfrac{y - \mu}{\sigma}\big) - \Big[ \mu \Phi\big(\tfrac{x - \mu}{\sigma}\big) - \sigma \varphi\big(\tfrac{x - \mu}{\sigma}\big) \Big]_{-\infty}^{y} + \Big[ \mu \Phi\big(\tfrac{x - \mu}{\sigma}\big) - \sigma\varphi\big(\tfrac{x - \mu}{\sigma}\big) \Big]_{y}^{\infty} - y\Big(1 - \Phi\big(\tfrac{y - \mu}{\sigma}\big)\Big) \\
&= y\Phi(z) - \mu\Phi(z) + \sigma\varphi(z) + \mu - \mu\Phi(z) + \sigma\varphi(z) - y\big(1 - \Phi(z)\big) \\
&= (y - \mu)(2\Phi(z) - 1) + 2\sigma\varphi(z) \\
&= \sigma\big( z(2\Phi(z) - 1) + 2\varphi(z) \big)
\end{aligned}
$$

For $\mathbb{E}|X - X'|$, note that $X - X' \sim N(0, 2\sigma^2)$. We can reuse the above derivation with $y = 0$, $\mu = 0$, and $\sigma \mapsto \sqrt{2}\sigma$. So:

$$
\begin{aligned}
\mathbb{E}|X - X'| &= \sqrt{2}\sigma\big( 0(2\Phi(0) - 1) + 2\varphi(0) \big)\\
&= 2\sqrt{2}\sigma\varphi(0) \\
&= \frac{2\sigma}{\sqrt{\pi}} \\ 
\end{aligned}
$$

Assembling the two parts:

$$
\begin{aligned}
\mathrm{CRPS}(F, y) &= \mathbb{E}|X - y| - \tfrac{1}{2}\mathbb{E}|X - X'| \\
&= \sigma\big( z(2\Phi(z) - 1) + 2\varphi(z) \big) - \frac{\sigma}{\sqrt{\pi}} \\
&= \sigma\bigg(z\big(2\Phi(z) - 1\big) + 2\varphi(z) - \frac{1}{\sqrt{\pi}}\bigg) \\
\end{aligned}
$$