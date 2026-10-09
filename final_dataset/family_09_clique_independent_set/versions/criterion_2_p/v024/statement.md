# Concurrent Job Selection

Time limit: 2 s
Memory limit: 256 MB

## Description

A server cluster must execute exactly **k** background jobs from a pool of **n** pending jobs. The jobs are identified by integers from 1 to **n**.

The execution planner has flagged **m** pairs of jobs that require exclusive access to the same database row, meaning they cannot both be selected for the concurrent batch.

The jobs are implicitly divided into two distinct processing tiers: data-ingestion and report-generation. A database row conflict only ever occurs between one data-ingestion job and one report-generation job. Two jobs of the same tier never conflict with each other. The tier of each job is not explicitly recorded in the input, but the provided conflict logs are guaranteed to perfectly follow this two-tier structure.

Your objective is to determine if it is possible to select exactly **k** jobs such that no two selected jobs share a database row conflict, and if so, to output one such valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 100000, 0 ≤ **m** ≤ 400000, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a database row conflict between job **u** and job **v**. No conflict is listed more than once. The conflicts are guaranteed to strictly adhere to the two-tier structure described above.

## Output

If a valid selection of **k** non-conflicting jobs exists, print `YES` on the first line. On the second line, print **k** distinct space-separated integers representing the selected job IDs. If multiple valid selections exist, any of them will be accepted.

If no such selection is possible, print `NO`.

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
