# Problem A — Core Network Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description

The architectural committee has approved a campus layout featuring **n** landmarks. Given the ample redundancy in the underground topography, there are **m** potential direct conduit links available between various pairs of landmarks, each with a fixed excavation and material cost.

To implement the new synchronization protocol, a small, highly restricted subset of exactly **t** landmarks has been designated as "core nodes". These core nodes must all be able to communicate with one another. Because **t** is strictly bounded and typically much smaller than **n**, the vast majority of the landmarks are non-core and function merely as optional relays. 

By leveraging the small size of the core group, you can efficiently construct an optimal spanning configuration. Your task is to synthesize a unified network that spans all **t** core nodes. You may route connections through any of the non-core landmarks if it reduces the total cost. Since the available conduits are guaranteed to be sufficient, you simply need to select the cheapest subset of links that ensures every core node can reach every other core node. Determine this minimum total cost.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers representing the core nodes (indexed 1 to **n**).
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), describing a potential conduit between landmark **u** and landmark **v** with a cost of **w**.
It is guaranteed that a valid network can always be formed.

## Output

Print a single integer: the minimum total cost to synthesize the network spanning all core nodes.

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

In Example 1, routing the data through landmark 4 (which is not a core node) incurs a cost of 1+1+1 = 3. This is cheaper than establishing conduits directly between the three core nodes, which would cost at least 4. In Example 3, there is only one core node, so no conduits need to be activated.
