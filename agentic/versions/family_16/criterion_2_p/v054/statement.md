# Problem B — Two-Stage Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing plant handles a daily manifest of production batches. The plant floor is divided into a preparation stage and a subsequent finishing stage. 

For every batch on the manifest, it must first be fully prepared in the preparation stage before it can be moved to the finishing stage. The plant operates under these strict conditions:

- Each stage can work on at most one batch at any given time.
- A batch cannot commence its finishing stage until its preparation stage is completely finished.
- To prevent logistical confusion, the plant manager mandates that the sequence in which the batches are processed must be identical across both stages. You must select one fixed ordering for all batches.

You are given the time required for each batch at both stages. Your objective is to arrange the batches into a single sequence that minimizes the total elapsed time from the start of the first batch's preparation until the final batch concludes its finishing stage. Report this earliest possible completion time.

## Input

The first line contains a single integer representing the number of production batches. The manifest will always contain at least one batch, and is restricted by the scheduling system's hard limit of two hundred thousand concurrent batches.

Each of the subsequent lines describes a single batch using two integers: the duration of its preparation stage followed by the duration of its finishing stage. A stage duration is always at least one time unit, and will never exceed the equipment's automatic safety cutoff of one million time units.

## Output

Print a single integer: the earliest possible time the entire manifest can be completed.

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

In Example 2, the single batch takes 5 units of time in the preparation stage and then 3 units in the finishing stage, concluding at time 8.
