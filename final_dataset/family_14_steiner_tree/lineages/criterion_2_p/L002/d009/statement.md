# Sparse Linear Subsystem Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a homogeneous linear system over $n$ real variables $x_1, x_2, \ldots, x_n$.

You are provided with a pool of $m$ candidate equations. Each candidate equation is specified by two indices $u$ and $v$ and an activation cost $w$. Activating this candidate adds the equation $x_u - x_v = 0$ to your system.

To ensure the system is well-posed, you are guaranteed that the full pool of $m$ candidate equations is minimally sufficient to collapse the variables to a single value. Specifically, if you were to activate all $m$ equations, the solution space would be restricted to exactly the one-dimensional subspace where $x_1 = x_2 = \ldots = x_n$. Furthermore, the candidate equations are strictly non-redundant: omitting any single equation from the full pool of $m$ would increase the dimension of the solution space.

You are given a target set of $t$ critical variables. You must select a subset of the candidate equations to activate. Your objective is to ensure that in the solution space of the resulting subsystem, the condition $x_i = x_j$ is algebraically entailed for all pairs of critical variables $i, j$. You may activate equations involving non-critical variables if they are necessary to establish this entailment.

Find the minimum total activation cost of a selected subset of equations that achieves this objective. The total cost is the sum of the activation costs $w$ of the equations you choose to activate.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$). 
The second line contains $t$ distinct integers: the indices of the critical variables.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a candidate equation $x_u - x_v = 0$ which requires a cost of $w$ to activate.

The provided set of $m$ candidate equations strictly satisfies the minimal sufficiency and non-redundancy guarantees described above.

## Output

Print a single integer: the minimum total activation cost of a subset of equations whose activation algebraically entails that all critical variables must take the same value.

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