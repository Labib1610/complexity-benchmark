# Problem A — Stable Substance Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

A chemical storage facility is preparing a new isolation chamber. The facility has **n** substances (numbered 1..n) and **m** known reactive pairs. Each pair joins two substances that react violently and cannot be stored together.

A selection of substances is **stable** if no two substances in the selection react violently (there is no reactive pair between any two of them).

The chamber requires exactly **k** substances to be tested together. Given a target capacity **k**, decide whether a stable selection of exactly **k** substances exists to fill the chamber, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a reactive pair. No pair is listed twice.

## Output

If a stable selection of **k** substances exists, print `YES` on the first line, then on the second line print **k** distinct substance numbers forming such a selection, separated by spaces. Any selection in which no two substances react violently is accepted.

If no such selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

A stable selection means no two chosen substances may react. In Example 2, substances 1, 3 and 5 have no reactive pairs among them. In Example 1 no three of the four substances are mutually non-reactive.
