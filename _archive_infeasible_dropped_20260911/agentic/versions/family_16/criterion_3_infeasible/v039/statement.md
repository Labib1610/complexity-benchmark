# Problem C — Impossible Target: Provide Evidence

Time limit: 2 s   Memory limit: 256 MB

## Description

A space agency is preparing a set of Joint Orbital Blocks. Each block must undergo a preparation phase in the Alpha Bay and then a verification phase in the Beta Bay. A block can only enter the Beta Bay after its preparation in the Alpha Bay is fully complete. Furthermore, each bay can only accommodate a single block at a time.

You are given a target duration. All blocks must completely finish both phases within this target duration.

For every dataset provided, it is a guaranteed fact that the target duration cannot possibly be met, regardless of the sequence in which the blocks are processed. Your objective is not to search for a sequence, but to output a short piece of evidence proving that the target is unachievable.

Exactly one of the following reasons always applies. Output the one that holds:

- **A single block requires too much time.** Since a block must go through the Alpha Bay and then the Beta Bay sequentially, if the sum of these two durations for a single block is strictly greater than the target duration, that block alone makes the target unachievable.
  Output: `JOB i` — where **i** (1-based) is such a block.

- **A bay has too much total work.** Since a bay processes blocks one at a time, it must be active for at least the sum of the durations of all blocks assigned to it. If the total work in the Alpha Bay (or the Beta Bay) exceeds the target duration, the target is impossible.
  Output: `LOAD c` — where **c** is 1 (for the Alpha Bay) or 2 (for the Beta Bay) and the total duration for that bay exceeds the target.

## Input

The first line contains two integers: the total count of Joint Orbital Blocks (at least 1, up to the fleet capacity of 200000) and the target duration (at least 1, up to the planetary alignment window of 1000000000).
Each of the subsequent lines describes one block in order from 1 to the total count. Each line contains two integers: the duration required in the Alpha Bay and the duration required in the Beta Bay. Every duration is at least 1 and bounded by the component degradation limit of 1000000.

## Output

Output a single line containing either `JOB i` (if block **i** cannot be completed in time) or `LOAD c` (if bay **c** has a total duration exceeding the target).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, block 1 requires 70 + 60 = 130 > 100 time units in sequence, making `JOB 1` valid evidence that the target is unachievable. In Example 2, no single block exceeds 150, but the Alpha Bay must be active for 50+50+50+50 = 200 > 150 units of time in total, so `LOAD 1` is the correct evidence.
