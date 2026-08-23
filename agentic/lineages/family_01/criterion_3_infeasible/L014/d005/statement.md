# Problem C — Signature Blend

Time limit: 2 s   Memory limit: 256 MB

You are developing a new fragrance using a library of $n$ distinct aromatic extracts. Due to chemical interactions, only specific pairs of extracts blend stably without degrading each other's scent profile. You have a laboratory report detailing $m$ such stable pairs.

You need to formulate a core accord. This accord must consist of exactly three distinct extracts. To ensure the fragrance does not separate over time, a stable blend must be possible between every pair of those three extracts. Therefore, a set of three extracts can only form the core accord if all three possible pairings among them are listed as stable in your laboratory report.

Find a set of three extracts that can form the core accord.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of extracts and the number of stable extract pairs. Extracts are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that extract $u$ and extract $v$ form a stable pair.
It is guaranteed that the input contains at least one valid set of three extracts for the accord.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of the three extracts.
If there are multiple valid sets of three extracts, output the one that is lexicographically smallest (i.e., smallest $a$; ties broken by smallest $b$; then smallest $c$).

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