# Problem B — Two-Stage Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

A high-capacity manufacturing facility must process a batch of **j** distinct items. The configuration space for this batch is vast: there are **j!** possible permutations in which the items can be ordered. You must evaluate this space to find a sequence that minimizes the total elapsed time until the entire batch is completed.

The facility's architecture consists of exactly two sequential stages: a primary processor and a secondary processor. Every item must first undergo primary processing and subsequently undergo secondary processing. The system enforces the following strict operational rules:

- A processor can only handle a single item at a time.
- An item's secondary processing cannot commence until its primary processing has successfully concluded.
- You must establish a single, global sequence for the batch. Both the primary and the secondary processors will process the items in this exact same chosen order.

Because the processors can operate simultaneously on different items, the total time depends heavily on how the primary and secondary stages overlap. Determine the absolute minimum time required for the secondary processor to finish the final item in the batch, assuming the optimal sequence is chosen.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the duration of the item on the primary processor and the secondary processor, respectively.

## Output

Print a single integer: the minimum possible time at which the secondary processor finishes the final item.

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

In Example 2, the single item occupies the primary processor for 5 time units, and then the secondary processor for 3 time units. It finishes at time 8.
