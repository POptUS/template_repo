# Appendix

## Taylor Remainder Theorem

```{prf:Theorem}
:label: eqn:TaylorRemainder
Given $k \in \N$, $x_0,h \in \R$, and a function $f : \R \to \R$.  If
$f^{(k+1)}$ exists on $(x_0, x_0 + h)$ and $f^{(k)}$ is continuous on $[x_0,
x_0 + h]$, then there exists $\xi \in (x_0, x_0 + h)$ such that
\begin{equation*}
f(x_0 + h) = f(x_0) + f'(x_0)h + \frac{1}{2!}f''(x_0)h^2 + \cdots +
\frac{1}{k!}f^{(k)}(x_0)h^k + \frac{1}{(k+1)!}f^{(k+1)}(\xi)h^{k+1}.
\end{equation*}
```
