# Phase 2: Audit Contradiction Extraction

Time limit: 2 s   Memory limit: 256 MB

Our automated workforce compliance pipeline consists of three phases. In Phase 1, the system parses union regulations and safety guidelines to generate a list of pairwise incompatibilities—pairs of staff members who cannot be assigned to the same operational shift. The facility operates on exactly two shifts.

Phase 1 has already determined that the given constraints cannot be satisfied with only two shifts. Your module is responsible for Phase 2: isolating a concrete contradiction to pass along to Phase 3, the automated reporting engine. To prove that two shifts are insufficient, your module must identify a triplet of employees where every individual in the triplet is incompatible with both of the other two.

Because the Phase 3 reporting engine requires deterministic input, if there are multiple such triplets, you must provide the one that comes first lexicographically.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of employees who cannot share a shift.
It is guaranteed that at least one triplet of mutually incompatible employees exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$, representing the IDs of the employees in the extracted triplet. The IDs must be printed in ascending order ($a < b < c$). If there are multiple valid triplets, output the one that minimizes $a$; if tied, minimizes $b$; and if still tied, minimizes $c$.

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
