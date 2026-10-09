# Archival Restoration

Time limit: 1 s   Memory limit: 256 MB

## Description

Within the restoration department of a historical archive, there are two distinct workstations: the transcription desk and the binding table. 

Work at the transcription desk is performed by a single calligrapher, who can only handle one manuscript at a time. Similarly, the binding table is operated by a single bookbinder, who also works on one manuscript at a time. A strict sequential dependency exists for every manuscript: it must first be fully transcribed at the desk before it can be moved to the table to be bound. 

Furthermore, the department enforces a strict procedural rule for any batch of **j** manuscripts: an ordering of the items must be established beforehand. Both the calligrapher and the bookbinder must process all **j** items in that exact same order. 

Given the time required to transcribe and to bind each manuscript, your task is to arrange them into a valid ordering such that the entire batch is completely restored (meaning the bookbinder has finished the final item) as early as possible. Calculate this earliest possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the time required to transcribe the manuscript at the desk, and the time required to bind it at the table, respectively.

## Output

Print a single integer: the smallest possible total time to finish binding the last manuscript.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single manuscript takes 5 units of time to transcribe and then 3 units of time to bind, finishing at time 8.
