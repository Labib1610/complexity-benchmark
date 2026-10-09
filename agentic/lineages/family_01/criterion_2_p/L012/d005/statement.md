# Problem B — Power Scaling

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility employs $n$ robotic welders, identified by integers from 1 to $n$. The facility requires each welder to be configured with a calibration mode of exactly 1 or 2.

Over time, management has installed $m$ shared power buses. Each bus connects two specific welders. A strict operational rule dictates that to prevent electrical overload, the system must maintain local equilibrium. Specifically, for every welder $i$, let $k_i$ be the total number of buses connected to it. For each of these $k_i$ buses, consider the calibration mode of the welder at the other end. The sum of these $k_i$ calibration modes must evaluate to exactly $k_i \times (3 - s_i)$, where $s_i$ is the calibration mode assigned to welder $i$. (If a welder is not connected to any buses, this condition is considered satisfied).

Your task is to determine whether the entire set of welders can be configured in complete compliance with this operational rule. If a compliant configuration exists, you must provide the specific configuration sequence $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$). If multiple such compliant sequences exist, you must output the one that produces the smallest possible value when evaluated as the sum $\sum_{i=1}^n s_i \cdot 3^{n-i}$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a power bus connecting welder $u$ and welder $v$.

## Output
If there is no way to assign the calibration modes without violating the operational rule, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each either 1 or 2), representing the valid configuration sequence that minimizes the required sum.

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