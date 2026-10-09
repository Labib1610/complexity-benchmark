# Essential Site Path Aggregation

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a network of **n** distinct sites, numbered $1$ to **n**. You are given a target set of **t** sites, called the *essential sites*. 

You are provided with a catalog of **m** available undirected cables. Each cable connects a pair of sites (**u**, **v**) and has an associated maintenance cost of **w**. It is guaranteed that the full catalog of **m** available cables forms a fully connected network on the **n** sites with exactly **n** - 1 cables. This structure guarantees that there is exactly one unique simple path (sequence of cables) between any pair of sites in the network.

Your goal is to select a subset of these **m** available cables to retain. The retention is governed by a system of exactly $\frac{t(t-1)}{2}$ strict dependency constraints, one for every possible pair of distinct essential sites. 

For each pair of essential sites $(A, B)$, consider their *critical separation set*: the set of all cables in the full network that possess the property that if that single cable were removed from the full network, $A$ and $B$ would no longer be connected to each other. The constraint dictates that every cable in the critical separation set for $(A, B)$ must be present in your retained subset.

You must find the minimum possible total cost (the sum of the costs of the retained cables) such that all $\frac{t(t-1)}{2}$ constraints are simultaneously satisfied.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **n** ≤ 200000, **m** = **n** - 1, 1 ≤ **t** ≤ **n**).

The second line provides **t** distinct integers representing the essential sites.

The subsequent **m** lines each contain three integers **u**, **v**, and **w**. These values describe an available undirected cable between site **u** and site **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**) with a maintenance cost of **w** (1 ≤ **w** ≤ 1000000). It is guaranteed that if all **m** available cables are used, all **n** sites are connected to each other, with exactly one unique simple path between any pair of sites.

## Output

Print a single integer indicating the minimum possible total cost of a chosen subset of cables such that all $\frac{t(t-1)}{2}$ critical separation set constraints are satisfied.

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

In Example 1, the essential sites are 1 and 4. There is $\frac{2(1)}{2} = 1$ constraint, for the pair (1, 4). The critical separation set for (1, 4) consists of the cables (1, 2), (2, 3), and (3, 4), because removing any one of these from the full network leaves site 1 and site 4 disconnected. Therefore, all three of these cables must be retained. Their total cost is 5 + 1 + 2 = 8.

In Example 2, there is only one essential site. Since there are no pairs of distinct essential sites, there are 0 constraints to satisfy, and no cables need to be retained. The minimum cost is 0.