# Problem C — Schema Conflict Certification

Time limit: 2 s   Memory limit: 256 MB

A distributed system consists of $n$ databases, numbered 1 through $n$. The architecture specifies that these databases must be divided into exactly two synchronization rings. However, certain pairs of databases have incompatible schemas and cannot be placed in the same ring.

Your task is not to attempt this division, but to certify that it is impossible. It is guaranteed that the system contains at least one set of three databases where each database in the set is incompatible with both of the other two. Any such triplet proves that two rings cannot suffice. Your job is to output one such triplet.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of incompatible databases.
It is guaranteed that at least one such triplet exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$-$b$, $a$-$c$, and $b$-$c$ are incompatible. Output the lexicographically smallest such triplet (smallest $a$; ties by smallest $b$; then smallest $c$).

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