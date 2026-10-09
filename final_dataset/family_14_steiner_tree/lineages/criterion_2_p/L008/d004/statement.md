# Phase 2: Signal Convergence

Time limit: 2 s   Memory limit: 256 MB

## Description

A neuro-computational core consists of $R$ nodes (numbered 1 to $R$). There are $S$ available bidirectional links between these nodes.

During a diagnostic test, $P$ specific nodes are injected with a trace signal. 

You must activate a subset of the available links. The chosen subset must allow all $P$ trace signals to eventually converge at a single common node. The signals can travel any distance and in any direction, but they can only move across links that you have activated. They may converge at any node in the core (it does not have to be one of the injected nodes).

Each link has an activation cost. The total activation cost of your chosen subset is the sum of the activation costs of the distinct links included in that subset. Find the minimum possible total activation cost to allow this convergence.

## Input

The first line contains three integers $R$, $S$, and $P$. The total number of nodes $R$ is constrained by the core's maximum capacity of $200,000$. $S$ is always exactly $R - 1$. The number of injected nodes $P$ is at least $1$ and at most $R$.
The second line contains $P$ distinct integers: the identifiers of the injected nodes.
Each of the next $S$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le R$, $u \neq v$). This represents a bidirectional link between node $u$ and node $v$ with an activation cost $w$ (where $1 \le w \le 1,000,000$). 
The links provided in the input are guaranteed to connect all $R$ nodes with zero redundancy: activating all links allows a signal to pass between any two nodes in the core, but if any single link were permanently removed, it would be impossible to route signals between certain pairs of nodes.

## Output

Print a single integer: the minimum total activation cost of the chosen subset of links.

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