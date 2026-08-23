# Audit Pipeline Phase 2: Bottleneck Identification

Time limit: 2 s   Memory limit: 256 MB

As part of an automated workforce management audit system, a facility uses a multi-stage workflow to evaluate shift allocation constraints:

1. **Ingestion Phase**: Collect worker profiles (indexed $1$ through $n$) and a master record of $m$ pairwise worker conflicts. Two conflicting workers cannot be assigned to the same shift.
2. **Bottleneck Isolation Phase**: Identify a core bottleneck—a set of three distinct workers where every pair within the set conflicts with each other. This mutually conflicting group serves as proof that the entire workforce cannot be scheduled across at most two shifts.
3. **Escalation Phase**: Dispatch an exception report to management detailing the primary bottleneck identified in Phase 2.

Your task is to implement the **Bottleneck Isolation Phase**. Given the worker conflict data, find three workers $a, b, c$ with $a < b < c$ such that all three pairs ($a$–$b$, $a$–$c$, and $b$–$c$) are listed conflicts. If multiple such groups exist, output the lexicographically smallest one (smallest $a$; if tied, smallest $b$; if still tied, smallest $c$).

## Input

The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of workers and the number of conflict pairs, respectively.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a conflicting pair of workers.

It is guaranteed that at least one such group of three mutually conflicting workers exists in the input.

## Output

Print three space-separated integers $a$, $b$, and $c$ on a single line ($a < b < c$) representing the lexicographically smallest triple of mutually conflicting workers.

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
