# Register Synchronization Network

Time limit: 2 s   Memory limit: 256 MB

## Description

A computing grid contains **N** data registers, labeled 1 through **N**.

There are **E** bidirectional synchronization channels available to be activated. Each channel links a specific pair of registers, **u** and **v**, and requires a one-time activation cost of **w**. 

The full set of available channels provides complete signal coverage: if all **E** channels were activated, a signal could successfully propagate between any two registers in the grid.

A specific subset of **F** registers are designated as *target* registers. You must choose a single subset of the available channels to permanently activate so that a signal can propagate between any two target registers using exclusively the activated channels. (Signals may route through non-target registers, provided the channels along the route are also activated).

Determine the minimum total activation cost required to connect all target registers in this manner. (If **F** = 1, exactly 0 channels need to be activated, so the minimum total cost is 0.)

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the labels of the target registers.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing an available channel between register **u** and register **v** with an activation cost of **w**.

## Output

Print a single integer: the minimum total activation cost required to ensure all target registers can signal each other.

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