# Phase 2: Diagnostic Triplet Extraction

Time limit: 2 s   Memory limit: 256 MB

The automated resource allocator processes deployment requests in three phases. In Phase 1, it gathers all operational constraints from various departments to attempt a two-shift deployment schedule. When Phase 1 fails to find a valid two-shift assignment, the pipeline moves to Phase 2: Diagnostic Triplet Extraction.

You are implementing the Phase 2 module. The system has already determined that the current constraints make a two-shift schedule impossible. To generate an actionable error report for Phase 3 (where human supervisors will manually override constraints or authorize a third shift), your module must isolate a minimal core contradiction. Specifically, any group of three entities where every entity in the group has a constraint with both of the other two cannot possibly be divided into just two shifts. 

The Phase 1 module guarantees that the provided constraint data contains at least one such trio of mutually conflicting entities. Your module's sole responsibility is to identify one such trio and pass it to Phase 3.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), which represent the number of entities and the number of constraint pairs generated in Phase 1, respectively. Entities are identified by integers from $1$ to $n$.

Following this are $m$ lines, each containing two integers $u$ and $v$. This indicates a constraint where entity $u$ and entity $v$ must be assigned to different shifts.

It is guaranteed by Phase 1 that there is at least one group of three entities where every entity in the group has a constraint with both of the other two.

## Output
Output three integers $a$, $b$, and $c$ on a single line, representing the identifiers of the three conflicting entities, formatted such that $a < b < c$.

Because Phase 3 expects a deterministic diagnostic log, if multiple such trios exist, you must output the one that appears first lexicographically. This means you must minimize $a$; if there is a tie, minimize $b$; and if still tied, minimize $c$.

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
