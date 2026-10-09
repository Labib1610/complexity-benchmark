# Subspace Constraint Optimization

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a vector space $V = \mathbb{R}^n$. The coordinates of any vector $y \in V$ are denoted as $y_1, y_2, \dots, y_n$.

There is a proposed set of $m$ linear constraints. Each proposed constraint is defined by a pair of coordinate indices $u$ and $v$, representing the equation $y_u = y_v$, and has an associated activation cost $w$. You are guaranteed that $m = n - 1$, and that the intersection of all $m$ proposed constraints forms exactly the 1-dimensional subspace where all $n$ coordinates are equal (i.e., $y_1 = y_2 = \dots = y_n$).

You are given a set of $t$ focal coordinate indices. You must select a subset of the proposed constraints to activate. Your selected subset defines a subspace $W \subseteq V$ consisting of all vectors $y$ that satisfy every constraint in your subset. You require that for every vector $y \in W$, the values of all $t$ focal coordinates are exactly equal to each other. You may activate constraints involving non-focal coordinates if they help satisfy this algebraic requirement.

Find the minimum total activation cost of a selected subset of constraints that satisfies this requirement. The total cost is the sum of the activation costs $w$ of the constraints you choose to activate.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$). The proposed constraints strictly satisfy the intersection guarantee described above.
The second line contains $t$ distinct integers: the focal coordinate indices.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a proposed constraint $y_u = y_v$ that requires a cost of $w$ to activate.

## Output

Print a single integer: the minimum total cost of a subset of constraints whose defined subspace forces all focal coordinates to be equal.

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