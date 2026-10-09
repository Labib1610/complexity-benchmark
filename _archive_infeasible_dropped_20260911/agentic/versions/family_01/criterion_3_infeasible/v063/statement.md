# Deployment Conflict

Time limit: 2 s   Memory limit: 256 MB

A quantitative finance firm has developed $n$ algorithmic trading bots. The infrastructure team plans to deploy each bot into exactly one of two isolated execution environments. 

However, certain pairs of bots target the same liquidity pools. If deployed in the same environment, they will trigger race conditions. The infrastructure team has compiled a list of these conflicting pairs, which must be assigned to different environments.

The deployment has been halted because the team realized that no valid assignment into two environments is possible. Your task is to extract a simple proof of this impossibility. Specifically, you must identify a closed loop of exactly three conflicting bots: a sequence of three distinct bots where the first conflicts with the second, the second conflicts with the third, and the third conflicts with the first. Since there are only two environments available, any such trio guarantees that at least two of its bots would be forced into the same environment.

It is guaranteed that the provided list of conflicts contains at least one such trio.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of bots and the total number of conflicting pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that bot $u$ and bot $v$ target the same liquidity pools and will conflict if placed in the same environment.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the IDs of the three bots in the trio. The IDs must be printed in strictly increasing order ($a < b < c$).

If there are multiple valid trios, output the one that minimizes $a$. If there is still a tie, minimize $b$, and if a tie remains, minimize $c$.

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
