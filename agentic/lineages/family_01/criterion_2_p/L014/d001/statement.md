# Portfolio Diversification Strategy

Time limit: 1 s   Memory limit: 256 MB

You are a quantitative analyst constructing investment vehicles from a pool of $n$ distinct financial assets, numbered 1 through $n$. Your firm offers exactly two investment funds: Fund 1 and Fund 2. Every asset must be allocated to exactly one of these two funds.

Risk analysis has highlighted $m$ pairs of assets that exhibit extreme market correlation. To ensure proper diversification and mitigate catastrophic losses, any two assets flagged as highly correlated must be separated—they cannot be assigned to the same fund.

The firm's automated trading system requires the final asset allocation to be strictly deterministic. If there are multiple valid ways to allocate the assets while respecting all separation constraints, the system requires the lexicographically smallest allocation. (An allocation is represented as a sequence of $n$ integers, where the $i$-th integer is the fund, 1 or 2, assigned to asset $i$. A sequence $A$ is lexicographically smaller than sequence $B$ if $A$ has a smaller value at the first position where they differ.)

If the correlation constraints are so entangled that no valid allocation exists, you must reject the pool entirely.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of assets and the number of highly correlated pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that asset $u$ and asset $v$ are highly correlated and must not be assigned to the same fund.

## Output
If no valid allocation is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers (each either 1 or 2) — the lexicographically smallest valid allocation.

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