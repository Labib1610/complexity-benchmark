# Problem A — Delivery Route Planning

Time limit: 5 s   Memory limit: 256 MB

## Description

A delivery company operates across **n** locations numbered 1 to n, connected by **m** bidirectional roads. A valid delivery route is a sequence of locations such that:

- every location appears exactly once, and
- each pair of consecutive locations in the sequence is connected by a direct road.

Determine whether a valid delivery route exists. If one exists, output any valid route.

## Input

The first line contains two integers **n** and **m** (1 ≤ n ≤ 20, 0 ≤ m ≤ n·(n−1)/2).  
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v) describing a bidirectional road between location u and location v.  
No road appears more than once. No self-loops.

## Output

If a valid delivery route exists, print `YES` on the first line, then on the second line print the n location numbers separated by spaces, forming a valid route (any valid route is accepted).  
If no valid route exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4
1 2
2 3
3 4
1 3
```

**Output**
```
YES
1 2 3 4
```

### Example 2

**Input**
```
4 2
1 2
3 4
```

**Output**
```
NO
```

### Example 3

**Input**
```
2 1
1 2
```

**Output**
```
YES
1 2
```
