# Satisfiability of Bounded Integer States

Time limit: 2 s   Memory limit: 256 MB

## Description
You are tasked with finding a valid discrete state vector $\vec{x} = (x_1, x_2, \dots, x_m)$ for a system of $n$ components and $m$ directional dependencies. Each dependency $j$ from component $u$ to component $v$ has an integer upper bound $C_j$, meaning its assigned state $x_j$ must be chosen from the finite domain $\{0, 1, \dots, C_j\}$. The Cartesian product of these domains defines a massive combinatorial search space of size $\prod_{j=1}^m (C_j + 1)$.

A state vector is valid if and only if it satisfies a strict system of linear equations across the components. For any component $i$, let $I_i$ be the sum of the variables $x_j$ for all dependencies directed into $i$, and $O_i$ be the sum of the variables $x_j$ for all dependencies directed out of $i$. The system requires $I_i = O_i$ for all components, except for a specified starting component $s$ and terminating component $t$. For these two components, a boundary condition dictates that the system must instead satisfy $O_s - I_s = d$ and $I_t - O_t = d$, where $d$ is a required integer target.

Your objective is to determine if there exists at least one satisfying assignment $\vec{x}$ in the state space that fulfills all equations simultaneously. If such an assignment exists, you must output it. 

## Input
Line 1: Three integers $n$, $m$, and $1$ (representing the number of components, dependencies, and active boundary conditions).
Line 2: Three integers $s$, $t$, and $d$ (the starting component, terminating component, and the required target).
Next $m$ lines: Three integers $u$, $v$, and $C_j$, representing a dependency from component $u$ to component $v$ with domain upper bound $C_j$.

## Output
If a satisfying state vector exists, output `YES` on the first line, followed by a second line containing $m$ integers representing the assigned values $x_1, x_2, \dots, x_m$ in the exact order the dependencies were provided in the input. If no such assignment exists, output `NO`.

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
