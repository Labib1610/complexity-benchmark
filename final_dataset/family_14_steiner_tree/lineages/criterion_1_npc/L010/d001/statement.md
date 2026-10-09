# Problem A — Cabling the Required Sites

Time limit: 5 s   Memory limit: 256 MB

## Description

A campus consists of **n** sites, identified by integers from 1 to **n**. You can install cabling between certain pairs of sites, with each possible connection incurring a specific cost. A specific subset of **t** sites has been designated as required.

You must choose which cabling connections to install such that every required site is mutually reachable from every other required site. No connectivity condition is imposed on sites that are not required. Determine the minimum total installation cost necessary to achieve this.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers representing the required sites.
The subsequent **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a cabling connection can be installed between site **u** and site **v** for a cost of **w**.
It is guaranteed that the available connections are sufficient to establish communication between all required sites.

## Output

Output a single integer representing the minimum total cost to ensure all required sites are mutually reachable.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, establishing connections through site 4 (which costs 1+1+1 = 3) is cheaper than connecting the three required sites without it (which would cost 4). In Example 3, there is only one required site, so no cabling needs to be installed.