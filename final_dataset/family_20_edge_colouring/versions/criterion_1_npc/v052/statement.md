# Problem A — Power Grid Maintenance Shifts

Time limit: 5 s   Memory limit: 256 MB

## Description
The city's underground power grid consists of distribution vaults connected by high-voltage pipelines. The grid has been constructed under strict zoning laws: if you trace the connections from any distribution vault, you will always find exactly three pipelines attached to it.

The maintenance authority operates on a three-shift rotation (Shift 1, Shift 2, and Shift 3). Each pipeline must be completely shut down for maintenance during exactly one of these shifts. 

To prevent a blackout, a vault's safety breaker will trip if more than one of its connected pipelines is disabled during the same shift. You must find an assignment of shifts to pipelines such that no safety breaker trips anywhere in the grid. If such an assignment is possible, the maintenance plan can be executed. Otherwise, the grid must be redesigned.

## Input
The first line contains two integers `n` and `m` (`n` is even, `m = 3n/2`, `2 ≤ n ≤ 2000`), representing the number of distribution vaults and high-voltage pipelines, respectively.
The following `m` lines each contain two integers `u` and `v` (`1 ≤ u < v ≤ n`), indicating a pipeline connecting vault `u` and vault `v`.

## Output
If a valid maintenance schedule can be formed, print `YES` on the first line. On the second line, print `m` integers, each either `1`, `2`, or `3`, representing the shift assigned to each pipeline in the exact order they were provided in the input. If multiple valid schedules exist, any may be printed.
If it is impossible to schedule the maintenance without tripping a breaker, print `NO`.

## Example
### Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
### Output:
```
YES
1 2 3 3 2 1
```
