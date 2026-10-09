# Problem B — Asset Hedging

Time limit: 1 s   Memory limit: 256 MB

A wealth management firm is dividing a pool of $n$ financial assets between two distinct investment vehicles, designated as Vehicle 1 and Vehicle 2. Your task is to assign each of the $n$ assets to exactly one of these two vehicles.

To manage market volatility, quantitative analysts have flagged $m$ specific pairs of assets due to their extreme correlation. The firm enforces a strict hedging mandate on these flagged pairs: for any such pair, the sum of their assigned vehicle identifiers must equal exactly 3. 

You must determine if there is a complete assignment of all $n$ assets that perfectly satisfies every hedging mandate. If a valid assignment exists, you must output it. When multiple valid assignments exist, you must provide the one that forms the lexicographically smallest sequence of $n$ vehicle identifiers (where each identifier is 1 or 2).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), indicating the total number of assets and the number of flagged asset pairs. The assets are indexed from 1 to $n$.
The following $m$ lines each contain two integers $u$ and $v$, specifying a pair of assets that falls under the hedging mandate.

## Output
If no assignment can satisfy all hedging mandates, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (with each $s_i \in \{1, 2\}$) denoting the assigned vehicles for assets 1 through $n$. If there are multiple valid assignments, output the sequence that is lexicographically smallest.

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