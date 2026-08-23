# Portfolio Diversification Strategy

Time limit: 1 s   Memory limit: 256 MB

You are a quantitative analyst constructing a portfolio from a pool of $n$ distinct financial assets, numbered 1 through $n$. Each asset requires a risk profile index of either 1 or 2.

Risk analysis has flagged $m$ structural dependencies between certain pairs of assets. To maintain balanced exposure, regulatory rules dictate that any two assets linked by a dependency must have their risk profile indices sum to exactly 3.

The firm's automated trading system demands a strictly deterministic portfolio configuration. If multiple valid configurations satisfy all regulatory rules, the system filters them sequentially: it evaluates the assets in ascending order from 1 to $n$. For each asset $i$, if the pool of remaining valid configurations contains both assignments (1 and 2) for asset $i$, the system permanently discards all configurations where asset $i$ has an index of 2. This filtering proceeds through all $n$ assets until a single definitive configuration remains.

If the dependencies make it impossible to assign indices without violating a rule, you must reject the pool entirely.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of assets and the number of structural dependencies.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a dependency between asset $u$ and asset $v$.

## Output
If no valid configuration is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers (each either 1 or 2, separated by spaces) — the valid configuration that satisfies the system's deterministic tie-breaking rule.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```