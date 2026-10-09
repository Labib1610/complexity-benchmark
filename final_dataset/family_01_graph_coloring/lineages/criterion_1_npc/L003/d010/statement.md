# Antenna Alignment

Time limit: 2 s   Memory limit: 256 MB

You are tasked with configuring a network of $n$ communication antennas. Every antenna in the network requires exactly one operational mode, which must be selected from the integers 1, 2, and 3.

The terrain contains $m$ direct line-of-sight links between specific pairs of antennas. When two antennas share a line-of-sight link, their signals interact, generating an interference value. The interference value for a link between an antenna assigned mode $x$ and an antenna assigned mode $y$ is given by the value $I_{x, y}$ from the following interference table:

- $I_{1, 1} = 6$, $I_{1, 2} = -3$, $I_{1, 3} = -3$
- $I_{2, 1} = -3$, $I_{2, 2} = 6$, $I_{2, 3} = -3$
- $I_{3, 1} = -3$, $I_{3, 2} = -3$, $I_{3, 3} = 6$

To guarantee reliable communication, the network must be perfectly stabilized. The total network interference—calculated as the sum of the interference values across all $m$ line-of-sight links—must evaluate to exactly $-3m$.

Your objective is to determine if there exists a complete assignment of operational modes to all $n$ antennas that achieves a total network interference of exactly $-3m$.

## Input
The first line contains two integers $n$ and $m$ — the number of antennas and the number of line-of-sight links ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). The antennas are indexed from $1$ to $n$.
Each of the subsequent $m$ lines provides two distinct integers $u$ and $v$ ($1 \le u, v \le n$), indicating that antenna $u$ and antenna $v$ share a direct line-of-sight link. 

## Output
If a stabilized configuration is impossible, output a single line containing NO.
If a valid configuration exists, output YES on the first line. On the second line, output $n$ space-separated integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the operational mode assigned to antenna $i$. Any valid configuration will be accepted.

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