# Problem A — Orbital Resonance Alignment

Time limit: 2 s   Memory limit: 256 MB

A space station has $n$ stabilizing gyroscopes. To maintain operational equilibrium, each gyroscope must be tuned to a frequency band $s_i \in \{1, 2, 3\}$.

The station's structural integrity depends on $m$ critical load-bearing struts, each connecting a specific pair of gyroscopes. The interaction between connected gyroscopes generates a resonance drift.

For a strut connecting gyroscope $u$ and gyroscope $v$, the resonance drift $D_{u,v}$ is calculated using the following orbital mechanics formula:
$D_{u,v} = (s_u^2 + s_v^2) \pmod{s_u \times s_v}$

The total system drift $W$ is the sum of the resonance drifts across all $m$ struts:
$W = \sum_{j=1}^m D_{u_j, v_j}$

To maintain perfect structural stability, the total system drift must be exactly equal to the number of struts. (That is, $W = m$).

Your task is to determine whether there exists a valid frequency assignment for all gyroscopes $1 \dots n$ such that the total system drift $W$ is exactly $m$. If such an assignment exists, you must provide one.

## Input
The first line contains two integers $n$ and $m$ — the number of gyroscopes and the number of struts ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a strut connecting gyroscope $u$ and gyroscope $v$. Each strut is listed at most once.

## Output
If it is impossible to align the gyroscopes to the required drift state, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), with $s_i$ representing the frequency band assigned to gyroscope $i$. Any valid assignment is accepted.

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
*Explanation for Example 1:*
Assigning frequency bands 1, 2, 3, 3 yields the following resonance drifts:
- Strut (1, 2) with bands 1 and 2: $D_{1,2} = (1^2 + 2^2) \pmod{1 \times 2} = 5 \pmod 2 = 1$.
- Strut (1, 3) with bands 1 and 3: $D_{1,3} = (1^2 + 3^2) \pmod{1 \times 3} = 10 \pmod 3 = 1$.
- Strut (2, 3) with bands 2 and 3: $D_{2,3} = (2^2 + 3^2) \pmod{2 \times 3} = 13 \pmod 6 = 1$.
- Strut (1, 4) with bands 1 and 3: $D_{1,4} = (1^2 + 3^2) \pmod{1 \times 3} = 10 \pmod 3 = 1$.
- Strut (2, 4) with bands 2 and 3: $D_{2,4} = (2^2 + 3^2) \pmod{2 \times 3} = 13 \pmod 6 = 1$.

The total system drift $W$ is $1 + 1 + 1 + 1 + 1 = 5$. Since $m = 5$, the configuration achieves the target drift and is stable.

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