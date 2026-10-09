# Problem B — Asset Hedging

Time limit: 1 s   Memory limit: 256 MB

A wealth management firm is restructuring its holdings by dividing exactly $n$ financial assets into two distinct investment vehicles: Portfolio 1 and Portfolio 2. You are responsible for allocating each of the $n$ assets into exactly one of these two portfolios.

To minimize exposure to market volatility, the firm's analysts have identified $m$ pairs of assets that exhibit extreme correlation. A strict hedging mandate is enforced for these pairs: for any identified pair of assets, if one asset is allocated to Portfolio 1, the other must be placed in Portfolio 2. Conversely, if one is allocated to Portfolio 2, the other must be placed in Portfolio 1. 

Determine whether it is possible to allocate all $n$ assets into the two portfolios such that every hedging mandate is perfectly satisfied. If a valid allocation exists, you must provide it. In the event that multiple valid allocations are possible, you must select the one that is lexicographically smallest when expressed as a sequence of $n$ portfolio identifiers (each being either 1 or 2).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of assets and the number of correlated asset pairs, respectively. Assets are numbered from 1 to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$, representing a pair of assets subject to the hedging mandate.

## Output
If no valid allocation exists that satisfies all hedging mandates, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the assigned portfolios for assets 1 through $n$. If there are multiple valid allocations, output the sequence that is lexicographically smallest.

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