# Problem A — Seasonal Wildlife Relocation

Time limit: 5 s
Memory limit: 256 MB

## Description
In wildlife conservation, managing the seasonal migration of animal populations through ecological corridors is a standard network routing task. You are provided with a network of $n$ reserves and $m$ one-way corridors. Each corridor has a fixed integer carrying capacity, which is the absolute maximum number of animals that can safely pass through it in a single season.

This season, there are $k$ specific migration groups. Each group has a designated source reserve, a designated sink reserve, and a precise integer number of animals that must be routed.

Because all groups share the same physical network, the sum of animals from all groups passing through any single corridor cannot exceed that corridor's carrying capacity. Furthermore, since we are tracking individual animals, the number of animals of any group assigned to any corridor must be a non-negative integer.

The standard principle of conservation applies to every group individually: for any reserve that is not a group's source or sink, the number of animals of that group entering the reserve must exactly equal the number leaving. At a group's source, its net outbound movement must exactly match its required migration size. At its sink, its net inbound movement must match this same size.

Given the integer capacities and the strict conservation requirements, determine if a valid integer routing exists for all groups simultaneously, and if so, output it.

## Input
The first line contains three integers $n$ (the number of reserves), $m$ (the number of corridors), and $k$ (the number of migration groups).
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the source reserve, the sink reserve, and the required number of animals for the $i$-th group.
The following $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way corridor from reserve $u$ to reserve $v$ with a carrying capacity of $cap$ animals.

## Output
If a valid routing plan exists, print `YES`. Then, print $k$ lines, each containing $m$ integers. The $i$-th line must list the number of animals of group $i$ passing through each of the $m$ corridors, in the exact order the corridors were given in the input.
If no such plan is possible, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 2
2 3 1
1 2 2
2 4 1
1 3 1
3 4 2
2 3 1
```

**Output:**
```
YES
1 1 1 1 0
0 0 0 0 1
```
