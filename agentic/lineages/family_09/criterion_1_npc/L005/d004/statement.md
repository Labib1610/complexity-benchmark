# Problem A — Resource-Sharing Task Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

A processing system has a queue of **n** distinct jobs (numbered 1 to **n**). Due to hardware constraints, the system must select exactly **k** jobs to execute in the current batch.

There are **m** known hardware conflicts between certain jobs. A conflict happens if two specific jobs require exclusive access to the same hardware component. To ensure successful execution, the selected batch of **k** jobs must be completely conflict-free. This means that for every listed conflict pair (**u**, **v**), the selected batch cannot contain both job **u** and job **v**.

Given the total number of jobs **n**, the number of conflicts **m**, and the required batch size **k**, determine if a conflict-free batch of exactly **k** jobs can be selected, and if so, report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing two jobs that conflict with each other. The input will never list the same pair of jobs more than once.

## Output

If a conflict-free batch of **k** jobs exists, print `YES` on the first line, then on the second line print the **k** distinct job numbers to be executed, separated by spaces. If multiple conflict-free batches exist, any valid selection is accepted. Print only the **k** selected jobs.

If no such batch exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

In Example 2, selecting jobs 1, 3, and 5 is conflict-free. The first conflict requires both 1 and 2 to be selected (job 2 is not selected), and the second requires both 3 and 4 to be selected (job 4 is not selected). Thus, no conflicts are present in the batch.
In Example 1, any batch of 3 jobs will include both jobs from at least one conflict pair, meaning it is impossible to form a conflict-free batch.