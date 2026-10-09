# Emergency Pressurization

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital station is composed of **n** modules, identified by integers from 1 to **n**. These modules are physically linked by a network of structural corridors. The architecture of the station guarantees that the entire facility is fully contiguous, and that there is exactly one unique sequence of corridors connecting any pair of modules without retracing steps.

Due to a reactor failure, the station must operate on emergency power. There are **t** critical modules that house essential life-support systems. The commander must define a safe subnetwork by choosing a collection of corridors to keep pressurized. The chosen subnetwork must be functionally contiguous with respect to the critical modules: it must be possible to navigate between any two critical modules exclusively by traversing the chosen pressurized corridors. Non-critical modules may be included in this safe subnetwork to serve as transit nodes.

Pressurizing a corridor requires a specific continuous power draw. Corridors excluded from the collection are depressurized and impassable. Calculate the minimum total power draw required to maintain a collection of pressurized corridors that successfully integrates all **t** critical modules.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1). The given corridors strictly satisfy the unique connectivity guarantee described above.
The second line contains **t** distinct integers: the identifiers of the critical modules.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a corridor linking module **u** and module **v** that requires **w** units of power to pressurize.

## Output

Print a single integer: the minimum total power draw required to keep all critical modules functionally interconnected.

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