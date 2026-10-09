# Intercellular Nutrient Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description

A fungal organism consists of **n** cellular junctions. These junctions are linked by **m** microscopic tubes. The biological structure is such that between any two junctions, there exists exactly one non-repeating sequence of tubes.

Among all junctions, **t** of them contain reproductive spores. In order for the organism to reproduce successfully, all spore-containing junctions must be able to exchange nutrients with one another. Nutrients can flow freely through any tube that has been metabolically activated. Activating the tube between junction **u** and junction **v** requires a specific metabolic cost **w**.

Determine the minimum total metabolic cost required to activate a subset of tubes such that every spore-containing junction can exchange nutrients with every other spore-containing junction (possibly passing through other intermediate junctions).

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the junctions containing reproductive spores.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): representing a tube linking junction u and junction v with an activation cost of w. The tubes form the structure described above.

## Output

Print a single integer: the minimum total metabolic cost to link all spore-containing junctions.

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

In Example 1, the spore-containing junctions 1 and 4 can only exchange nutrients via junctions 2 and 3, so all three tubes (costs 5, 1, and 2) must be activated, totaling 8.
In Example 2, there is only one spore-containing junction, so no tubes need to be activated.
