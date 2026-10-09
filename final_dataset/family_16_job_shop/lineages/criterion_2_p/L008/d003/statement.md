# Problem B — Expedition Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

An expedition needs to survey **j** distinct sectors. For each sector, you are given the duration required for its surface scan and the duration required for its deep core extraction.

You must arrange the **j** sectors into a single linear sequence. The expedition's operations will then unfold along two parallel tracks according to these synchronization rules:

- The surface scans are performed one by one, strictly following your chosen sequence. The scan of the first sector begins at time 0, and each subsequent scan begins immediately after the previous scan concludes.
- The deep core extractions are also performed one by one, strictly following your chosen sequence.
- The extraction for a given sector cannot commence until two prerequisites are satisfied: the surface scan of that specific sector must be complete, and the deep core extraction of the immediately preceding sector in your sequence (if applicable) must also be complete. Once both conditions are met, the extraction begins immediately.
- Once an operation (scan or extraction) begins on a sector, it runs continuously for its specified duration.

Determine the sequence of sectors that minimizes the time at which the deep core extraction of the final sector in the sequence is completed. Report that smallest possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations for a sector's surface scan and deep core extraction, respectively.

## Output

Print a single integer: the smallest possible time at which all sectors are completely finished.

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

In Example 2, the single sector undergoes a surface scan for 5 time units, followed by a deep core extraction for 3 time units, finishing at time 8.