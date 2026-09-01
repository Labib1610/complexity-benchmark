# Problem B — Energy State Configuration

Time limit: 1 s
Memory limit: 256 MB

A quantum system consists of $n$ nodes, indexed from 1 to $n$. A tuning configuration assigns each node a specific state, which must be either the integer 1 or the integer 2.

The laboratory maintains a record of $m$ links between these nodes. These links dictate the total energy of the system. To avoid destabilization, the system must achieve a perfectly stable energy level.
Let $r_1, r_2, \dots, r_n$ (where each $r_i \in \{1, 2\}$) be the sequence of assigned states.
Let $D_i$ be the total number of times node $i$ appears as an endpoint in the $m$ recorded links. (Note: if a record connects a node to itself, that node appears twice in that single record).
The total energy $E$ of the configuration is computed by the following formula:
$$E = \sum_{i=1}^n \left( 6 \cdot D_i \cdot r_i^2 \right) - \sum_{j=1}^m \left( 14 \cdot r_{u_j} \cdot r_{v_j} \right)$$
where $(u_j, v_j)$ represents the $j$-th recorded link.

The system is perfectly stable if and only if its total energy $E$ is exactly equal to $2m$. 

Your task is to determine a valid tuning configuration for all $n$ nodes that achieves this exact energy level $E = 2m$. If multiple valid configurations exist, you must output the one that produces a sequence $r_1, r_2, \dots, r_n$ that is lexicographically smaller than any other valid sequence. This means it must prioritize assigning 1 to node 1 if possible; then prioritize assigning 1 to node 2, and so on sequentially.

If no configuration can achieve the required energy $E = 2m$, you must report the failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), identifying a linked pair of nodes in the record.

## Output
If no tuning configuration can achieve the required energy, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $r_1, r_2, \dots, r_n$ (where each $r_i \in \{1, 2\}$) representing the state assigned to each respective node from 1 to $n$. This sequence must be the lexicographically smallest possible valid sequence.

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