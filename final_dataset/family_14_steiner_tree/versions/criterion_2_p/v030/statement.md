# Problem B — Facility Ventilation

Time limit: 2 s   Memory limit: 256 MB

## Description

An underground research facility consists of **n** chambers (numbered 1 to **n**). To maintain stability, certain pairs of chambers can be linked by opening a reinforced ventilation duct. There are **m** such ducts available in the facility's blueprint, each requiring a specific amount of energy to unseal.

The blueprint is designed with two strict structural rules regarding the available ducts:
1. There are exactly **n − 1** available ducts in total.
2. If every available duct were unsealed, air would be able to circulate between any two chambers in the facility through some sequence of ducts.

A specific set of **t** chambers are designated as priority zones. You must select a subset of ducts to unseal so that air can circulate among all priority zones. Specifically, for any pair of priority zones, there must exist a sequence of unsealed ducts that allows air to pass from one to the other (possibly passing through other non-priority chambers along the way). 

Determine the minimum total energy required to unseal a valid subset of ducts.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the priority zones.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an available duct between chamber u and chamber v that requires w energy to unseal. The available ducts follow the structural rules described above.

## Output

Print a single integer: the minimum total energy required to unseal the necessary ducts.

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

In Example 1, the priority zones 1 and 4 can only exchange air if the sequence of ducts passing through chambers 2 and 3 is unsealed, meaning all three available ducts (5 + 1 + 2 = 8) must be opened. In Example 2, there is only one priority zone, so the circulation requirement is already met without unsealing any ducts.
