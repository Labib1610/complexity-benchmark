# Problem B — One-Way Route Planning

Time limit: 1 s   Memory limit: 256 MB

## Description

A delivery company operates across **n** locations numbered 1 to n, connected by **m** one-way roads. Every road leads strictly forward — once a vehicle leaves a location it can never return to it. (You may think of each location as belonging to a stage, and every road goes from a lower stage to a higher one.)

A valid delivery route is a sequence of all n locations such that:

- every location appears exactly once, and
- each pair of consecutive locations in the sequence is connected by a direct one-way road in the forward direction.

Determine whether a valid delivery route exists. If one exists, output it.

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
