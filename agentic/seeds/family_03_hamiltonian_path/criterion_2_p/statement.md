# Problem B — One-Way Route Planning

Time limit: 1 s   Memory limit: 256 MB

## Description

A courier plans a sweep across **n** depots joined by **m** one-way service roads. Every road runs strictly forward: picture the depots arranged in stages, each road leading from an earlier stage to a later one, so once the vehicle leaves a depot it can never return. The sweep must be an ordering of all n depots visiting each exactly once, with every consecutive pair joined by a forward road. Because the roads never loop back, reachability is acyclic and feasibility can be settled without trying all orders. Decide whether a single-pass forward sweep visiting all depots exists, and if so report one ordering; otherwise report that none exists.

## Input

The first line contains two integers **n** and **m** (1 ≤ n ≤ 200 000, 0 ≤ m ≤ 200 000).  
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n) describing a one-way road from u to v.  
The road network is guaranteed to have no directed cycles.

## Output

If a valid delivery route exists, print `YES` on the first line, then on the second line print the n location numbers separated by spaces.  
If no valid route exists, print `NO`.

The output is uniquely determined when a route exists.

## Examples

### Example 1

**Input**
```
4 3
1 2
2 3
3 4
```

**Output**
```
YES
1 2 3 4
```

### Example 2

**Input**
```
3 2
1 3
2 3
```

**Output**
```
NO
```
