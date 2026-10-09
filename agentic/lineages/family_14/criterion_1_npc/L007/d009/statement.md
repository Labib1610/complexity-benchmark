# Coordinate Indifference

Time limit: 5 s   Memory limit: 256 MB

## Description

You are studying the properties of real-valued multivariate functions $f(x_1, \dots, x_n)$ over $n$ coordinates.

A function $f$ is considered *indifferent* to a transposition of coordinates $u$ and $v$ if exchanging the input values at positions $u$ and $v$ never changes the output of the function, regardless of the values of any coordinates. Formally, for all possible inputs, $f(\dots, x_u, \dots, x_v, \dots) = f(\dots, x_v, \dots, x_u, \dots)$.

There are **m** available transposition operations you can activate. The $i$-th available operation transposes the coordinates at indices **u** and **v**. Activating this operation incurs a penalty of **w**.

You are given a priority collection of **t** key coordinate indices. Your goal is to activate a subset of the available operations such that the following strict condition holds:
Any real-valued function $f$ that is indifferent to **all** of your activated transpositions is necessarily indifferent (as a logical consequence) to a transposition of coordinates $a$ and $b$, for every distinct pair of indices $a, b$ in your priority collection.

Determine the minimum total penalty required to activate a subset of operations that achieves this guarantee.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the priority coordinate indices.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000): an available operation transposing the coordinates at indices **u** and **v**, and its penalty **w**.
The provided set of available operations is always sufficient to satisfy the required condition.

## Output

Print a single integer: the minimum total penalty required to activate a subset of operations that achieves the condition.

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

In Example 3, with only one priority coordinate, there are no distinct pairs to enforce, so choosing no operations satisfies the condition vacuously with a total penalty of 0.