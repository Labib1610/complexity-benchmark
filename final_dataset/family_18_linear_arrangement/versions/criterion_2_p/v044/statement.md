# Backbone Trenching for a Reporting System

Time limit: 5 s
Memory limit: 256 MB

## Description
A monitoring installation requires $n$ unique modules to be assigned to $n$ mounting slots. These slots are arranged strictly in a single straight row and are numbered sequentially from $1$ to $n$. Each slot will hold exactly one module. The configuration space consists of all $n!$ possible bijective mappings between the modules and the slots.

The modules must communicate using a set of $m$ predefined data links. Each link connects a specific pair of modules. When a link joins a module placed in slot $x$ to a module placed in slot $y$, it requires a physical cable of length exactly $|x - y|$. Multiple cables can run parallel to each other along the row of slots without penalty. You are provided with a total cable budget $B$, representing the maximum allowable sum of the lengths of all $m$ cables combined.

To ensure the system functions correctly, the communication architecture guarantees that a message can travel between any two modules. Furthermore, to prevent signal feedback loops, the architecture strictly ensures there are no redundant links: starting from any module, there is exactly one sequence of links you can follow to reach any other module without traversing the same link twice. Consequently, the number of links $m$ is always exactly $n - 1$.

Your task is to evaluate the configuration space of module assignments to determine if there exists a permutation of the $n$ modules into the $n$ slots such that the total length of all physical cables is at most $B$. If no such assignment is possible, report that the budget cannot be met.

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
