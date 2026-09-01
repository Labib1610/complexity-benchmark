# Problem A — Sensor Network Telemetry

Time limit: 2 s   Memory limit: 256 MB

A research team is configuring a network of $n$ telemetry sensors. Each sensor $i$ must be programmed with a phase parameter $c_i$ selected from the set $\{1, 2, 3\}$.

Due to physical proximity, certain pairs of sensors interact. If two interacting sensors are assigned the exact same phase parameter, their signals will overlap and cause severe data loss. You are provided with a complete list of these interacting pairs.

Your task is to determine a sequence of phase parameters $c_1, c_2, \dots, c_n$ such that for every interacting pair $(u, v)$, their parameters satisfy $|c_u - c_v| \ge 1$. If no safe configuration is possible, you must report it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$) — the number of sensors and the number of interacting pairs. The sensors are numbered from 1 to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ — denoting that sensor $u$ and sensor $v$ interact with each other.

## Output
If no valid sequence of phase parameters exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$), with $c_i$ representing the phase parameter assigned to sensor $i$. Among all valid sequences, output the lexicographically smallest sequence (compare $c_1$ first, then $c_2$, and so on).

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