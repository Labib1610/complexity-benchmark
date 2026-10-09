# Problem A — Interstellar Comms Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

A space station has **n** communication modules (numbered 1 to **n**). A specific subset of **t** modules are designated as *critical*. Your task is to establish a network so that every critical module can route data to every other critical module, either directly or through a sequence of intermediate modules.

You are provided with a list of **m** potential bidirectional data links that can be activated. Activating a link between two modules requires a certain continuous power draw. You may route data through any of the non-critical modules if it results in a more power-efficient overall network, or you may ignore them entirely.

To assist with your configuration planning, note these two system guarantees:
- The total number of potential data links **m** will never exceed 4950.
- The number of critical modules **t** will never exceed **m** + 1.

Find the minimum total power draw required to activate a set of links such that all critical modules are connected in a single communicating network.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the IDs of the critical modules.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a potential data link between module **u** and module **v** with a power draw of **w**.
It is guaranteed that the provided links are sufficient to interconnect all critical modules.

## Output

Print a single integer: the minimum total power draw required to interconnect all critical modules.

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

In Example 1, routing the connections through the non-critical module 4 (power draw 1+1+1 = 3) is more efficient than connecting the three critical modules directly (which would draw 4). In Example 3, since there is only one critical module, no links need to be activated.
