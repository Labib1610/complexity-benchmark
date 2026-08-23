# Problem C — Pipeline Stage 2: Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

The manufacturing plant uses a three-phase automated system to assign personnel: data parsing, viability checking, and shift assignment. Your module handles viability checking.

The plant operates on a strict two-shift system (Shift 1 and Shift 2). However, the parsed incompatibility data is known to be unresolvable. Your task is not to assign shifts, but to produce a certificate of failure.

The ingested data is guaranteed to contain at least one group of three personnel where every individual in the group is incompatible with the other two. The existence of such a trio mathematically prevents a valid two-shift assignment. You must find one such trio to send to the error-logging service.

To ensure the viability checker does not exceed memory limits, the data parsing phase guarantees the following structural properties on the input:
- No individual staff member is paired with more than $n-1$ distinct colleagues.
- There are at least three staff members who each appear in two or more incompatibility pairs.
- The sum of the appearances of all staff members across the $m$ pairs is exactly $2m$.

## Input
The first line provides $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of staff members and the number of incompatibility pairs.
The following $m$ lines each contain two integers $u$ and $v$ — an incompatible pair.
It is guaranteed that at least one mutually incompatible trio exists.

## Output
Provide three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, such that the pairs $a-b$, $a-c$, and $b-c$ are all listed as incompatibilities. If multiple such trios exist, output the one that is lexicographically smallest (the one with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

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
