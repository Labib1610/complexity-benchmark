# Problem B — Activating the Primary Network

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a routing protocol for a network of **n** locations (numbered 1 to n) and **m** potential point-to-point connections. Each connection has a known activation cost. The network topology guarantees that a message broadcast from any location will reach every other location without ever encountering a closed loop. 

A specific group of **t** locations are designated as **primary**. Your objective is to select a subset of the potential connections to activate so that every primary location can communicate with every other primary location. Messages can be routed through any activated intermediate non-primary locations. 

You must determine the absolute minimum total activation cost required to ensure all primary locations are mutually reachable.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the primary locations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000) representing a potential connection between location u and location v with an activation cost of w.

## Output

Print a single integer: the minimum total activation cost to fully connect all primary locations.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the primary locations 1 and 4 can only communicate if the connections between (1,2), (2,3), and (3,4) are all activated. The total cost is 5 + 1 + 2 = 8.
In Example 2, there is only one primary location, so no connections need to be activated. The minimum total cost is 0.
In Example 3, primary locations 1, 2, and 3 must all be connected. Activating the connection (1,2) with cost 4 and the connection (2,3) with cost 5 achieves this for a total cost of 9.