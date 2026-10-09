# Problem A — Execution Tiers

Time limit: 2 s   Memory limit: 256 MB

A system consists of $n$ processes, numbered 1 through $n$. Each process $i$ must be assigned an execution tier $s_i$. To meet the system's operational parameters, each assigned tier $s_i$ must be an integer satisfying $1 \le s_i \le 3$.

You are provided with a list of $m$ interference constraints. Each constraint specifies two processes $u$ and $v$ that run concurrently. To prevent resource collisions, the execution tiers of any two concurrently running processes $u$ and $v$ must satisfy the condition $|s_u - s_v| \ge 1$.

Determine whether it is possible to assign a valid execution tier to every process such that all interference constraints are satisfied.

## Input
The first line contains two integers $n$ and $m$ — the number of processes and the number of interference constraints ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the identifiers of two processes that are constrained.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each satisfying $1 \le s_i \le 3$), where $s_i$ is the execution tier of process $i$. Any valid assignment is accepted.

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
