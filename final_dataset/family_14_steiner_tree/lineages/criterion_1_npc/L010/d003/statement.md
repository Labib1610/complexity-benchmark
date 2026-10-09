# Problem A — Fiber Optic Network Activation

Time limit: 5 s   Memory limit: 256 MB

## Description

A telecommunications provider is upgrading its regional fiber network. The region contains **n** distribution hubs, labeled from 1 to **n**. The provider has a list of potential direct fiber links that can be activated between certain pairs of hubs, each with an associated activation cost.

The government mandates that a specific group of **t** hubs, designated as critical facilities, must be fully interconnected. This means a signal must be able to travel between any two critical facilities using only the activated fiber links. The signal can pass through any number of intermediate hubs, so non-critical hubs can be freely utilized as relays to bridge the connections.

Your task is to determine the absolute minimum total activation cost required to fully interconnect all **t** critical facilities.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers identifying the critical facilities.
The next **m** lines each provide three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a direct fiber link can be activated between hub **u** and hub **v** for a cost of **w**.
It is guaranteed that it is possible to fully interconnect all critical facilities using the provided options.

## Output

Output a single integer representing the minimum total activation cost to ensure all critical facilities are interconnected.

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

In Example 1, using hub 4 as a relay (which costs 1+1+1 = 3) is more cost-effective than linking the three critical facilities directly (which would cost 4). In Example 3, there is only one critical facility, so no links need to be activated.