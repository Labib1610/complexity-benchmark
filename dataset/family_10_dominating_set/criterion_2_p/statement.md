# Problem B — Hierarchy Monitoring

Time limit: 1 s   Memory limit: 256 MB

## Description

A facility has **n** locations (numbered 1..n) connected by direct links. Location **1** is the top of the facility. Every other location names exactly one **parent** location it links to, and following parents from any location always leads up to location 1. There are no closed loops of links.

If you install a sensor at a location, that sensor **monitors** its own location and every location directly linked to it (its parent and all of its children). A location is **covered** if it has a sensor or is directly linked to one.

Find the minimum number of sensors needed so that every location is covered.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 200000).
Each of the next **n−1** lines contains two integers **c** and **p** (1 ≤ c, p ≤ n, c ≠ p): a direct link where **p** is the parent of **c**. Every location except location 1 appears exactly once as a **c**.

## Output

Print a single integer: the minimum number of sensors needed to cover every location.

## Examples

### Example 1

**Input**
```
3
2 1
3 2
```

**Output**
```
1
```

### Example 2

**Input**
```
4
2 1
3 1
4 1
```

**Output**
```
1
```

### Example 3

**Input**
```
7
2 1
3 1
4 2
5 2
6 3
7 3
```

**Output**
```
2
```

## Note

In Example 1 the three locations form a chain 1–2–3; a single sensor at location 2 monitors all of them. In Example 3, sensors at locations 2 and 3 cover the whole facility.
