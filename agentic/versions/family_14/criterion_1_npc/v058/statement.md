# Substation Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

A regional infrastructure project involves a power grid of exactly **n** substations. Between various pairs of these substations, there are **m** bidirectional transmission corridors. Each corridor has a known electrical impedance. 

Among the **n** substations, exactly **t** of them are designated as primary generators. The remaining substations in the grid function as standard routing relays. Any standard relay can be utilized to pass signals between connected corridors. 

A configuration of the grid requires choosing a subset of the available transmission corridors to become active. When a corridor is active, it incurs its impedance as a continuous cost. A configuration is considered phase-stable if and only if it is possible to travel from any primary generator to any other primary generator using only the active corridors and the substations they connect.

Given the layout of the grid and the locations of the primary generators, your objective is to find a phase-stable configuration. Specifically, you must output the absolute minimum possible total impedance of any active subset of corridors that achieves phase stability.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the identifiers of the primary generators.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a transmission corridor between substation **u** and substation **v** with impedance **w**.
It is guaranteed that at least one phase-stable configuration exists.

## Output

Print a single integer: the exact minimum total impedance required for a phase-stable configuration.

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

In Example 1, the primary generators are substations 1, 2, and 3. Connecting them directly using the corridors between 1 and 2, and between 2 and 3, would result in a total impedance of 4. However, activating the corridors (1,4), (2,4), and (3,4)—which route through the standard relay substation 4—yields a total impedance of 3, which is the optimal phase-stable configuration.

In Example 3, there is only one primary generator. A configuration with zero active corridors is already phase-stable, resulting in a total impedance of 0.
