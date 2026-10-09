# Inter-Departmental Synergy

Time limit: 5 s
Memory limit: 256 MB

## Description

A large corporation has **n** departments (numbered 1 to **n**). The board of directors has identified **t** "core" departments. These core departments must be fully integrated, meaning that any core department can share information with any other core department, either directly or via a sequence of intermediate departments.

Information sharing happens through bidirectional communication streams. There are **m** possible streams that can be established between pairs of departments. Establishing a stream between department **u** and department **v** incurs an annual cost of **w**. 

You may establish streams between any departments (core or non-core). A non-core department can act as an intermediary, passing information between other departments. Your task is to determine the minimum total annual cost to establish a set of streams such that all **t** core departments are integrated.

Due to corporate regulations and budget caps, every valid scenario guarantees the following:
* The total number of possible streams **m** evaluated by the board is strictly less than 5000.
* No individual stream will ever have an annual cost **w** equal to or exceeding $10^7$.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the core departments.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating a possible stream between department u and department v with annual cost w.
It is guaranteed that it is possible to integrate all core departments using the available streams.

## Output

Print a single integer: the minimum total annual cost to integrate all core departments.

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

In Example 1, routing information through the non-core department 4 (costs 1+1+1 = 3) is cheaper than integrating the three core departments directly (which would cost 4). In Example 3 there is only one core department, so no streams need to be established.
