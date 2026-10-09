# Problem B — Production Line Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing facility runs $n$ distinct machines. Each machine must be securely locked into one of two states: mode 1 or mode 0. The facility's power grid is safeguarded by $m$ safety interlocks. Each interlock monitors a pair of reference conditions.

A reference condition depends on a specific machine being in a specific mode. The fundamental safety protocol of the facility dictates that an interlock will trip a catastrophic shutdown if both of its monitored reference conditions are violated at the same time. To keep the facility running, the overall configuration must prevent this simultaneous violation across all $m$ interlocks.

Determine if a safe facility-wide configuration exists, and if so, output the required mode for each machine.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of machines and the number of safety interlocks, respectively.

The next $m$ lines each contain two non-zero integers $c_1$ and $c_2$ ($|c_i| \le n$), detailing the reference conditions for that interlock. A positive value $c_i > 0$ means the reference condition is "machine $c_i$ is in mode 1". A negative value $c_i < 0$ means the reference condition is "machine $|c_i|$ is in mode 0". 

Remember that safe operation requires avoiding the scenario where a machine configuration fails to match $c_1$ while simultaneously failing to match $c_2$.

## Output
If it is impossible to configure all $n$ machines without causing a shutdown, output a single line with the word `NO`.

If a safe configuration is possible, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) to specify the chosen mode for each machine from 1 to $n$.

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
There might be several safe configurations; outputting any valid one is correct. A single machine can be involved in the reference conditions of multiple interlocks.