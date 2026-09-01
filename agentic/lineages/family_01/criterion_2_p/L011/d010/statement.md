# Power Grid Synchronization

Time limit: 1 s
Memory limit: 256 MB

You are deploying a cluster of $n$ processing units. Each unit $i$ must be configured with a power state $s_i \in \{1, 2\}$.

The cluster contains $m$ bidirectional data links between units. For each unit $i$, let $d_i$ be the number of data link endpoints connected to it. (A link between distinct units $u$ and $v$ provides one endpoint to $u$ and one to $v$; a link connecting a unit to itself provides two endpoints to that unit).

Based on the configuration, we define two values for each unit $i$:
- The **local potential** is calculated as $d_i \times s_i$.
- The **neighborhood potential** is the sum of the power states of the units at the other end of each of its $d_i$ links. (If multiple links connect the same pair of units, each link contributes to the sum independently).

To prevent overheating while maintaining performance, the cluster achieves optimal equilibrium if and only if, for every unit $i$, the sum of its local potential and its neighborhood potential is exactly $3 \times d_i$.

Your task is to determine a valid power state configuration for all $n$ units such that the cluster reaches optimal equilibrium. If there are multiple valid configurations, you must output the one that produces the lexicographically smallest sequence of power states $s_1, s_2, \dots, s_n$. If it is impossible to satisfy the requirement, report that no such configuration exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a data link exists between unit $u$ and unit $v$.

## Output
If there is no valid configuration, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $s_1, s_2, \dots, s_n$, representing the lexicographically smallest valid sequence of power states.

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