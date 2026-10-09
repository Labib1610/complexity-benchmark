# Problem A — Greenhouse Climate Phase Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A botanical research facility needs to cultivate a batch of $n$ distinct crop varieties. The cultivation process is divided into a sequence of discrete climate phases. The facility has a strict mandate to complete the entire batch within $T$ phases.

During any single phase, the greenhouse provides exactly $M$ cultivation slots, meaning it can support the simultaneous cultivation of at most $M$ varieties. Each variety requires exactly one phase to complete its growth cycle. There is no benefit to leaving slots empty, but there is also no penalty as long as the total duration does not exceed $T$ phases.

The varieties have biological dependencies. Certain crops release specific soil nutrients that are strictly required by other crops. If variety $b$ requires nutrients from variety $a$, variety $a$ must be cultivated in a strictly earlier phase than variety $b$. Cultivating them in the same phase is insufficient, as the required nutrients are only fully integrated into the soil after the phase concludes. The specific physical location of a variety within the greenhouse during a phase is irrelevant; only the phase number matters.

You must assign exactly one phase (from 1 to $T$) to every variety such that all nutrient dependencies are satisfied and no phase is assigned more than $M$ varieties. Furthermore, any valid allocation must satisfy two additional administrative constraints:
- The total number of unused cultivation slots across all $T$ phases must evaluate to exactly $M \times T - n$.
- For any two crop varieties, the absolute difference between their assigned phase numbers cannot exceed $T - 1$.

If it is possible to allocate all varieties under these conditions, output the phase assignments. Otherwise, report that the batch cannot be completed.

## Input
First line: four integers $n$, $M$, $T$, $m$.
Each of the next $m$ lines: two integers $a$ and $b$ — variety $a$ must be cultivated in a strictly earlier phase than variety $b$. (Varieties are numbered 1 to $n$).

## Output
Print `YES` then $n$ integers (the phase of each variety, in $1 \dots T$); otherwise `NO`.

## Example

**Input:**
```
4 2 3 3
1 2
1 3
2 4
```

**Output:**
```
YES
1 2 2 3
```
