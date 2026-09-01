# Problem C — Processor Allocation Audit

Time limit: 2 s
Memory limit: 256 MB

You are auditing a task scheduler that distributes $n$ processes across two identical processors. The scheduler receives a list of $m$ mutual exclusion constraints. Each constraint specifies that a particular pair of processes cannot be assigned to the same processor due to resource conflicts.

The current list of constraints makes it impossible to schedule all processes on just two processors. To demonstrate this flaw, you must extract a minimal failing subset consisting of exactly three processes. 

Specifically, you need to find three distinct processes such that each process in the group has a mutual exclusion constraint with both of the other two processes in the group. Because there are only two processors available, any attempt to allocate these three processes will inevitably place at least one constrained pair on the same processor.

It is guaranteed that the provided constraints contain at least one such group of three processes. The provided logs can be highly skewed: in some configurations, the processes with the smallest identifiers will have a dense web of mutual exclusion constraints that never form a failing group of three, while the only valid failing subset consists entirely of the largest identifiers. Your task is to find and report the correct subset.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of processes and the number of mutual exclusion constraints. Processes are numbered from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a mutual exclusion constraint between process $u$ and process $v$. It is guaranteed that at least one such group of three processes exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, representing the identifiers of the three processes that form the failing subset. 

The identifiers must be printed in ascending order ($a < b < c$). If there are multiple valid groups of three processes, you must output the one that is lexicographically smallest. This means you should first minimize $a$; if there are ties, minimize $b$ among those ties; and if there are still ties, minimize $c$.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
2 4
3 4
```
**Output:**
```
1 2 3
```

## Example 2
**Input:**
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
**Output:**
```
1 2 4
```