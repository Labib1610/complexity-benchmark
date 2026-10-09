# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

A production floor is attempting to assign $n$ assembly workers to two distinct assembly lines. We are given $m$ conflict reports. Each report lists two workers who require the same calibration device, meaning they cannot be assigned to the same assembly line.

It has been determined that the workers cannot be validly split into two lines. To demonstrate why, you must locate a specific obstruction: a set of three workers where every possible pair chosen from those three individuals appears as a conflict report. Because each of the three restricts the other two from joining their line, they cannot be split across only two lines.

Find one such group of three workers to serve as evidence of this scheduling failure.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a pair of workers involved in a conflict report.
It is guaranteed that at least one group of three workers, where all three are pairwise reported in conflicts, exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$, such that the workers $a$, $b$, and $c$ all mutually conflict (i.e., the input contains a report for the pair $a$ and $b$, a report for the pair $a$ and $c$, and a report for the pair $b$ and $c$, regardless of the order they appear in the report). Output the lexicographically smallest such group (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
