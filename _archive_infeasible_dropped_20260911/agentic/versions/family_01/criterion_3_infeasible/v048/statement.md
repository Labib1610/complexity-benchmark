# Shift Allocation Audit

Time limit: 2 s
Memory limit: 256 MB

The manufacturing plant operates using exactly two daily shifts. Management has collected a list of incompatibilities between certain pairs of employees who cannot be assigned to the same shift.

An external audit has determined that the provided incompatibility list makes it entirely impossible to assign every employee to one of the two shifts without a violation. Specifically, the data contains at least one triplet of employees where every individual in the triplet is incompatible with both of the other two. Such a triplet forms an undeniable proof that two shifts are inadequate. 

Your task is to identify one such triplet to serve as the certificate of impossibility. 

Furthermore, the data collection process guarantees the following structural properties: no single employee is listed in 2000 or more incompatibilities, and the sum of the number of incompatibilities per employee across the entire plant is at most 400,000.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair.
It is guaranteed that at least one such triplet exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are incompatibilities. Output the lexicographically smallest such triplet (smallest $a$; ties by smallest $b$; then smallest $c$).

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```
