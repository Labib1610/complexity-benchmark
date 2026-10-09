# Satisfiability of Bounded Integer States

Time limit: 2 s   Memory limit: 256 MB

## Description
You are tasked with finding a valid discrete assignment vector $\vec{x} = (x_1, x_2, \dots, x_m)$ for a system of $m$ bounded integer variables subject to $n$ linear equality constraints. Each variable $x_j$ is associated with an ordered pair of constraint indices $(u, v)$ and is restricted to a finite domain $\{0, 1, \dots, C_j\}$. The Cartesian product of these domains creates a massive combinatorial state space of size $\prod_{j=1}^m (C_j + 1)$.

A configuration $\vec{x}$ is considered valid if and only if it simultaneously satisfies all $n$ linear equations in the system. Each constraint $i \in \{1, \dots, n\}$ is formulated by summing the variables that contain $i$ in their associated ordered pair. Let $P_i$ be the sum of all variables $x_j$ whose associated pair has $i$ as its second element, and let $Q_i$ be the sum of all variables $x_j$ whose associated pair has $i$ as its first element. 

The system dictates that $P_i - Q_i = E_i$ for all $i$. For the vast majority of the constraints, the required constant $E_i$ is exactly $0$, enforcing a perfect balance. However, the system includes an active boundary condition defined by a starting index $s$, a terminating index $t$, and a target magnitude $d$. To satisfy this condition, the constants for these two specific constraints are fixed at $E_s = -d$ and $E_t = d$. 

Your objective is to determine whether there exists at least one vector $\vec{x}$ in the state space that satisfies this entire system of equations. If such an assignment exists, you must output it.

## Input
Line 1: Three integers $n$, $m$, and $1$ (representing the number of linear constraints, the number of variables, and the active boundary conditions).
Line 2: Three integers $s$, $t$, and $d$ (the starting index, terminating index, and the target magnitude).
Next $m$ lines: Three integers $u$, $v$, and $C_j$, representing a variable associated with the ordered pair $(u, v)$ and its maximum domain value $C_j$.

## Output
If a satisfying vector $\vec{x}$ exists, output `YES` on the first line, followed by a second line containing $m$ integers representing the assigned values $x_1, x_2, \dots, x_m$ in the exact order the variables were provided in the input. If no such assignment exists, output `NO`.

## Example

### Input
```text
4 5 1
1 4 8
1 2 5
1 3 5
2 4 4
3 4 4
2 3 2
```

### Output
```text
YES
4 4 4 4 0
```
