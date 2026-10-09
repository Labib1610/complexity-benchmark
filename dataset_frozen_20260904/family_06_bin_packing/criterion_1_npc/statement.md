# Problem A — Cargo Loading

Time limit: 5 s   Memory limit: 256 MB

## Description

A shipment has **n** indivisible items, item **i** weighing **w[i]**. You have containers, each with the same weight capacity **C**. Each item must be placed whole into exactly one container, and the total weight in any container may not exceed **C**.

Use as **few containers as possible** to load every item. Report the smallest number of containers and one valid loading that achieves it.

## Input

The first line contains two integers **n** and **C** (1 ≤ n ≤ 28, 1 ≤ C ≤ 1 000 000 000).
The second line contains **n** integers **w[1] … w[n]** (1 ≤ w[i] ≤ C), the item weights.

## Output

On the first line print the minimum number of containers needed.
On the second line print **n** integers where the i-th integer is the container number (from 1 to that minimum) holding item i. Any loading that uses the minimum number of containers and never exceeds capacity C is accepted.

## Examples

### Example 1

**Input**
```
4 10
6 5 4 5
```

**Output**
```
2
1 2 1 2
```

### Example 2

**Input**
```
3 10
7 7 7
```

**Output**
```
3
1 2 3
```

### Example 3

**Input**
```
1 5
5
```

**Output**
```
1
1
```

## Note

In Example 1, two containers suffice: {6, 4} = 10 and {5, 5} = 10. In Example 2, three weight-7 items cannot share a capacity-10 container, so three containers are needed.
