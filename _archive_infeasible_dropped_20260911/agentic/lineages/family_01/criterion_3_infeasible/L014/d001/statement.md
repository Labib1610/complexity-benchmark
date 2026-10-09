# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

Two production shifts are available at the manufacturing plant. Some pairs of personnel cannot be assigned to the same operational period due to interpersonal disputes. The administration has already verified that the current staffing requirements are fundamentally flawed: the provided records always contain a group of three individuals where every person in the group disputes with both of the others. Such a configuration makes a two-shift assignment logically unattainable. 

Your task is not to create a schedule, but to identify one such group of three individuals to serve as evidence of the scheduling failure.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of personnel and the number of reported disputes, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of personnel who dispute each other.
The input data will always contain at least one trio of personnel who all mutually dispute one another.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$ such that all three pairs ($a$ and $b$, $a$ and $c$, $b$ and $c$) are in dispute. Output the lexicographically smallest such trio (minimize $a$; in case of a tie, minimize $b$; then minimize $c$).

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