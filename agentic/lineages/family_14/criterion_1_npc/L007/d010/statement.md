# Sequence Divergence Bounds

Time limit: 5 s   Memory limit: 256 MB

## Description

You are studying a mathematical system of **n** unknown infinite sequences of real numbers. Let the $i$-th sequence be denoted as $X_i = (X_{i,1}, X_{i,2}, X_{i,3}, \dots)$.

There are **m** available bounding conditions you can enforce on this system. The $j$-th available condition applies to the sequences $X_u$ and $X_v$, and guarantees that the infinite sum of their absolute element-wise differences is bounded by 1:
$$ \sum_{k=1}^{\infty} |X_{u,k} - X_{v,k}| \le 1 $$
Enforcing this specific condition incurs a penalty of **w**.

You are given a priority collection of **t** key sequence indices. Your goal is to enforce a subset of the available conditions such that the following strict mathematical consequence holds:
For every pair of distinct sequence indices $a$ and $b$ in your priority collection, the infinite sum $\sum_{k=1}^{\infty} |X_{a,k} - X_{b,k}|$ is guaranteed to converge to a strictly finite value. This convergence must hold for ANY possible assignment of real numbers to the sequences $X_1, \dots, X_n$, provided they satisfy all of your enforced conditions.

Determine the minimum total penalty required to enforce a subset of conditions that achieves this guarantee.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the indices of the priority sequences.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000): an available condition applying to sequences **u** and **v**, and the penalty **w** to enforce it.
The provided set of available conditions is always sufficient to satisfy the requirement.

## Output

Print a single integer: the minimum total penalty required to enforce a subset of conditions that guarantees finite convergence for all priority pairs.

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

In Example 1, enforcing the conditions on (1,4), (2,4), and (3,4) incurs a penalty of $1 + 1 + 1 = 3$. For any sequences satisfying these bounds, the triangle inequality guarantees that for any priority pair, such as 1 and 2:
$$ \sum_{k=1}^{\infty} |X_{1,k} - X_{2,k}| \le \sum_{k=1}^{\infty} |X_{1,k} - X_{4,k}| + \sum_{k=1}^{\infty} |X_{4,k} - X_{2,k}| \le 1 + 1 = 2 $$
Thus, the infinite sum is guaranteed to be strictly finite. This is the minimum possible penalty to achieve the guarantee for all priority pairs.

In Example 3, with only one priority sequence, there are no distinct pairs to constrain, so choosing no conditions satisfies the requirement vacuously with a penalty of 0.