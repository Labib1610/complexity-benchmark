# Day and Night

**Time limit:** 1 s  
**Memory limit:** 256 MB

## Description

A manufacturing plant operates two distinct shifts, labeled 1 and 2. The plant employs $n$ workers, numbered 1 through $n$. There are $m$ pairs of workers who have interpersonal conflicts and cannot be assigned to the same shift.

Your task is to assign every worker to either shift 1 or shift 2 such that no conflicting pair of workers shares the same shift.

Additionally, the operational policy specifies:
- Any worker who has no conflicts with any other worker must be assigned to shift 1.

If multiple valid shift assignments satisfy all conditions, you must output the lexicographically smallest sequence $s_1, s_2, \dots, s_n$. If no valid assignment is possible, report this outcome.

## Input

The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of workers and the number of conflict pairs, respectively.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that worker $u$ and worker $v$ cannot be assigned to the same shift.

## Output

If no valid shift assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid shift schedule.

## Example 1

### Input
```
4 4
1 2
2 3
3 4
1 4
```

### Output
```
YES
1 2 1 2
```

## Example 2

### Input
```
3 3
1 2
1 3
2 3
```

### Output
```
NO
```
