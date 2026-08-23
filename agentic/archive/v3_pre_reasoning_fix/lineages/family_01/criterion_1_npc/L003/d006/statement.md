# Problem A — Acoustic Drone Deployment

Time limit: 2 s   Memory limit: 256 MB

A fleet of $n$ deep-sea mining drones, numbered $1$ to $n$, is being deployed. Each drone must be assigned exactly one operational depth tier: $1$, $2$, or $3$.

Each depth tier $k \in \{1, 2, 3\}$ corresponds to a specific acoustic fingerprint, which is a sequence of three integers $F_{k,1}, F_{k,2}, F_{k,3}$. The $j$-th value of the fingerprint is given by the formula:
$F_{k,j} = (k \cdot j) \bmod 4$

During pre-deployment analysis, the system identified $m$ pairs of drones that will operate in overlapping acoustic zones. To prevent destructive sonar resonance, the mission controller enforces a wave separation rule. For any two drones $u$ and $v$ in an overlapping zone, assigned depth tiers $d_u$ and $d_v$ respectively, their fingerprints must satisfy the following condition:
$\sum_{j=1}^{3} |F_{d_u, j} - F_{d_v, j}| = 4$

The deployment configuration must be listed as a sequence of $n$ integers, where the $i$-th integer is the depth tier of drone $i$. To standardize deployment logs, if there are multiple valid configurations that satisfy the resonance rule, the system must generate the sequence that is lexicographically smallest.

If it is impossible to assign depth tiers to all drones without violating the resonance rule, the system must abort the deployment.

## Input
The first line contains two integers $n$ and $m$ — the number of drones and the number of pairs in overlapping zones ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of drones that share an acoustic zone and therefore must satisfy the acoustic fingerprint condition.

## Output
If no valid depth assignment is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $d_1, d_2, \dots, d_n$ (where each $d_i \in \{1, 2, 3\}$), representing the depth tier assigned to drone $i$. Among all valid assignments, output the sequence that is lexicographically smallest (compare $d_1$ first, then $d_2$, and so on).

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