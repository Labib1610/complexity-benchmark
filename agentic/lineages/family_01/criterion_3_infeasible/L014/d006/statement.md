# Problem C — Balanced Triad

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a market containing $n$ financial assets. Due to market dynamics, only specific pairs of assets exhibit a mutually stable hedge. You have a verified list of $m$ such hedged asset pairs.

You must construct a core portfolio. This portfolio requires exactly three distinct assets. To ensure the portfolio is resilient against volatility, a stable hedge must exist between every pair of assets within it. Therefore, a set of three assets can only form the core portfolio if all three possible pairings among them are present in your list of hedged pairs.

Find a set of three assets that can form the core portfolio.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of assets and the number of hedged pairs. Assets are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that asset $u$ and asset $v$ form a stable hedge.
It is guaranteed that the input contains at least one valid set of three assets for the portfolio.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of the three assets.
If there are multiple valid sets of three assets, output the one that is lexicographically smallest (i.e., smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```