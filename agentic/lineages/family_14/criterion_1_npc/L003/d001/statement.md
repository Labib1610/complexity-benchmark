# Problem A — Establishing the Protocols

Time limit: 5 s   Memory limit: 256 MB

## Description

A system has **n** components (numbered 1..n). You can establish shared protocols between specific pairs of components; each available protocol has a specific cost to establish. Data can flow between any two components that share an established protocol, and can be forwarded through any chain of components that have established protocols.

You are given a list of **t** designated components. Your task is to select a set of protocols to establish such that data can be exchanged between any two of these **t** designated components. Any component in the system can be used to forward data. Determine the minimum total sum of costs for the set of protocols you establish.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the designated components.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an available shared protocol between components u and v that costs w to establish.
The available protocols are sufficient to allow all designated components to exchange data.

## Output

Print a single integer: the minimum total cost of the established protocols required to allow all designated components to exchange data with one another.

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

In Example 1, establishing protocols involving component 4 (costs 1+1+1 = 3) is cheaper than using protocols that only involve the designated components (which would cost 4). In Example 3 there is only one designated component, so no protocols need to be established.