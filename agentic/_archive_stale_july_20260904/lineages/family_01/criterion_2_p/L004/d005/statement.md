# Problem B — Microservice Capacity Scaling

Time limit: 1 s
Memory limit: 256 MB

A backend architecture consists of $n$ microservices. You must assign each microservice a replication factor of either 1 or 2.

The system processes $m$ synchronous workflows. Each workflow depends on a specific pair of microservices. The total capacity of a workflow is calculated as the product of the replication factors of the two microservices involved.

To meet strict latency requirements without causing resource contention, every workflow must have a total capacity of exactly 2.

Determine if it is possible to assign a valid replication factor to all $n$ microservices such that all $m$ workflows have a capacity of exactly 2.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of the two microservices that a workflow depends on.

## Output
If no valid assignment is possible, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $z_1 \dots z_n$ (where each $z_i \in \{1,2\}$) representing the valid assignment. If multiple valid assignments exist, output the lexicographically smallest sequence $z_1 \dots z_n$.

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