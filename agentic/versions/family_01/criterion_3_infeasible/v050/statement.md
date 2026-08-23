# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

At the manufacturing plant, the human resources department maintains a registry of schedule conflicts. Specifically, there are $n$ employees, and the department has identified $m$ specific pairs of individuals who have overlapping external obligations and are therefore prohibited from working simultaneously on the same assembly line.

Management has mandated that the entire workforce be partitioned into exactly two distinct assembly lines. However, an internal audit has revealed that the current density of conflicts makes this proposed two-line arrangement unachievable. Rather than attempting an assignment, you are required to furnish a concrete justification for why the mandate cannot be fulfilled.

To formally document this failure, you must locate a trio of employees such that every individual in the trio has a recorded conflict with both of the other two members of that trio. The registry is guaranteed to contain at least one such trio. You must isolate and report one such group to serve as the proof of impossibility.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the following $m$ lines provides two integers $u$ and $v$ — a pair of employees with overlapping external obligations.
It is guaranteed that at least one trio of mutually conflicting employees exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$, representing a trio where the pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all present in the conflict registry. Output the lexicographically smallest such trio (the one with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

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
