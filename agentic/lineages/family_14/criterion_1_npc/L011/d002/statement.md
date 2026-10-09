# Problem A — Pneumatic Infrastructure

Time limit: 5 s   Memory limit: 256 MB

## Description

An industrial complex contains **n** buildings (numbered 1 through **n**). You have a catalog of potential bidirectional pneumatic transport tubes that can be constructed between specific pairs of buildings. Each potential tube has a known construction cost.

Due to an impending inspection, a roster of **t** specific buildings are flagged as *audit-critical*. The inspection requires that all audit-critical buildings be fully interconnected. This means a physical canister must be able to travel between any two audit-critical buildings, possibly passing through other intermediate buildings via a contiguous sequence of constructed tubes.

You may select any combination of the available tubes to construct. Determine the minimum possible total cost required to ensure all audit-critical buildings are interconnected.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the audit-critical buildings.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a potential tube between building **u** and building **v** with a construction cost of **w**.
It is guaranteed that the available potential tubes are sufficient to interconnect all audit-critical buildings.

## Output

Print a single integer: the minimum total construction cost.

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

In Example 1, constructing the tubes that join building 4 to buildings 1, 2, and 3 incurs a total cost of 1 + 1 + 1 = 3. This successfully interconnects the audit-critical buildings (1, 2, and 3) and is more economical than linking them exclusively using direct connections between each other, which would cost at least 4. In Example 3, there is only one audit-critical building, so no tubes need to be constructed.