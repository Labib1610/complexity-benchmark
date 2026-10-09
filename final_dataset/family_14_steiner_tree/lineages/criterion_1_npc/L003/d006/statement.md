# Problem A — Constraint System Optimization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a system of $n$ unknown real variables, $x_1, x_2, \ldots, x_n$.

You are given a target set of $t$ distinct indices from $\{1, \dots, n\}$. Your goal is to ensure that all variables indexed by this target set are strictly identical, regardless of the overall assignment. 

To achieve this, you may activate constraints from a provided list of $m$ candidate constraints. Each candidate constraint is of the form $x_u = x_v$ (for some $u \neq v$) and has an associated activation cost. When a constraint is activated, any valid assignment of the variables must satisfy $x_u = x_v$. 

You must choose a collection of the candidate constraints to activate such that, in every possible valid assignment of real numbers to $x_1, \dots, x_n$ that satisfies all activated constraints, all variables in the target set are forced to take the exact same value. 

Determine the minimum possible total cost of a chosen collection of constraints that achieves this. Because intermediate variables can be shared to chain equalities together, independently satisfying pairwise conditions between target variables is often suboptimal; an activated constraint is paid for only once and can simultaneously contribute to aligning multiple targets. You must optimize the shared system of constraints as a whole.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line contains $t$ distinct integers: the indices in the target set.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a candidate constraint $x_u = x_v$ available for activation, which has an activation cost of $w$.
It is guaranteed that activating all $m$ candidate constraints successfully forces the target variables to be equal.

## Output

Print a single integer: the minimum total cost of a selected set of candidate constraints that achieves the goal.

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

In Example 1, activating the constraints $x_1 = x_4$, $x_2 = x_4$, and $x_3 = x_4$ (total cost $1+1+1 = 3$) ensures that $x_1 = x_2 = x_3 = x_4$. Any valid assignment must therefore give the target variables $x_1, x_2$, and $x_3$ the same value. This selection is cheaper than activating direct constraints between the target variables (which would cost at least 4). 
In Example 3, with only one index in the target set, no constraints need to be activated to force the single variable to equal itself, so the minimum cost is 0.