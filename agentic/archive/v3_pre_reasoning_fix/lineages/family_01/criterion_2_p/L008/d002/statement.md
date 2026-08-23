# Problem B — Leverage Compliance

Time limit: 1 s   Memory limit: 256 MB

A financial firm manages $n$ investment funds. For the upcoming quarter, each fund must be assigned a leverage tier of either $1$ or $2$.

The firm's risk management system has identified $m$ pairs of funds that share significant asset overlaps. To comply with regulatory cross-exposure limits, the firm must ensure that for every identified pair, the product of their assigned leverage tiers is exactly $2$. 

You must determine a leverage tier assignment for each fund that satisfies all cross-exposure constraints, or report that no such arrangement is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of funds that share asset overlaps.

## Output
If no valid leverage arrangement exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $t_1, \dots, t_n$ (each $t_i \in \{1, 2\}$), where $t_i$ is the leverage tier assigned to fund $i$. If there are multiple valid arrangements, output the one that is lexicographically smallest.

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