# Problem B — Cargo Loading (Bulky Items)

Time limit: 2 s   Memory limit: 256 MB

## Description

A shipment has **n** indivisible items, item **i** weighing **w[i]**. You have containers, each with the same weight capacity **C**. Each item must be placed whole into exactly one container, and the total weight in any container may not exceed **C**.

In this shipment **every item weighs more than a third of a container's capacity** (that is, 3·w[i] > C for every item). Because of this, no container can hold more than two items.

Use as **few containers as possible** to load every item. Report the smallest number of containers and one valid loading that achieves it.

## Input

The first line contains two integers **n** and **C** (1 ≤ n ≤ 200000, 1 ≤ C ≤ 1 000 000 000).
The second line contains **n** integers **w[1] … w[n]** (C/3 < w[i] ≤ C), the item weights. Every item weighs more than C/3.

## Output

On the first line print the minimum number of containers needed.
On the second line print **n** integers where the i-th integer is the container number (from 1 to that minimum) holding item i. Any loading that uses the minimum number of containers and never exceeds capacity C is accepted.

## Examples

### Example 1

**Input**
```
5 10
6 4 5 5 7
```

**Output**
```
3
1 1 2 2 3
```

### Example 2

**Input**
```
3 10
8 8 8
```

**Output**
```
3
1 2 3
```

### Example 3

**Input**
```
2 10
4 6
```

**Output**
```
1
1 1
```

## Note

This is the same cargo-loading problem as Problem A. The only difference is that every item is bulky (heavier than a third of capacity), so at most two items share a container — which makes an efficient exact solution possible. In Example 1, pair {6,4} and {5,5}, leaving 7 alone: three containers.
