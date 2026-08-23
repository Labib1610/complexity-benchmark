# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

The manufacturing plant is attempting to divide its workforce into two non-overlapping operating shifts. This division is currently blocked by a set of restriction protocols. Each restriction protocol is tied to a specific pair of employees, indicating they cannot function on the same shift.

Your task is to provide the formal documentation proving that a valid two-shift arrangement is unattainable. It is a known fact that the personnel records contain a specific localized failure: there exists at least one group of exactly three employees configured such that, if you select any two individuals from this group, you will find a restriction protocol linking them. Because no two individuals in this group can share a shift, assigning all three to only two shifts is impossible.

You must identify and output the members of one such group.

## Input
The first line provides the employee headcount $n$ and the number of restriction protocols $m$. The headcount $n$ ranges from 3 up to the facility capacity of 2000. The number of protocols $m$ is at least 3 and never exceeds the lesser of the total number of possible unique pairs among the $n$ employees and the database limit of 200000.
Each of the subsequent $m$ lines contains two integers $u$ and $v$, representing a restriction protocol between employee $u$ and employee $v$.
It is guaranteed that at least one group of three employees satisfying the failure condition exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$ with $a < b < c$, such that restriction protocols exist between $a$ and $b$, $a$ and $c$, and $b$ and $c$. You must output the group that comes first numerically (the smallest value for $a$; in case of a tie, the smallest value for $b$; and if still tied, the smallest value for $c$).

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
