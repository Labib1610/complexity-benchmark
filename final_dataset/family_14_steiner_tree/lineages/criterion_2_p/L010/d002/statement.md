# Industrial Component Routing

Time limit: 2 s   Memory limit: 256 MB

## Description

An industrial facility consists of **n** workstations. These workstations are connected by **m** bidirectional conveyor belts. The facility is completely integrated, meaning it is possible to route components between any two workstations via some sequence of belts.

Among all workstations, **t** of them are designated as quality control stations. For a specific inspection protocol, all quality control stations must be able to exchange components with one another. Components can flow freely through any conveyor belt that has been powered on. Powering on the conveyor belt between workstation **u** and workstation **v** incurs a specific energy cost **w**.

Determine the minimum total energy cost required to power on a subset of conveyor belts such that every quality control station can exchange components with every other quality control station (possibly routing through other intermediate workstations).

## Input

The first line contains three integers **n**, **m**, and **t**. The facility has at most 200000 workstations, so **n** is between 1 and 200000. The number of quality control stations **t** is at least 1 and at most **n**. The physical layout dictates that the number of conveyor belts **m** is always exactly one less than the number of workstations (**m** = **n** − 1).

The second line contains **t** distinct integers: the identifiers of the quality control stations.

Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a conveyor belt linking workstation **u** and workstation **v**. The energy cost **w** is at least 1 and is bounded by 1000000. The conveyor belts form the completely integrated structure described above.

## Output

Print a single integer: the minimum total energy cost to link all quality control stations.

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

In Example 1, the quality control stations 1 and 4 can only exchange components via workstations 2 and 3, so all three conveyor belts (costs 5, 1, and 2) must be powered on, totaling 8.
In Example 2, there is only one quality control station, so no conveyor belts need to be powered on.