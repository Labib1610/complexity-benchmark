# Facility Ventilation Integration

Time limit: 2 s   Memory limit: 256 MB

## Description

An underground facility consists of **N** pressure chambers, labeled 1 through **N**.

The facility contains **E** potential ventilation shafts. Each shaft can be bored to link a specific pair of chambers, **u** and **v**, requiring a known excavation effort of **w**. The geological survey confirms that the proposed shafts provide exact facility-wide access: if all **E** shafts were bored, air could circulate between any two chambers in the facility, with exactly one simple sequence of shafts connecting any given pair.

A specific subset of **F** chambers are designated as *vital*. You must select a subset of the potential shafts to bore so that air can circulate between any two vital chambers using only the bored shafts. Air may pass through non-vital chambers, provided the shafts along the route are also bored.

Determine the minimum total excavation effort required to ensure all vital chambers are integrated in this manner. (If **F** = 1, no shafts need to be bored, so the minimum total effort is 0.)

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the labels of the vital chambers.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing a potential shaft between chamber **u** and chamber **v** with an excavation effort of **w**.

## Output

Print a single integer: the minimum total excavation effort required to ensure all vital chambers can circulate air among themselves.

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