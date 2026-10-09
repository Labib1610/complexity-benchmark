# Conflict-Free Project Team (Two Shifts)

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing plant employs **n** workers (numbered 1..n). The plant management has identified **m** personality conflicts among the workforce. Each conflict involves exactly two workers who cannot work together.

The plant operates on exactly **two shifts**. Every conflict connects a worker on one shift to a worker on the other — there are no conflicts between two workers on the same shift. (The shift rosters are not provided to you; you must deduce them from the conflict reports.)

A project team is considered **harmonious** if no two workers on the team have a conflict.

Given a target team size **k**, determine whether a harmonious project team of exactly **k** workers can be formed, and if so, list its members.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a conflict between two workers. No conflict is listed twice, and the conflicts are guaranteed to follow the two-shift structure described above (every conflict is between workers on different shifts).

## Output

If a harmonious team of **k** workers exists, print `YES` on the first line, then on the second line print **k** distinct worker numbers forming such a team, separated by spaces. Any team in which no two workers conflict is accepted.

If no such team exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```

## Note

In Example 1, workers 1 and 2 (being on the same shift) do not conflict. In Example 3, the largest harmonious team has only 2 workers, so a team of 3 is impossible.
