# Problem B — Backbone Trenching for a Reporting System

Time limit: 5 s
Memory limit: 256 MB

## Description
A monitoring installation requires $n$ modules to be installed into $n$ mounting slots arranged in a single straight row. The slots are numbered sequentially from $1$ to $n$. Each slot will hold exactly one module.

The modules must be wired together using $m$ data links, where each link joins a specific pair of modules. The links are designed such that a message can travel between any two modules in the system. However, to prevent feedback, there are no redundant links: starting from any module, there is exactly one sequence of links you can follow to reach any other module without traversing the same link twice. Because of this design, the number of links $m$ is always exactly $n - 1$.

When a link joins a module in slot $x$ to a module in slot $y$, it requires a physical cable of length $|x - y|$. You are given a total cable budget $B$, which is the maximum allowable sum of the lengths of all $m$ cables combined. Multiple cables can run parallel to each other along the row of slots without penalty.

Determine an assignment of the $n$ modules to the $n$ slots such that the total length of all cables is at most $B$. If no such assignment is possible, report that the budget cannot be met.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a data link between module $u$ and module $v$.

## Output
If the budget can be met, print `YES` on the first line. On the second line, print $n$ integers representing the slot numbers (from $1$ to $n$, forming a permutation) where modules $1, 2, \dots, n$ are installed, respectively.
If the budget cannot be met, print `NO`.

## Example
**Input**
```text
4 3 4
1 2
1 3
1 4
```

**Output**
```text
YES
2 1 3 4
```
