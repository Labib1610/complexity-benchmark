# Problem A — Linking the Critical Hubs

Time limit: 5 s   Memory limit: 256 MB

## Description

A regional development project involves **n** zones (numbered 1..n). Among these, **t** specific zones are designated as critical hubs. 

You are tasked with establishing a communication network. You are given a list of possible segments, each joining two different zones at a specific cost. 

You must select a subset of these segments such that all critical hubs can communicate with each other. Two hubs can communicate if there is a sequence of selected segments connecting them, which may pass through any number of intermediate zones. The non-critical zones are entirely optional; you may route communication through them if it reduces the total cost, or ignore them completely.

Find the minimum total cost of a set of segments that ensures all critical hubs are connected.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the critical hubs.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a segment joining zone u and zone v at cost w.
The provided segments are sufficient to connect all critical hubs.

## Output

Print a single integer: the minimum total cost to connect all critical hubs.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, routing the connection through the optional zone 4 (costs 1+1+1 = 3) is cheaper than joining the three critical hubs directly (which would cost 4). In Example 3 there is only one critical hub, so no segments are needed.