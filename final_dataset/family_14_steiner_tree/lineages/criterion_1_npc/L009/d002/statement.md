# Problem A — Linking the Priority Facilities

Time limit: 5 s   Memory limit: 256 MB

## Description

A regional development project encompasses **n** distinct districts (numbered 1 to **n**). Due to strict regulatory caps on special infrastructure, a maximum of 10 districts can be granted priority facility status. There are exactly **t** such priority facilities in the current plan.

Your objective is to establish a unified data grid. You are provided with a catalogue of potential optical links, each capable of joining two different districts at a given cost.

You must choose a collection of these optical links so that every priority facility can exchange data with all other priority facilities. Data exchange between any two priority facilities is possible if they are joined by a sequence of chosen optical links. This sequence can traverse any number of intermediate districts. The districts without priority status are strictly optional; you may route the grid through them if it achieves a lower total cost, or you may bypass them entirely.

Determine the minimum total cost of a collection of optical links that successfully interconnects all priority facilities.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2). The integer **t** represents the number of priority facilities, which is at least 1 and, as dictated by the regulatory cap, at most 10.
The second line contains **t** distinct integers: the ids of the priority facilities.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an optical link joining district **u** and district **v** at cost **w**.
The provided optical links are sufficient to interconnect all priority facilities.

## Output

Print a single integer: the minimum total cost to interconnect all priority facilities.

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

In Example 1, routing the grid through the optional district 4 (costs 1+1+1 = 3) is cheaper than joining the three priority facilities directly (which would cost 4). In Example 3 there is only one priority facility, so no optical links are needed.