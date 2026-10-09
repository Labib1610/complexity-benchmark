# Problem B — Synchronization Topology

Time limit: 2 s   Memory limit: 256 MB

## Description

A network architecture is composed of **n** distinct modules, indexed 1 through **n**. The architecture design includes a set of **m** potential data conduits. Each conduit bridges exactly two modules and requires a specific energy expenditure to power on.

The blueprint of these conduits adheres to a strict topological specification:
1. The total number of potential conduits **m** is exactly **n − 1**.
2. The conduits are arranged such that a valid routing sequence of one or more conduits exists between any pair of modules in the network.

Within this architecture, a specific subset of **t** modules are designated as critical synchronization nodes. 

Your objective is to determine the minimum total energy expenditure required to power on a selection of conduits such that every critical synchronization node can exchange data with every other critical synchronization node. Data may freely pass through non-critical modules as part of a route.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line contains **t** distinct integers representing the indices of the critical synchronization nodes.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). This indicates a potential data conduit between module **u** and module **v** requiring an energy expenditure of **w** to power on. The conduit configuration is guaranteed to follow the topological specification described above.

## Output

Output a single integer representing the minimum total energy expenditure required to power on conduits so that all critical synchronization nodes can communicate with one another.

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

In Example 1, the critical synchronization nodes 1 and 4 can only exchange data if the transmission passes through modules 2 and 3. As a result, all three available conduits (requiring energy expenditures of 5, 1, and 2) must be powered on, resulting in a total expenditure of 8.
In Example 2, there is only one critical synchronization node, so no conduits need to be powered on and the total expenditure is 0.
