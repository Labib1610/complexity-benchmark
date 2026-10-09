# Problem B — Market Equilibrium

Time limit: 1 s   Memory limit: 256 MB

You are analyzing a market with $n$ commodities. Each commodity $i$ must be assigned a pricing tier $p_i$, which must be chosen as either 1 or 2.

There are $m$ observed dependencies between pairs of commodities. The $k$-th dependency involves commodities $u_k$ and $v_k$.

To maintain market equilibrium, every dependency must satisfy two strict conditions:
1. At least one of the two commodities involved in the dependency must be assigned to pricing tier 1.
2. At least one of the two commodities involved in the dependency must be assigned to pricing tier 2.

Your objective is to determine if there exists a pricing tier assignment for all $n$ commodities that satisfies both conditions for all $m$ dependencies. If such an assignment exists, you must output it. In cases where multiple valid assignments exist, you must choose the one whose sequence of tiers $p_1, p_2, \dots, p_n$ is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of commodities and the number of dependencies.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), specifying the 1-based indices of the two commodities involved in that dependency.

## Output
If no valid pricing tier assignment can achieve equilibrium, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2\}$) denoting the pricing tiers. If there are multiple valid sequences, output the sequence that is lexicographically smallest.

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