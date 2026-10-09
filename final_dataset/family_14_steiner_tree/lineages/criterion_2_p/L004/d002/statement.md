# Synchronization Energy

Time limit: 2 s
Memory limit: 256 MB

## Description

In an industrial plant, a fluid distribution system connects **n** processing units (numbered 1 to **n**) using **m** bidirectional transfer pipes. The system is designed such that fluid can flow between any two units. To prevent pressure loops, the network is built without any redundant connections, ensuring no fluid can circulate in a closed circuit. 

A sensor array has flagged exactly **t** specific units that require synchronization. To synchronize them, you must activate a subset of the pipes to form a single continuous fluid network containing all **t** flagged units. The active network must allow fluid to flow between any two flagged units. Unflagged units may be part of this active network if they are needed to bridge the connections.

Activating a pipe consumes a specific amount of mechanical energy. Your task is to select a subset of pipes that connects all **t** flagged units while minimizing the total mechanical energy consumed.

## Input

The first line contains three integers **n**, **m**, and **t**. The plant's capacity limits the number of units **n** (1 ≤ **n** ≤ 200000). The piping design ensures **m** = **n** − 1. The number of flagged units **t** is restricted by the available units (1 ≤ **t** ≤ **n**).
The second line contains **t** distinct integers: the identifiers of the flagged units.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. These denote a bidirectional transfer pipe between distinct units **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**). The mechanical energy **w** required to open this pipe is bounded by the generator limits (1 ≤ **w** ≤ 1000000).

## Output

Print a single integer: the minimum total energy required to form a continuous network connecting all flagged units.

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