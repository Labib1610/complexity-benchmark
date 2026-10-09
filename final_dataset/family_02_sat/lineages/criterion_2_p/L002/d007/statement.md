# Problem B — Production Line Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing facility runs $n$ distinct machines. Each machine must be securely locked into one of two tension states: $s_i \in \{0, 1\}$.

The facility's power grid is safeguarded by $m$ safety interlocks. Each interlock receives two mechanical linkages from the machines. A linkage is defined by a non-zero integer $c$. The linkage's connected machine is given by its absolute value, $|c|$.

When a machine $u = |c|$ is configured to state $s_u$, the linkage transmits a mechanical torque $\tau$ to the interlock, determined by the equation:
$$\tau = c \cdot (2s_u - 1)$$

An interlock is designed to safely absorb torque, but it has a critical vulnerability. If the torques from *both* of its connected linkages are strictly negative, the interlock fractures and triggers a catastrophic facility-wide shutdown. 

To keep the facility operational, you must determine a facility-wide configuration (assigning state 0 or 1 to each machine) such that all $m$ interlocks remain intact. Determine if a safe configuration exists, and if so, output the required state for each machine.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of machines and the number of safety interlocks, respectively.

The next $m$ lines each contain two non-zero integers $c_1$ and $c_2$ ($|c_i| \le n$), detailing the two linkages for that interlock. 

## Output
If it is impossible to configure all $n$ machines without causing a shutdown, output a single line with the word `NO`.

If a safe configuration is possible, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) to specify the chosen tension state for each machine from 1 to $n$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
There might be several safe configurations; outputting any valid one is correct. A single machine can connect linkages to multiple interlocks.