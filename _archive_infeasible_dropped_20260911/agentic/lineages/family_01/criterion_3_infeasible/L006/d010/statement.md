# Problem C — Registry Resonance

Time limit: 2 s
Memory limit: 256 MB

You are analyzing a system of $n$ independent memory registries, numbered $1$ to $n$.
The system receives a sequence of $m$ synchronization pulses. Each pulse involves exactly two distinct registries. It is guaranteed that no two pulses involve the same pair of registries (the order of registries in a pulse does not matter).

A *resonance anomaly* occurs if there exists a set of three distinct registry IDs $\{x_1, x_2, x_3\}$ (where $x_1 < x_2 < x_3$) such that exactly three of the $m$ pulses have both of their involved registries within this set.

You must find the IDs involved in this anomaly. It is guaranteed that the sequence of pulses produces at least one such configuration.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 200000)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two registries involved in the pulse.
It is guaranteed that at least one resonance anomaly exists.

## Output
Print three integers $x_1$, $x_2$, and $x_3$ on one line with $x_1 < x_2 < x_3$. Output the lexicographically smallest such combination (smallest $x_1$; ties broken by smallest $x_2$; then smallest $x_3$).

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