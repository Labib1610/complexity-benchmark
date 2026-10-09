# Problem A — Balanced Machines

Time limit: 5 s   Memory limit: 256 MB

## Description

There are **n** tasks; task **i** takes **d[i]** units of time. You have two identical machines. Each task must be assigned to exactly one of the two machines. Decide whether the tasks can be split so that the **total time on each machine is equal**, and if so report one valid assignment.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 40).
The second line contains **n** integers **d[1] … d[n]** (1 ≤ d[i] ≤ 1000000000), the task durations.

## Output

If the tasks can be split so both machines have equal total time, print `YES` on the first line, then on the second line print the indices of the tasks assigned to the first machine, separated by spaces (the remaining tasks go to the second machine). Any assignment that makes the two machine totals equal is accepted. If the first machine is empty in your assignment, leave the second line blank.

If no equal split exists, print `NO`.

## Examples

### Example 1

**Input**
```
4
3 1 2 2
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
4
1 1 1 5
```

**Output**
```
NO
```

### Example 3

**Input**
```
1
5
```

**Output**
```
NO
```

## Note

In Example 1, machine one gets tasks 1 and 2 (time 3+1 = 4) and machine two gets tasks 3 and 4 (time 2+2 = 4). In Example 2 the total time is 8 but no group of tasks sums to 4.
