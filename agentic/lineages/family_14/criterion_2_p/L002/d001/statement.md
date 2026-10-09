# Orbital Station Power Grid

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital station consists of **n** modules (numbered 1 to **n**). These modules are interconnected by structural corridors. The architecture of the station guarantees that the entire facility is fully contiguous, utilizing the absolute minimum number of corridors necessary to achieve this integration.

During a low-power emergency, the station commander must power down non-essential areas. However, **t** specific modules contain vital life-support systems. The commander must keep a subset of corridors fully pressurized so that all **t** vital modules remain interlinked. This means every vital module must be able to reach every other vital module (either directly or through intermediate modules) exclusively by traversing pressurized corridors.

Each corridor requires a certain amount of power to remain pressurized, and unpressurized corridors cannot be traversed. Determine the minimum total power required to maintain pressurization in a set of corridors that successfully connects all **t** vital modules.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line contains **t** distinct integers: the identifiers of the vital modules.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a corridor linking module **u** and module **v** that requires **w** units of power to pressurize.

## Output

Print a single integer: the minimum total power required to keep all vital modules connected.

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