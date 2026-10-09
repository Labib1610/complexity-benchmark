# Problem B — Archive Migration

Time limit: 1 s   Memory limit: 256 MB

## Description

A data migration project requires transferring **j** independent archives from a legacy system to a new platform. The transfer of each archive involves two sequential phases: extraction and integration. A single extraction server handles the first phase, and a single integration server handles the second phase. For each archive, you are provided the time required to extract it and the time required to integrate it.

The migration follows these operational rules:
- Each server processes exactly one archive at a time.
- The integration of an archive can only begin after its extraction is completely finished.
- You must establish a single processing sequence for the archives. Both servers process the archives in this exact chosen sequence.

Your goal is to choose the sequence that minimizes the total time elapsed from the start of the first extraction until the final archive finishes integration. Calculate and output this minimum possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **e** and **i** (1 ≤ e, i ≤ 1000000): the extraction time and the integration time of an archive.

## Output

Print a single integer: the minimum possible time at which the integration of all archives is complete.

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

In Example 2, the single archive takes 5 units of time to extract and then 3 units to integrate, finishing at time 8.
