# Essential Site Path Aggregation

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a network of **n** distinct sites, numbered $1$ to **n**. You are given a target set of **t** sites, called the *essential sites*. 

You are provided with a catalog of **m** available undirected cables. Each cable connects a pair of sites (**u**, **v**) and has an associated maintenance cost of **w**. It is guaranteed that the full catalog of **m** available cables forms a fully connected network on the **n** sites with exactly **n** - 1 cables. This structure guarantees that there is exactly one unique simple path (sequence of cables) between any pair of sites in the network.

Your goal is to select a subset of these **m** available cables to retain. The rule for retention is: for every possible pair of essential sites, you must retain all cables that make up the unique simple path between them in the full network. 

You must find the minimum possible total cost (the sum of the costs of the retained cables) that satisfies this rule.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **n** ≤ 200000, **m** = **n** - 1, 1 ≤ **t** ≤ **n**).

The second line provides **t** distinct integers representing the essential sites.

The subsequent **m** lines each contain three integers **u**, **v**, and **w**. These values describe an available undirected cable between site **u** and site **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**) with a cost of **w** (1 ≤ **w** ≤ 1000000). It is guaranteed that if all **m** available cables are used, all **n** sites are connected to each other, with exactly one unique simple path between any pair of sites.

## Output

Print a single integer indicating the minimum total cost of a chosen subset of cables such that, for every pair of essential sites, all cables on the unique simple path between them are retained.

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

In Example 1, the essential sites are 1 and 4. The unique simple path between site 1 and site 4 in the full network consists of the cables (1, 2), (2, 3), and (3, 4). Therefore, all three of these cables must be retained. Their total cost is 5 + 1 + 2 = 8.

In Example 2, there is only one essential site. Since there are no pairs of distinct essential sites, no paths need to be retained. The minimum cost is 0.