# Problem A — Transmission Tiers

Time limit: 2 s   Memory limit: 256 MB

You are deploying a network of $n$ automated transmission towers. Each tower must be configured to operate at exactly one of three available power tiers, designated as tier 1, tier 2, and tier 3.

Due to terrain constraints, certain pairs of towers have overlapping broadcast regions. There are $m$ such overlapping pairs. To prevent destructive interference, the signals within an overlapping region must be asymmetric. Specifically, within any overlapping pair, one of the two towers must operate at a strictly higher power tier than the other.

Determine if there is a valid power tier configuration for all $n$ towers. If multiple valid configurations exist, output the assignment that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ — the number of transmission towers and the number of overlapping pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of towers with overlapping broadcast regions.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $t_1, t_2, \dots, t_n$ (each in $\{1, 2, 3\}$), where $t_i$ is the power tier of tower $i$. Among all valid configurations, output the lexicographically smallest sequence (compare $t_1$ first, then $t_2$, and so on).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```