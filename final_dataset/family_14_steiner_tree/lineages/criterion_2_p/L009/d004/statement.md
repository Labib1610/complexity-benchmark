# Differential Sensor Deployment

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility monitors **N** continuous environmental parameters, labeled 1 through **N**.

There are **E** differential sensors available for deployment. Each sensor can measure the exact relative difference (i.e., $p_u - p_v$) between a specific pair of parameters, $p_u$ and $p_v$. Deploying a sensor that measures the difference between parameter **u** and parameter **v** incurs a calibration cost of **w**. 

The full set of available sensors is minimally comprehensive: if all of them were deployed, it would be possible to calculate the exact difference between any two parameters in the facility, and removing any single sensor from the full set would make this impossible for at least one pair.

A subset of **F** parameters are designated as critical. You must choose a subset of the available sensors to deploy such that the exact difference between any two critical parameters can be logically deduced using exclusively the measurements from the deployed subset. (Measurements involving non-critical parameters may be used as intermediate terms in this calculation as long as their sensors are deployed).

Determine the minimum total calibration cost required to deploy a valid subset of sensors.

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the labels of the critical parameters.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing an available sensor between parameter **u** and parameter **v** with a calibration cost of **w**.

## Output

Print a single integer: the minimum total calibration cost required such that the differences between all critical parameters can be deduced.

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