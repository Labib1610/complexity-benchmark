# Problem B — Module Integration Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description

You are tasked with designing a routing sub-network for a distributed system. The system contains **n** processing modules, numbered 1 through **n**. You are given a list of **m** potential bidirectional data conduits that can be deployed. Deploying a conduit between a specific pair of modules incurs a given installation cost.

There are **t** modules designated as critical processors. Your goal is to select a subset of the potential conduits to deploy so that all critical processors can transmit data to one another. Data can be relayed through non-critical modules if necessary.

Determine the minimum total installation cost required to achieve full connectivity among all critical processors.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ID numbers of the critical processors.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a potential conduit between module **u** and module **v** with an installation cost of **w**. The system architecture guarantees that deploying all **m** conduits would successfully connect all **n** modules into a single network.

## Output

Print a single integer representing the minimum total cost to deploy conduits such that all critical processors can communicate with each other.

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

In Example 1, the critical processors 1 and 4 can only communicate if the data passes through modules 2 and 3. Therefore, all three available conduits (costs 5, 1, and 2) must be deployed, giving a total cost of 8.
In Example 2, there is only one critical processor, so no conduits need to be deployed and the total cost is 0.