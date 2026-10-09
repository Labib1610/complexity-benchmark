# Problem A — Equilibrium Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description

You are researching a system of **n** chemical isomers (numbered 1 to n). Certain pairs of isomers can be transformed into each other via specific reversible reactions. Enabling a reaction requires synthesizing a unique enzyme, which has a distinct synthesis cost.

Among the **n** isomers, **t** are designated as **essential isomers**.

Initially, each isomer exists in isolation. Synthesizing the enzyme for the reaction between isomer *u* and isomer *v* allows them to freely interconvert, merging the equilibrium pool containing *u* and the equilibrium pool containing *v* into a single unified equilibrium pool. 

You must select a subset of enzymes to synthesize such that, once they are introduced and the pools merge, all **t** essential isomers end up in the exact same unified equilibrium pool. (Other, non-essential isomers may also end up in this pool).

Determine the minimum total synthesis cost of a set of enzymes that satisfies this requirement.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the essential isomers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a reversible reaction between isomers u and v that requires an enzyme costing w.
The available reactions are sufficient to allow all essential isomers to end up in the same equilibrium pool.

## Output

Print a single integer: the minimum total synthesis cost of the selected enzymes.

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

In Example 1, synthesizing the enzymes for the reactions between isomer 4 and isomers 1, 2, and 3 (total cost 1+1+1 = 3) merges their pools such that the three essential isomers end up in the same equilibrium pool. This is cheaper than synthesizing enzymes strictly for the reactions between the essential isomers themselves (which would cost 4). In Example 3 there is only one essential isomer, so it is already its own equilibrium pool and no enzymes are needed.