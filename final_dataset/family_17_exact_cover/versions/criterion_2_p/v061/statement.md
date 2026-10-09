# Pipeline Dispatch Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
A data processing pipeline contains $2q$ distinct tasks, identified by integers from 1 to $2q$. To optimize execution, you must group the tasks into pairs that will be processed concurrently.

Due to memory access patterns, two tasks can only be paired if they cross the midpoint of the ID space. Specifically, every certified pair consists of one task with an ID in the range 1 through $q$, and one task with an ID in the range $q+1$ through $2q$. You are provided with a log of $t$ such certified pairs. The pipeline strictly enforces that only pairs explicitly listed in this log may be grouped together.

A full pipeline dispatch requires selecting a subset of these certified pairs such that every single task in the pipeline (from 1 to $2q$) is included in exactly one selected pair. 

Determine whether it is possible to configure a full pipeline dispatch. If it is achievable, output the pairs to be grouped; otherwise, indicate that it is impossible.

## Input
The first line contains two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000).
The next $t$ lines each contain two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), representing a certified pair between task $a$ and task $b$.

## Output
If a full pipeline dispatch is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of a selected pair. If it is impossible, print `NO`.

## Example 1
### Input
```
3 4
1 4
2 5
3 5
3 6
```
### Output
```
YES
1 4
2 5
3 6
```

## Example 2
### Input
```
2 2
1 3
2 3
```
### Output
```
NO
```
