# Problem B — Fiber-Optic Monitoring

Time limit: 2 s
Memory limit: 256 MB

## Description

An underground facility consists of **n** chambers (numbered 1 to **n**). Passageways connect certain pairs of chambers. The facility was constructed such that there are exactly **n − 1** passageways in total, and there is exactly one route of passageways between any two chambers.

A subset of **t** chambers contain structural anomalies. Engineers need to deploy a continuous fiber-optic monitoring network that links all chambers containing anomalies. 

The fiber-optic cable must be routed through the existing passageways. Installing cable in a given passageway requires a specific number of work-hours. The network can branch at any chamber, meaning anomalous chambers can be linked either directly or by routing through intermediate chambers. 

Calculate the minimum total work-hours required to install a continuous fiber-optic network that connects every anomalous chamber.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifying numbers of the chambers containing structural anomalies.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a passageway connecting chamber u and chamber v that requires w work-hours for cable installation. The passageways form the structure described above.

## Output

Print a single integer: the minimum total work-hours needed to connect all anomalous chambers.

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

In Example 1, the anomalous chambers 1 and 4 are linked only by passing through chambers 2 and 3. Therefore, cable must be installed in all three passageways, requiring 5 + 1 + 2 = 8 work-hours. In Example 2, there is only one anomalous chamber, so no cable installation is needed.
