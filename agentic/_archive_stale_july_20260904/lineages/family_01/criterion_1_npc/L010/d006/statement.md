# Problem A — Resonant Loop Prevention

Time limit: 2 s
Memory limit: 256 MB

You are configuring a system of $n$ signal relays, numbered 1 to $n$. Each relay must be assigned a frequency multiplier chosen from the values 1, 2, and 3. This configuration is expressed as a sequence $f_1, f_2, \dots, f_n$, where $f_i \in \{1, 2, 3\}$ is the multiplier for relay $i$.

To evaluate the system's stability, each relay $i$ is assigned a configuration vector based on its multiplier, defined as $C_i = (1, f_i, f_i^2)$.

You are provided with a list of $m$ pairs of relays that are in physical proximity. When two relays $u$ and $v$ are in proximity, their signals interact. They will create a destructive resonant loop if and only if the cross product of their configuration vectors, $C_u \times C_v$, results in the zero vector $(0, 0, 0)$.

Your task is to determine if there exists a valid sequence of multipliers such that absolutely no resonant loops are created among any of the given proximity pairs. If such a sequence exists, you must output it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that relay $u$ and relay $v$ are in physical proximity.

## Output
If there is no valid sequence of multipliers that avoids all resonant loops, print a single line containing `NO`.
If at least one such sequence exists, print `YES` on the first line. On the second line, print the $n$ integers $f_1, f_2, \dots, f_n$ representing the multipliers assigned to the relays. 
If there are multiple valid sequences, you must output the one that is lexicographically smallest. (A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first index $i$ where they differ, $A_i < B_i$).

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