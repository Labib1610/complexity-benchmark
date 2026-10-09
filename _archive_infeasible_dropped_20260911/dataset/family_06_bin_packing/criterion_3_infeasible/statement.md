# Problem C — Oversized Item

Time limit: 1 s   Memory limit: 256 MB

## Description

A shipment has **n** indivisible items, item **i** weighing **w[i]**. Every container has the same capacity **C**, and each item must be placed whole into a single container.

In the input you are given, **at least one item is heavier than a single container's capacity**, so that item fits in no container and the shipment cannot be loaded.

Report the smallest index of an item whose weight exceeds **C**.

## Input

The first line contains two integers **n** and **C** (1 ≤ n ≤ 200000, 1 ≤ C ≤ 1 000 000 000).
The second line contains **n** integers **w[1] … w[n]** (1 ≤ w[i] ≤ 2 000 000 000), the item weights. It is guaranteed that at least one weight exceeds C.

## Output

Print a single integer: the smallest index **i** (1-based) such that **w[i] > C**.

## Examples

### Example 1

**Input**
```
4 10
3 12 5 8
```

**Output**
```
2
```

### Example 2

**Input**
```
3 100
50 60 250
```

**Output**
```
3
```

## Note

In Example 1, item 2 weighs 12, which exceeds the capacity 10, so it cannot be placed in any container.
