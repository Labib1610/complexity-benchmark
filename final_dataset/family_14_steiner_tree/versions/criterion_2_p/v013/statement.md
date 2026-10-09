# Optimal Link Activation

Time limit: 2 s
Memory limit: 256 MB

## Description

A large-scale communication grid consists of **n** facilities (numbered 1 to **n**). Among these, a specific subset of **t** facilities are designated as critical and must be able to exchange data with one another. Data exchange is possible if there is a sequence of active links connecting them.

You are provided with a list of **m** potential bidirectional links, each with an associated activation cost. Your task is to select a subset of these links to activate. Any of the $2^m$ possible configurations of active links can be chosen. A configuration is valid if all **t** critical facilities belong to the same connected component; they may route data through non-critical facilities if necessary. Your goal is to find a valid configuration that minimizes the sum of the activation costs.

To ensure baseline connectivity is theoretically possible, the infrastructure was designed such that activating all **m** links would allow data exchange between any pair of the **n** facilities. Furthermore, the total number of potential links **m** is exactly **n** − 1. 

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line contains **t** distinct integers: the identifiers of the critical facilities.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating a potential link between facility **u** and facility **v** with an activation cost of **w**.
It is guaranteed that activating all **m** links connects all **n** facilities.

## Output

Print a single integer: the minimum total cost of a valid configuration.

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
