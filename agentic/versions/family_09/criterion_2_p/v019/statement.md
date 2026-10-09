# Concurrent Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description

A distributed computing cluster consists of **n** processing modules and **m** bidirectional data pipelines. Each pipeline connects two different modules.

The network satisfies a strict architectural guarantee: choose any starting module $X$, and gather all other modules that can be reached from $X$ by following at least one sequence consisting of an even number of pipelines (the sequence is permitted to traverse the same pipelines and modules multiple times). It is guaranteed that within this gathered collection, no two modules are directly connected by a pipeline.

You need to select exactly **k** modules to run a concurrent diagnostic test. To prevent data corruption, a selection is only valid if no two selected modules are directly connected by a pipeline.

Determine whether a valid selection of exactly **k** modules exists, and if so, report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a pipeline between module **u** and module **v**. No pipeline is listed twice. The network is guaranteed to satisfy the even-sequence structural property described above.

## Output

If a valid selection of **k** modules exists, print `YES` on the first line, then on the second line print **k** distinct module numbers forming such a selection, separated by spaces. Any valid selection is accepted.

If no such selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```
