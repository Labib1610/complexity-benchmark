# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

A factory operates on a strict two-shift system. Management has collected a list of employee pairs who have filed grievances against each other and cannot be placed on the same shift. It has become clear that no valid schedule exists that satisfies all these constraints. 

Your job is not to attempt to build a schedule, but to officially cancel the roster plan by providing a formal proof of impossibility. A proof consists of exactly three employees who mutually cannot work with one another (each has a grievance against the other two). Any such trio proves that two shifts are insufficient. Your task is to identify one such trio.

## Input
The first line contains two integers $n$ and $m$, representing the headcount and the number of grievance records. The factory requires a minimum headcount of $3$ to operate, but its physical capacity limits $n$ to at most $2000$ employees. The grievance system has logged $m$ conflicts; there are always at least $3$ records, and the system's database caps this at $200000$ records (or the maximum possible number of unique pairs among the $n$ employees, whichever is fewer).

Each of the next $m$ lines contains two integers $u$ and $v$ — the identifiers (from $1$ to $n$) of two employees who refuse to share a shift.

It is guaranteed that the provided grievance logs contain at least one valid proof of impossibility.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that $a$ cannot work with $b$, $a$ cannot work with $c$, and $b$ cannot work with $c$. Output the lexicographically smallest such group (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
