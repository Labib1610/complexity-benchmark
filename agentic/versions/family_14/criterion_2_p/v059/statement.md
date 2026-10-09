# Intercellular Nutrient Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description

A fungal entity comprises **n** cellular nodes. These nodes are joined by **m** microscopic conduits. The architecture of the entity is such that it forms a single unified network, yet contains no redundant conduits that would create a closed loop.

Within this entity, **t** specific nodes harbor vital reproductive material. For the organism to reproduce successfully, all nodes with reproductive material must be able to share resources with each other. Resources can flow freely between nodes as long as the conduits connecting them are actively maintained. Keeping the conduit between node **u** and node **v** open requires a continuous energy expenditure of **w**.

Determine the lowest possible total energy expenditure required to maintain a selection of conduits such that resources can flow between any pair of reproductive nodes (this flow may route through other intermediate nodes).

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** is exactly one less than **n**).
The second line contains **t** distinct integers: the identifiers of the nodes harboring reproductive material.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000): denoting a conduit between node **u** and node **v** with an energy expenditure of **w**. The conduits follow the structural rules described above.

## Output

Print a single integer: the lowest total energy expenditure needed to link all reproductive nodes.

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

In Example 1, the reproductive nodes 1 and 4 can only share resources by routing through nodes 2 and 3. Therefore, all three conduits (expenditures 5, 1, and 2) must be maintained, yielding a total of 8.
In Example 2, there is only one reproductive node, meaning no conduits need to be maintained.
