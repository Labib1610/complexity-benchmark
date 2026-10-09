# Problem A — Trichrome Shifts

Time limit: 2 s
Memory limit: 256 MB

A manufacturing plant operates with three distinct daily schedules, designated by the identifiers 1, 2, and 3. The plant employs $n$ workers. Due to interpersonal grievances, certain pairs of workers are incompatible and cannot be present at the facility during the same schedule. 

Furthermore, the factory management guarantees that the average number of incompatibilities per worker is strictly less than $n$.

Management requires a schedule allocation that satisfies all of the following regulatory constraints:
- Each of the $n$ workers must be allocated exactly one of the three schedules.
- No two incompatible workers may be allocated the exact same schedule.
- The total headcount for any single schedule must not exceed $n$ workers.
- The sum of the schedule identifiers assigned to the workforce must be at least $n$ and at most $3n$.

Determine if there exists a valid allocation of workers to schedules that satisfies all regulations. If it is impossible, report so.

## Input
The first line of the input contains two integers $n$ and $m$ — the total number of workers and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$).
The following $m$ lines each contain two integers $u$ and $v$, representing a pair of workers who have a grievance with each other ($1 \le u, v \le n$, $u \neq v$). Each unordered pair is listed at most once.

## Output
If there is no allocation that satisfies all regulations, output `NO` on a single line.
If a valid allocation exists, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{1, 2, 3\}$ is the schedule identifier allocated to worker $i$. Any valid allocation that satisfies all constraints is accepted.

## Example 1
### Input
```
4 5
1 2
1 3
2 3
1 4
2 4
```
### Output
```
YES
1 2 3 3
```

## Example 2
### Input
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
### Output
```
NO
```
