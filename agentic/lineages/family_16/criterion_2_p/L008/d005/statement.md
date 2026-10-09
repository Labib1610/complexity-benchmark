# Problem B — Expedition Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

An expedition needs to process **j** sectors. For each sector, you are given an energy requirement **p1** and an energy yield **p2**.

You must arrange the **j** sectors into a single linear sequence. As the expedition processes your sequence sector by sector, it maintains a `battery charge` (initially 0) and an `accumulated cost` (initially 0).

For each sector in your sequence, the following steps occur in this exact order:
1. The sector requires **p1** units of energy. If the current `battery charge` is strictly less than **p1**, the expedition draws the exact shortfall from an auxiliary grid. This shortfall is recorded as the `grid draw` for this sector. (If the `battery charge` is sufficient, the `grid draw` is 0).
2. The `battery charge` is updated to `max(0, battery charge - p1)`.
3. The sector then yields **p2** units of energy, which is added to the `battery charge`.
4. The `accumulated cost` is increased by the `grid draw` and then also increased by the **p2** yield.

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
- Processing the third sector (1, 3): The charge is 0, requirement p1 is 1. The shortfall is 1, so `grid draw` is 1. The charge updates to max(0, 0 - 1) = 0. Then p2 (3) is added, making the charge 3. The `accumulated cost` increases by 1 (grid draw) + 3 (p2) = 4.
- Processing the second sector (2, 4): The charge is 3, requirement p1 is 2. The charge is sufficient, so `grid draw` is 0. The charge updates to max(0, 3 - 2) = 1. Then p2 (4) is added, making the charge 5. The `accumulated cost` increases by 0 (grid draw) + 4 (p2) = 4 (becoming 8).
- Processing the first sector (3, 2): The charge is 5, requirement p1 is 3. The charge is sufficient, so `grid draw` is 0. The charge updates to max(0, 5 - 3) = 2. Then p2 (2) is added, making the charge 4. The `accumulated cost` increases by 0 (grid draw) + 2 (p2) = 2 (becoming 10).
The final `accumulated cost` is 10, which is the overall completion metric.

In Example 2, processing the single sector (5, 3):
- The charge is 0, requirement p1 is 5. The shortfall is 5, so `grid draw` is 5. The charge updates to max(0, 0 - 5) = 0. Then p2 (3) is added, making the charge 3. The `accumulated cost` increases by 5 (grid draw) + 3 (p2) = 8.
The overall completion metric is 8.