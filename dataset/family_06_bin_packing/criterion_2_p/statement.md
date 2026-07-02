# Problem B — Bulk Cargo Loading

Time limit: 1 s   Memory limit: 256 MB

## Description

A shipment consists of **n** batches of a bulk material, batch **i** weighing **w[i]**. The material is loose, so any batch may be split freely across containers in any amounts (an item may be partially loaded into one container and the rest into others). Every container has the same capacity **C**.

Determine the smallest number of containers needed to hold all of the material.

## Input

The first line contains two integers **n** and **C** (1 ≤ n ≤ 200000, 1 ≤ C ≤ 1 000 000 000).
The second line contains **n** integers **w[1] … w[n]** (1 ≤ w[i] ≤ 1 000 000 000), the batch weights.

## Output

Print a single integer: the smallest number of containers needed.

## Examples

### Example 1

**Input**
```
3 10
6 5 4
```

**Output**
```
2
```

### Example 2

**Input**
```
3 10
10 10 10
```

**Output**
```
3
```

### Example 3

**Input**
```
4 7
1 1 1 1
```

**Output**
```
1
```

## Note

In Example 1, the total weight is 15; since material can be split, two containers (capacity 10 each) suffice.
