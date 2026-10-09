# Problem A — Interference-Free Collection

Time limit: 5 s   Memory limit: 256 MB

## Description

A monitoring system has **n** sensors (numbered 1..n) and **m** interference links. Each link joins two sensors whose signals interfere with each other.

A collection of sensors is **interference-free** if no two sensors in the collection share an interference link.

Given a target size **k**, decide whether an interference-free collection of exactly **k** sensors exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): an interference link. No link is listed twice.

## Output

If an interference-free collection of **k** sensors exists, print `YES` on the first line, then on the second line print **k** distinct sensor numbers forming such a collection, separated by spaces. Any collection in which no two sensors have a link is accepted.

If no such collection exists, print `NO`.

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

In Example 2, sensors 1, 3 and 5 have no interference links among them. In Example 1 no three of the four sensors are mutually free of links.
