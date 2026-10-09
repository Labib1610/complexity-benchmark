# Datacenter Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

A computing facility houses **n** server racks, indexed from 1 to **n**. The building is pre-wired with exactly **n − 1** fiber-optic links. The topology of these links guarantees that, when all are powered on, there is exactly one unique communication route between any given pair of racks. Powering on each link incurs a specific activation expense.

A customer has rented a specific group of **t** racks. Your objective is to power on a selection of the fiber-optic links so that every rented rack can exchange data with every other rented rack. Data can be routed through racks that the customer has not rented.

The total activation expense for your network is calculated by summing two components:
1. The individual activation expenses of all powered-on fiber-optic links.
2. A relay activation fee for every unrented rack that is included in the active communication routes.

Currently, the relay activation fee is fixed at 0 per unrented rack. Calculate the minimum total activation expense necessary to tie all the rented racks together, ensuring you incorporate both the link expenses and the relay activation fees into your final calculation.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers, which are the indices of the rented racks.
The next **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000). This indicates a pre-wired fiber-optic link between rack **u** and rack **v** that costs **w** to power on. The given infrastructure of **m** links guarantees that exactly one valid sequence of links exists between any two racks when fully powered on.

## Output

Output a single integer: the minimum total activation expense to power on the required links and racks.

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