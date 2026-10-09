# Equivalence Deduction

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of $n$ unknown variables, denoted $x_1, x_2, \dots, x_n$. You are provided with a set of $m = n - 1$ potential equality constraints. Each constraint specifies that two particular variables are equal ($x_u = x_v$), and has a specific verification cost $w$ to activate.

The set of potential constraints is minimal and complete: if you were to activate all $m$ constraints, it would logically imply that all $n$ variables are equal. Because $m = n - 1$, there are no redundant constraints (removing any constraint from the full set would mean not all $n$ variables are guaranteed to be equal).

A client has specified a target list of $t$ variables. Your objective is to select a subset of the potential constraints to activate such that the activated constraints logically guarantee that all $t$ target variables are equal to each other. Variables not in the target list may also end up being equal to the target variables, which is permissible and often necessary to establish the required logical chain.

Determine the minimum total verification cost of a subset of constraints that must be activated to satisfy the client's requirement. Any constraint not needed for this logical deduction can be left inactive.

## Input

The first line provides three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line provides $t$ distinct integers, representing the indices of the target variables.
The next $m$ lines each contain three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), indicating a potential constraint $x_u = x_v$ with a verification cost of $w$.

## Output

Output a single integer: the minimum total verification cost of the activated constraints that guarantee all $t$ target variables are equal.

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