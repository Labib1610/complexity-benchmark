# Problem B — Relative Calibration

Time limit: 2 s
Memory limit: 256 MB

## Description

An array of **n** sensors (numbered 1 to **n**) is being calibrated. You cannot measure the absolute reading of any sensor. Instead, there are **m** available pairwise calibration procedures. Each procedure compares two specific sensors, determining the exact numerical difference between their readings. The available procedures are comprehensive enough that, if all were performed, you could mathematically deduce the relative difference between any two sensors in the entire array.

The project requires establishing the relative differences among a specific group of **t** target sensors. You must select a subset of the available procedures to perform such that the relative difference between every pair of these **t** target sensors can be deduced (possibly using other non-target sensors as intermediaries in the calculations). 

Each procedure has a known financial cost to execute. You must find a valid selection of procedures that minimizes the total execution cost, and report this minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line contains **t** distinct integers: the identifiers of the target sensors.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing an available calibration procedure between sensor **u** and sensor **v** that costs **w** to execute. It is guaranteed that the full set of **m** procedures can relate all **n** sensors.

## Output

Print a single integer: the minimum total execution cost of the procedures required to deduce the relative differences among all target sensors.

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