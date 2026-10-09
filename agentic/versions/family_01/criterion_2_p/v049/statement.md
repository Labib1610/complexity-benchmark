# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant employs $n$ workers, identified by integers from 1 to $n$. Operations rely on specialized equipment, and the plant maintains a log of $m$ equipment-sharing conflicts. Each conflict record lists two workers who need the same machinery. A strict safety regulation dictates that for any conflict record, the two workers it lists must be scheduled for different shifts.

The plant operates on a two-shift system, consisting only of shift 1 and shift 2. Every worker must be placed into exactly one of these two shifts.

Your objective is to determine if a complete schedule can be formed that respects all safety regulations. If such an arrangement is possible, you must provide it. When multiple valid schedules exist, you must output the schedule that produces the lexicographically smallest sequence of shift numbers for workers 1 through $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of workers and the number of conflict records.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of workers involved in a conflict record.

## Output
If no valid schedule can be formed without violating the safety regulations, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the shifts assigned to workers 1 through $n$. If there are multiple valid schedules, output the sequence that is lexicographically smallest.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
