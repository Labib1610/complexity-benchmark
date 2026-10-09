# Problem B — Relative Calibration

Time limit: 2 s
Memory limit: 256 MB

## Description

A facility contains **n** sensors, labeled from 1 to **n**. Because their absolute baseline readings are unobservable, their calibration must rely entirely on pairwise comparisons. You are given a roster of **m** potential testing operations. A single operation evaluates a specific pair of sensors and yields the precise numerical offset between them. 

The roster of operations provides full coverage of the facility: executing all of them would allow you to calculate the relative offset between any two sensors in the system. To avoid redundant testing, the roster contains exactly **n** − 1 operations, which guarantees there is exactly one unique sequence of tests linking any given pair of sensors.

Your objective focuses on a designated priority group of **t** sensors. You need to choose a subset of the testing operations so that the relative offset between every pair of these **t** priority sensors can be determined. You are allowed to include tests involving non-priority sensors if they help bridge the calculations between the priority ones.

Each testing operation carries a specific monetary cost. Determine the minimum total cost required to fund a valid subset of operations that fully integrates the priority sensors.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line lists **t** distinct integers representing the labels of the priority sensors.
Following this are **m** lines, each containing three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). These values indicate a potential testing operation that evaluates sensor **u** and sensor **v** at a cost of **w**. It is guaranteed that the given **m** operations can relate all **n** sensors, forming the structure described above.

## Output

Output a single integer representing the minimum possible total cost to execute the necessary operations to deduce the offsets among all priority sensors.

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