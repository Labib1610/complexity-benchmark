# Problem C — Incompatible Roster Certificate

Time limit: 2 s
Memory limit: 256 MB

The manufacturing plant operates using exactly two daily shifts. However, the proposed personnel roster is fundamentally flawed. You are not required to generate a working schedule; your task is solely to provide a certificate of its impossibility. 

Management has compiled a list of worker incompatibilities. It is mathematically certain that within these records, there exists at least one group of three workers who mutually clash with each other. The presence of any such trio unequivocally proves that two shifts are insufficient. 

To aid your processing, the system guarantees the following structural properties about the input data:
- The sum of the number of incompatibilities each worker is involved in, across all workers, will not exceed 400,000.
- The total number of given incompatible pairs $m$ will always be strictly less than $n^2$.

Your program must find and output one such trio of workers.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair of workers.
It is guaranteed that at least one mutually incompatible trio exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are incompatibilities. Output the lexicographically smallest such trio (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
