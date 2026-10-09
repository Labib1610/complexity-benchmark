# Tapestry Restoration

Time limit: 2 s   Memory limit: 256 MB

## Description

A historical tapestry is assembled from **N** fabric panels and **E** stitched borders. Each border joins exactly two panels. The borders unite all the panels into a single continuous tapestry.

A restoration team has identified **F** panels that feature critical historical motifs. To preserve the tapestry for display, a subset of the stitched borders must be reinforced with a special polymer thread. The chosen subset of borders must link all the critical panels together. Specifically, it must be possible to pass from any critical panel to any other critical panel by crossing exclusively reinforced borders. (Non-critical panels may be passed through if they are joined by these reinforced borders).

Each border requires a specific volume of polymer thread for reinforcement. Calculate the minimum total volume of thread needed to reinforce a valid subset of borders.

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the identifiers of the critical panels.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing a stitched border between panel **u** and panel **v** requiring **w** volume of thread.

## Output

Print a single integer: the minimum total volume of thread required such that all critical panels are linked exclusively via reinforced borders.

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