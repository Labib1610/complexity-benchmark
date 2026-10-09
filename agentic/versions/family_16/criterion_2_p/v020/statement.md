# Orbital Ore Processing

Time limit: 1 s   Memory limit: 256 MB

## Description

An orbital station processes **j** batches of raw asteroids. Each batch must pass through two stages in sequence: first the **Crusher**, and then the **Smelter**. For each batch, you know the exact time it takes to be crushed, and the exact time it takes to be smelted.

The facility operates under the following constraints:

- The Crusher can process only one batch at a time.
- The Smelter can process only one batch at a time.
- A batch can begin smelting only after it has been completely crushed.
- If the Smelter is busy, a crushed batch waits in a holding zone. This allows the Crusher to immediately begin working on the next batch without delay.
- Due to the automated conveyor system, the batches must enter the Smelter in the exact same sequence that they were fed into the Crusher.
- You have full control over the initial sequence in which the batches are fed into the Crusher.

Your goal is to determine the optimal sequence of batches to minimize the total time until the **last** batch finishes smelting. Report this minimum completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **c** and **s** (1 ≤ c, s ≤ 1000000): the processing times of a batch in the Crusher and the Smelter, respectively.

## Output

Print a single integer: the smallest possible time at which all batches are completely smelted.

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

In Example 2, the single batch takes 5 units of time in the Crusher and then 3 units in the Smelter, finishing at time 8.
