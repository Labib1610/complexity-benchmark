# Problem C — Identifying the Unreachable Location

Time limit: 1 s   Memory limit: 256 MB

## Description

A delivery company operates across **n** locations numbered 1 to n, connected by **m** bidirectional roads. It is known that at least one location has **no roads connected to it** — it is completely cut off from the rest of the network.

Because a valid delivery route must visit every location, and a cut-off location has no roads to enter or leave, planning such a route is impossible. Your task is to identify which location is cut off.

Output the **smallest** location number that has no roads connected to it.

## Input

The first line contains two integers **n** and **m** (2 ≤ n ≤ 200 000, 0 ≤ m ≤ n·(n−1)/2).  
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v) describing a bidirectional road between location u and location v.  
It is guaranteed that at least one location has no roads connected to it.

## Output

Print a single integer: the smallest location number with no roads connected to it.

## Examples

### Example 1

**Input**
```
4 2
2 3
3 4
```

**Output**
```
1
```

### Example 2

**Input**
```
5 3
1 2
2 3
1 3
```

**Output**
```
4
```
