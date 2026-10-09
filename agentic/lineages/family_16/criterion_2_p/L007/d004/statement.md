# Archival Exhibition

Time limit: 1 s   Memory limit: 256 MB

## Description

An archive has recently acquired **j** ancient manuscripts. You must arrange them in a single sequence from left to right for a new exhibition.

Each manuscript features two components: a physical display requiring **p1** minutes to inspect, and a digital scan requiring **p2** minutes to read.

A reviewer will evaluate the exhibition starting at the physical display of the first manuscript and finishing at the digital scan of the last manuscript. The reviewer follows these rules:
- They move strictly from left to right.
- They transition from the physical displays to the digital scans exactly once, at a manuscript **k** of their choosing. They cannot transition back to the physical displays.
- Consequently, if the reviewer transitions at the **k**-th manuscript in your arranged sequence (where 1 ≤ k ≤ j), their total inspection time is the sum of the physical display times for the 1st through **k**-th manuscripts, plus the sum of the digital scan times for the **k**-th through **j**-th manuscripts.

The reviewer is highly critical and will deliberately choose the transition point **k** that MAXIMIZES their total inspection time.

Determine the initial left-to-right arrangement of the **j** manuscripts that MINIMIZES this maximum possible inspection time. Report this minimum time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the physical display time and the digital scan time for that manuscript, respectively.

## Output

Print a single integer: the smallest possible maximum inspection time the reviewer can achieve.

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

In Example 2, the single manuscript takes 5 minutes to physically inspect and then 3 minutes to digitally scan. The reviewer must transition at manuscript 1, resulting in a total time of 8.