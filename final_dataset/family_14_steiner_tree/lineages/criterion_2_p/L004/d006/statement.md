# Rigid State Coupling

Time limit: 2 s
Memory limit: 256 MB

## Description

You are analyzing the configuration space of a system described by a state vector $\mathbf{x} = [x_1, x_2, \dots, x_n]^T \in \mathbb{R}^n$. The system has $n$ degrees of freedom, indexed 1 to $n$.

You are provided with a pool of $m$ optional locking mechanisms. Each mechanism is defined by two indices $u$ and $v$ and a cost $w$. Activating this mechanism restricts the state vector to the hyperplane orthogonal to $\mathbf{e}_u - \mathbf{e}_v$ (where $\mathbf{e}_k$ is the $k$-th standard basis vector of $\mathbb{R}^n$), which incurs a one-time cost of $w$.

The pool of mechanisms forms a minimal basis for full rigidity: there are exactly $m = n - 1$ mechanisms available, and if you were to activate all of them, the allowable state space would be reduced to exactly the 1-dimensional subspace spanned by the all-ones vector $\mathbf{1} = [1, 1, \dots, 1]^T$.

Your objective is to activate a subset of these mechanisms such that a specific list of $t$ critical indices are strictly coupled. That is, for any valid state vector $\mathbf{x}$ in the subspace defined by your activated subset, the components of $\mathbf{x}$ at the $t$ critical indices must all be equal to each other. The values of the remaining non-critical components do not matter, as long as the activated mechanisms are respected.

What is the minimum total cost of the mechanisms you must activate to ensure the $t$ critical indices are unconditionally coupled?

## Input

The first line contains three integers **n**, **m**, and **t**. The number of degrees of freedom is **n** (1 ≤ **n** ≤ 200000). The number of available mechanisms **m** is always exactly **n** − 1. The number of critical indices is **t** (1 ≤ **t** ≤ **n**).
The second line contains **t** distinct integers: the identifiers of the critical indices.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. These denote an optional mechanism restricting the state vector to the hyperplane orthogonal to $\mathbf{e}_u - \mathbf{e}_v$ (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), which costs **w** to activate (1 ≤ **w** ≤ 1000000).

## Output

Print a single integer: the minimum total cost required.

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