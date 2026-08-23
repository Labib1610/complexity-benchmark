# Problem C — Flight Manifest Rejection

Time limit: 2 s   Memory limit: 256 MB

A cargo company relies on two transport planes to ship various industrial chemicals. Certain pairs of chemicals are flagged in a safety database as incompatible and cannot share a plane.

The current shipping manifest cannot be divided between just two planes. To generate an automated safety rejection report, you must provide a minimal proof of this impossibility. You do not need to attempt a safe allocation.

Specifically, you must identify three distinct chemical IDs, $a$, $b$, and $c$, such that the database contains an incompatibility flag for $a$ and $b$, an incompatibility flag for $b$ and $c$, and an incompatibility flag for $a$ and $c$. Because these three specific flags prevent any two of the three chemicals from sharing a plane, they prove that at least three planes are required.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of chemicals and the number of incompatible pairs in the database. Chemicals are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that an incompatibility flag exists for chemicals $u$ and $v$.
It is guaranteed that the data contains at least one set of three chemicals satisfying the rejection criteria.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of the three chemicals that form the proof.
If there are multiple valid sets of three chemicals, output the one that is lexicographically smallest (i.e., smallest $a$; ties broken by smallest $b$; then smallest $c$).

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