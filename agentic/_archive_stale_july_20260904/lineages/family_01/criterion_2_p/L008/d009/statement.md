# Problem B — Harmonic Resonance

Time limit: 1 s   Memory limit: 256 MB

A facility operates $n$ resonance generators. There are $m$ interference testing links, each connecting a specific pair of generators. You must configure the facility by assigning each generator $i$ a state $s_i \in \{1, 2\}$. 

For any configuration, the system's overall resonance footprint is determined by calculating the sum of the states for each linked pair, and then taking the product of all $m$ of these sums. Formally, if the links connect pairs $(u_1, v_1), \dots, (u_m, v_m)$, the footprint is defined as $\prod_{j=1}^m (s_{u_j} + s_{v_j})$. (If $m=0$, the footprint is exactly $1$).

To ensure system stability, a configuration is only valid if its overall resonance footprint is exactly $3^m$.

Determine if there is a valid configuration for all $n$ generators.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of generators connected by an interference testing link.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1,2\}$) representing the valid configuration. If there are multiple valid configurations, output the one that minimizes the state $s_1$. If there is still a tie, minimize $s_2$, and so on sequentially up to $s_n$.

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