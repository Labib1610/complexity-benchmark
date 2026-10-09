# Minimum Infrastructure Activation

Time limit: 5 s   Memory limit: 256 MB

## Description

A distributed system consists of **n** processing modules. Certain pairs of modules share a dormant bidirectional data channel. Activating a channel requires a specific amount of energy.

To make the system operational, a designated group of **t** critical modules must be fully integrated. Integration is achieved when every critical module can transmit data to every other critical module, either via a single active channel or a sequence of active channels. 

You may leverage any of the remaining auxiliary modules as routing junctions. Often, finding the most efficient paths between critical modules and merging them at auxiliary junctions will yield a lower energy expenditure than linking the critical modules exclusively to one another. 

Determine the minimum total energy required to activate a set of channels that achieves this integration.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2): the total number of modules, the number of dormant channels, and the number of critical modules.
The second line contains **t** distinct integers representing the identifiers of the critical modules.
Each of the subsequent **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a dormant channel between module **u** and module **v** that costs **w** energy to activate.
The available channels are always sufficient to integrate the critical modules.

## Output

Output a single integer: the minimum total energy cost to integrate all critical modules.

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

In Example 1, merging the paths at auxiliary module 4 requires activating three channels for a total energy of 3 (1+1+1). Linking the critical modules directly without the auxiliary junction would require at least 4 energy. In Example 3, with only a single critical module, no channels need to be activated.
