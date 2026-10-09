# Problem A — Conflict-Free Committee

Time limit: 5 s   Memory limit: 256 MB

## Description

A corporate department has **n** employees (numbered 1..n) and a record of **m** documented conflicts. Each conflict involves two employees who refuse to work together.

A project committee is **conflict-free** if no two employees on the committee have a documented conflict (there is no conflict between any pair of them).

Given a target committee size **k**, decide whether a conflict-free committee of exactly **k** employees exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a documented conflict. No conflict is listed twice.

## Output

If a conflict-free committee of **k** employees exists, print `YES` on the first line, then on the second line print **k** distinct employee numbers forming such a committee, separated by spaces. Any committee in which no two employees have a conflict is accepted.

If no such committee exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

A conflict-free committee ensures no two chosen employees have a conflict. In Example 2, employees 1, 3 and 5 have no conflicts among them. In Example 1 no three of the four employees are mutually conflict-free.
