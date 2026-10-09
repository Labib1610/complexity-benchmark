# Problem B — Expedition Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

An expedition needs to process **j** sectors. For each sector, you are given an energy requirement **p1** and an energy yield **p2**.

You must arrange the **j** sectors into a single linear sequence. As the expedition processes your sequence sector by sector, it maintains a `battery charge` (initially 0) and an `accumulated cost` (initially 0).

For each sector in your sequence, the following steps occur in this exact order:
1. The sector requires **p1** units of energy. The expedition allocates energy from the current `battery charge` to meet this requirement, up to the available charge. The allocated amount is exactly `min(p1, battery charge)`. Any unmet requirement is handled externally and does not deplete the battery further.
2. The `battery charge` is reduced by the allocated amount.
3. The sector yields **p2** units of energy, which is fully added to the `battery charge`.
4. The `accumulated cost` is increased by the sum of the sector's energy requirement and yield (**p1** + **p2**), and then decreased by the allocated amount from Step 1.

After all **j** sectors have been processed, the overall completion metric is the final `accumulated cost`.

Determine the sequence of sectors that minimizes this overall completion metric. Report that smallest possible metric.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the energy requirement and energy yield for a sector, respectively.

## Output

Print a single integer: the smallest possible overall completion metric.

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

In Example 1, one optimal sequence is the third sector, then the second, then the first.
- Processing the third sector (1, 3): The charge is 0, requirement p1 is 1. The allocated amount is min(1, 0) = 0. The charge reduces by 0 to 0. Then p2 (3) is added, making the charge 3. The `accumulated cost` increases by p1 (1) + p2 (3) - allocated (0) = 4.
- Processing the second sector (2, 4): The charge is 3, requirement p1 is 2. The allocated amount is min(2, 3) = 2. The charge reduces by 2 to 1. Then p2 (4) is added, making the charge 5. The `accumulated cost` increases by p1 (2) + p2 (4) - allocated (2) = 4 (becoming 8).
- Processing the first sector (3, 2): The charge is 5, requirement p1 is 3. The allocated amount is min(3, 5) = 3. The charge reduces by 3 to 2. Then p2 (2) is added, making the charge 4. The `accumulated cost` increases by p1 (3) + p2 (2) - allocated (3) = 2 (becoming 10).
The final `accumulated cost` is 10, which is the overall completion metric.

In Example 2, processing the single sector (5, 3):
- The charge is 0, requirement p1 is 5. The allocated amount is min(5, 0) = 0. The charge reduces by 0 to 0. Then p2 (3) is added, making the charge 3. The `accumulated cost` increases by p1 (5) + p2 (3) - allocated (0) = 8.
The overall completion metric is 8.