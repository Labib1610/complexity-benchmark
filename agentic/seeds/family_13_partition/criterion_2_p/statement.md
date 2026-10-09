# Problem B — Balanced Machines (Short Tasks)

Time limit: 2 s   Memory limit: 256 MB

## Description

A workshop splits **n** jobs across two identical benches, job i taking d[i] units of time, each job on exactly one bench, seeking an even division where both benches carry equal total time. Here the durations are all small, bounded within a modest range, so the achievable bench-totals form a compact set that can be enumerated directly. Decide whether an even split exists, and if so report one; otherwise report that none does.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 2000).
The second line contains **n** integers **d[1] … d[n]** (1 ≤ d[i] ≤ 100), the task durations.

## Output

If the tasks can be split so both machines have equal total time, print `YES` on the first line, then on the second line print the indices of the tasks assigned to the first machine, separated by spaces (the remaining tasks go to the second machine). Any assignment that makes the two machine totals equal is accepted. If the first machine is empty in your assignment, leave the second line blank.

If no equal split exists, print `NO`.

## Examples

### Example 1

**Input**
```
4
1 2 3 4
```

**Output**
```
YES
2 3
```

### Example 2

**Input**
```
5
2 2 2 2 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
6
10 20 30 40 50 50
```

**Output**
```
YES
1 4 5
```

## Note

In Example 1, machine one gets tasks 2 and 3 (time 2+3 = 5) and machine two gets tasks 1 and 4 (time 1+4 = 5). In Example 2 the total time is 10 but no group of tasks sums to 5.
