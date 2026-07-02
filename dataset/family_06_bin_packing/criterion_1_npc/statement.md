# Problem A — Cargo Loading

Time limit: 5 s   Memory limit: 256 MB

## Description

A shipment has **n** indivisible items, item **i** weighing **w[i]**. You have **k** containers, each with the same weight capacity **C**. Each item must be placed whole into exactly one container, and the total weight in any container may not exceed **C**.

Determine whether all items can be loaded into the **k** containers, and if so report a valid loading.

## Input

The first line contains three integers **n**, **k**, and **C** (1 ≤ n ≤ 18, 1 ≤ k ≤ 18, 1 ≤ C ≤ 1 000 000 000).
The second line contains **n** integers **w[1] … w[n]** (1 ≤ w[i] ≤ C), the item weights.

## Output

If all items can be loaded, print `YES` on the first line, then on the second line print **n** integers where the i-th integer is the container number (from 1 to k) holding item i. Any loading in which no container's total weight exceeds C is accepted.

If the items cannot be loaded into k containers, print `NO`.

## Examples

### Example 1

**Input**
```
4 2 10
6 5 4 5
```

**Output**
```
YES
1 2 1 2
```

### Example 2

**Input**
```
3 2 10
7 7 7
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1 5
5
```

**Output**
```
YES
1
```

## Note

In Example 1, containers hold {6, 4} = 10 and {5, 5} = 10, both within capacity. In Example 2, three weight-7 items cannot share two capacity-10 containers.
