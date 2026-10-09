# Problem A — Activating the Fiber Grid

Time limit: 5 s   Memory limit: 256 MB

## Description

A communications network consists of **n** facilities and **m** dormant fiber links. Each link connects two facilities and requires a specific activation fee to be turned on.

Within this network, a specific subset of **t** facilities are classified as **critical**. The other facilities act as optional repeaters; you may route data through them if it reduces your overall costs, but they do not inherently need to be connected.

You must choose a set of dormant fiber links to activate such that all critical facilities can communicate with one another, either via direct links or by hopping through intermediate facilities. Determine the minimum total activation fee necessary to achieve this.

Please note the following guarantees about the network parameters:
* The total number of dormant fiber links **m** will never exceed 4950.
* The minimum total activation fee required to connect the critical facilities will always be strictly less than $10^8$.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers: the identifiers of the critical facilities.
Each of the subsequent **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a dormant fiber link between facilities **u** and **v** with an activation fee of **w**.
It is guaranteed that it is possible to connect all critical facilities using the available links.

## Output

Output a single integer representing the minimum total activation fee required to link all critical facilities.

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

In Example 1, routing the connection through the optional repeater facility 4 incurs an activation fee of 1+1+1 = 3, which is more cost-effective than linking the three critical facilities directly (which would incur a fee of 4). In Example 3, there is only one critical facility, meaning no links need to be activated.
