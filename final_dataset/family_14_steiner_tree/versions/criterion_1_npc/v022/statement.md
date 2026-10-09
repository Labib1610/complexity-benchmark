# Substation Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

A high-voltage power grid consists of **n** substations and **m** bidirectional transmission corridors. Each corridor connects two substations and has a known impedance. 

Within this grid, exactly **t** substations are designated as *primary generators*. To maintain phase stability, all **t** primary generators must be synchronized, meaning they must all be connected to each other through a chosen subset of the transmission corridors. The remaining substations act as optional routing relays; you may include any number of them in your synchronized subset if it reduces the total impedance.

Because the primary generators are few (**t** ≤ 10), their pairwise shortest routes can be mapped efficiently. In certain simple topologies, simply linking the generators via these shortest routes provides an optimal connection. For the provided grid, however, you must determine the absolute minimum total impedance of any set of corridors that successfully connects all **t** primary generators.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the primary generators.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a transmission corridor between substation u and substation v with impedance w.
It is guaranteed that a valid set of corridors exists to connect all primary generators.

## Output

Print a single integer: the exact minimum total impedance required to connect all primary generators.

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

In Example 1, the primary generators are 1, 2, and 3. The shortest route between any pair of primary generators (e.g., 1 and 2) directly has an impedance of 2. Linking them via these direct routes would result in a total impedance of 4. However, routing the synchronization through the optional relay substation 4 uses corridors (1,4), (2,4), and (3,4), each with impedance 1, yielding a lower total impedance of 3.

In Example 3, there is only one primary generator, so no corridors are needed, resulting in a total impedance of 0.
