# Secure Communications Network

Time limit: 2 s   Memory limit: 256 MB

## Description

A secure communications network consists of **N** outposts and **E** bidirectional transmission links. Each link directly connects exactly two outposts. The links are arranged such that the entire network is fully integrated, meaning messages can route between any two outposts, and the total number of transmission links is exactly one less than the total number of outposts.

A security audit has flagged **F** specific outposts that handle highly classified intelligence. To ensure the integrity of their communications, a subset of the transmission links must be upgraded with quantum encryption hardware. The chosen subset of upgraded links must form a secure infrastructure that connects all the classified outposts together. Specifically, it must be possible to route data from any classified outpost to any other classified outpost by traversing exclusively across upgraded links. (Unclassified outposts may serve as intermediate routing points if they are connected by these upgraded links).

Each link requires a certain financial allocation to be upgraded. Determine the minimum total financial allocation required to upgrade a valid subset of links.

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the identifiers of the classified outposts.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing a transmission link between outpost **u** and outpost **v** requiring a financial allocation of **w** to upgrade.

## Output

Print a single integer: the minimum total financial allocation required such that all classified outposts can communicate exclusively via upgraded links.

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