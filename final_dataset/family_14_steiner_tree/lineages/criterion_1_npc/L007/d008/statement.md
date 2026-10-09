# Invariant Functions

Time limit: 5 s   Memory limit: 256 MB

## Description

You are studying the symmetries of real-valued multivariate functions $f(x_1, \dots, x_n)$ over $n$ variables.

There are **m** available swap operations you can enable. The $i$-th available operation swaps the variables at indices **u** and **v**. Enabling this operation incurs a cost of **w**.

A function $f$ is considered *invariant* under a swap of variables at indices **u** and **v** if exchanging the input values at positions **u** and **v** never changes the output of the function, regardless of the values of any variables.

You are given a target set of **t** key variable indices. Your goal is to enable a subset of the available operations such that the following strict condition holds:
Any real-valued function $f$ that is invariant under **all** of your enabled operations must logically also be invariant under the swap of variables at indices $a$ and $b$, for every distinct pair of indices $a, b$ in your target set.

Determine the minimum total cost required to enable a subset of operations that achieves this guarantee.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the target variable indices.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an available operation swapping the variables at indices **u** and **v**, and its cost **w**.
The provided set of available operations is sufficient to achieve the required guarantee.

## Output

Print a single integer: the minimum total cost required to enable a subset of operations that achieves the condition.

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

In Example 1, enabling the operations involving index 4 (swapping 1 and 4, 2 and 4, and 3 and 4 at a cost of 1 + 1 + 1 = 3) ensures that any function invariant under these three swaps is also invariant under any swap between variables 1, 2, and 3. This incurs a lower cost than enabling the direct swaps among the target variables.

In Example 3, with only one target index, there are no distinct target pairs to enforce, so choosing no operations has a total cost of 0.