# Problem C — Odd Total

Time limit: 1 s   Memory limit: 256 MB

## Description

There are **n** tasks; task **i** takes **d[i]** units of time. You have two identical machines, and each task must be assigned to exactly one of them. You want to split the tasks so that the **total time on each machine is equal**.

In the input you are given, the sum of all durations is **odd**. Two equal whole-number totals must add up to an even number, so an odd total can never be split into two equal parts.

Determine whether an equal split exists.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 200000).
The second line contains **n** integers **d[1] … d[n]** (1 ≤ d[i] ≤ 1000000000), the task durations. Their total is guaranteed to be odd.

## Output

Print a single line containing `NO`, since the tasks cannot be split into two equal totals.

## Examples

### Example 1

**Input**
```
3
1 2 4
```

**Output**
```
NO
```

### Example 2

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

In Example 1 the total time is 7, which is odd and therefore cannot be divided into two equal whole-number halves.
