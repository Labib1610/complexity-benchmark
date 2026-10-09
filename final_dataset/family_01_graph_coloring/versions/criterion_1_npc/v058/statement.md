# Problem A — Operational Tier Configuration

Time limit: 2 s
Memory limit: 256 MB

A distributed computing environment contains $n$ processing nodes, which are identified by integers from 1 to $n$. The environment also includes $m$ direct communication bridges, each linking a specific pair of nodes.

To prevent data packet collisions, any two nodes that share a direct communication bridge must maintain a strict differential in their designated operating tiers. This means that if a bridge connects node $u$ and node $v$, their assigned tiers $t_u$ and $t_v$ must satisfy the condition $|t_u - t_v| \ge 1$. Furthermore, hardware limitations restrict the available operating tiers for any node to exactly three integer levels: 1, 2, and 3.

Your objective is to evaluate the provided layout of communication bridges and determine whether it is possible to assign a valid operating tier to every node in the environment. If such a configuration exists, you must output it; otherwise, you must report that the requirements are unsatisfiable.

## Input
The first line provides two integers $n$ and $m$ — representing the number of processing nodes and the number of communication bridges, respectively ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), specifying that a communication bridge exists between node $u$ and node $v$.

## Output
If it is impossible to assign operating tiers that satisfy all differential conditions, print a single line containing `NO`.
If a valid assignment is possible, print `YES` on the first line. On the second line, output $n$ space-separated integers $t_1, t_2, \dots, t_n$, where $t_i \in \{1, 2, 3\}$ is the operating tier assigned to node $i$. If multiple valid configurations exist, you may output any of them.

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
