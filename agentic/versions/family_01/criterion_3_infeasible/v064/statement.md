# Problem C — Task Force Selection

Time limit: 2 s
Memory limit: 256 MB

A network of $n$ agents is evaluating potential task forces. A task force is defined as a subset $S$ of agents. For a task force to be valid, every possible pair of distinct agents within $S$ must share a direct, bidirectional communication link.

The total number of possible agent subsets is $2^n$. When restricting the search to task forces of a fixed size $k$, the space of candidate subsets is exactly $\binom{n}{k}$. Your system must process the network topology to find a valid configuration of size exactly $k = 3$ for the upcoming operation. You are provided with the complete list of active communication links between agents. Diagnostics confirm that at least one such valid task force exists.

Your task is to identify a valid task force of the required size. If multiple valid configurations exist, you must report the lexicographically first one.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of agents and the number of active communication links, respectively. Agents are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that a bidirectional link exists between agent $u$ and agent $v$.
It is guaranteed that at least one valid task force of size 3 exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the identifiers of the agents in the selected task force.
The identifiers must be printed in ascending order ($a < b < c$).
To satisfy the lexicographical requirement, you must minimize $a$. If there are multiple valid task forces with the same $a$, minimize $b$. If there are still ties, minimize $c$.

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
