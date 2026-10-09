# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

The manufacturing plant operates using two time shifts, shift 1 and shift 2. However, the current assignment requirements cannot be fulfilled. Your task is to provide the proof that no valid assignment exists.

We are given $n$ machine operators and $m$ records of tool sharing. Each record indicates that two specific operators require the same specialized tool and therefore cannot work during the same shift. 

The provided list of requirements is impossible to satisfy because there is at least one collection of three operators where every possible pair chosen from those three individuals appears as a tool-sharing record. Because they all mutually restrict each other from working the same shift, they cannot be divided into only two shifts. You must identify one such group of three operators to certify the impossibility of the schedule.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a pair of operators who share a tool.
It is guaranteed that at least one group of three operators, where all three share tools with one another, exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$, such that the operators $a$, $b$, and $c$ all mutually share tools (i.e., the input contains a record for the pair $a$ and $b$, a record for the pair $a$ and $c$, and a record for the pair $b$ and $c$). Output the lexicographically smallest such group (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
