# Problem B — Relative Calibration

Time limit: 2 s
Memory limit: 256 MB

## Description

A facility contains **n** sensors, labeled from 1 to **n**. Because their absolute baseline readings are unobservable, their calibration relies entirely on pairwise comparisons. You are provided with a roster of **m** potential testing operations. Each operation evaluates a specific pair of sensors and yields the precise numerical offset between them.

The roster of operations constitutes a minimal basis for the facility: executing all of them allows the calculation of the relative offset between any two sensors in the system, but omitting even one operation would leave some offsets unresolvable. 

Your objective centers on a designated priority group of **t** sensors. You must select a subset of the testing operations such that the relative offset between every pair of these **t** priority sensors can be deduced. You may include tests involving non-priority sensors if they act as intermediaries in the calculations between the priority ones.

Each testing operation requires a specific monetary cost. Determine the minimum total cost needed to fund a valid subset of operations that fully calibrates the priority sensors relative to one another.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line lists **t** distinct integers representing the labels of the priority sensors.
Following this are **m** lines, each containing three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). These values indicate a potential testing operation that evaluates sensor **u** and sensor **v** at a cost of **w**. It is guaranteed that the given **m** operations provide the minimal basis described above.

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