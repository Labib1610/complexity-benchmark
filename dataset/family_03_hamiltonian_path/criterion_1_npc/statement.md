# Problem A — Delivery Route Planning

Time limit: 5 s   Memory limit: 256 MB

## Description

A courier must plan a single sweep across **n** depots joined by **m** two-way service roads. The sweep is a sequence of depots in which **every depot is visited exactly once** and each consecutive pair in the sequence is joined by a direct road — the vehicle never revisits a depot and never jumps between unconnected ones. Fuel, distances, and road quality are outside this plan; only which depots share a direct road matters. Some road maps admit such a one-pass sweep and many do not, and having many roads is no guarantee — a single unavoidable dead-end can make a full single-visit sweep impossible. Decide whether a sweep visiting all depots exactly once exists, and if so report one ordering; otherwise report that no single-pass sweep covers every depot.

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
