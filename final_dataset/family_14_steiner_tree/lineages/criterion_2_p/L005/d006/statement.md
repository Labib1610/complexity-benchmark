# Relative Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description

A metrology lab needs to calibrate a system of **n** sensors, numbered 1 through **n**. While absolute readings cannot be directly measured, the lab can evaluate relative differences between specific pairs of sensors. A subset of **t** sensors are designated as primary and must be cross-calibrated against each other.

The lab has a catalog of **m** available calibration procedures. Each procedure compares a specific pair of sensors and yields the exact mathematical difference between their baseline values. Executing a procedure incurs a certain computational cost. 

Your objective is to select a subset of these calibration procedures to execute such that the relative differences between all pairs of primary sensors become mathematically determined (either directly from a single procedure or deduced by combining multiple procedures). You must find the absolute minimum total computational cost required to achieve this.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **n** ≤ 200000, **m** = **n** - 1, 1 ≤ **t** ≤ **n**).

The second line provides **t** distinct integers representing the identifiers of the primary sensors.

The subsequent **m** lines each contain three integers **u**, **v**, and **w**. These values describe a potential calibration procedure between sensor **u** and sensor **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**) that incurs a computational cost of **w** (1 ≤ **w** ≤ 1000000). It is guaranteed that if all **m** available procedures were executed, the relative differences between all **n** sensors would be fully determined.

## Output

Print a single integer indicating the minimum total computational cost required to ensure the relative differences between all pairs of primary sensors are mathematically determined.

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

## Note

In Example 1, the relative difference between primary sensors 1 and 4 can only be deduced by combining the procedures for (1,2), (2,3), and (3,4). Thus, all three procedures (costing 5+1+2 = 8) must be executed. 

In Example 2, there is only one primary sensor, so no relative differences need to be determined, requiring a computational cost of 0.