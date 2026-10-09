# Problem A — Interconnecting the Primary Hubs

Time limit: 5 s   Memory limit: 256 MB

## Description

A quantum communication network is being established across a facility containing **n** research outposts (numbered 1 to **n**). Certain pairs of outposts can be physically linked by activating a dedicated fiber connection at a specific expense. 

Among these outposts, **t** are designated as **primary hubs**. To function correctly, all primary hubs must be mutually interconnected—meaning a signal must be able to travel between any two primary hubs, either directly or by passing through one or more intermediate outposts. The outposts that are not primary hubs are considered **auxiliary nodes**. You are free to route connections through auxiliary nodes if doing so reduces the overall expense, or you may bypass them entirely.

To ensure network stability and avoid excessive signal degradation, the facility's design guarantees three properties:
- The total number of available fiber connections will not exceed 4950.
- The number of auxiliary nodes will never exceed 99.
- The sum of activation expenses for any simple cycle of fiber connections in the provided network will not exceed $10^8$.

You must select a configuration of fiber connections to activate such that all primary hubs are interconnected. Determine the minimum total activation expense required to achieve this.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line provides **t** distinct integers representing the identifiers of the primary hubs.
Each of the subsequent **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000). This indicates that a fiber connection can be activated between outpost **u** and outpost **v** for an expense of **w**.
It is guaranteed that the available fiber connections are sufficient to interconnect all primary hubs.

## Output

Print a single integer representing the minimum total activation expense required to interconnect all primary hubs.

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

In Example 1, routing the connections through the auxiliary node 4 incurs an expense of 1 + 1 + 1 = 3, which is more cost-effective than linking the three primary hubs directly (which would incur an expense of 4). In Example 3, there is only a single primary hub, so no fiber connections need to be activated.
