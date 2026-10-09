# Phase 2: Signal Convergence

Time limit: 2 s   Memory limit: 256 MB

## Description

A neuro-computational core consists of $R$ nodes (numbered 1 to $R$). There are $S$ available bidirectional links between these nodes.

During a diagnostic test, $P$ specific nodes are injected with a trace signal. 

You must designate a subset of the $R$ nodes to form a contiguous processing zone. To be valid, this designated subset must satisfy two conditions:
1. It must include all $P$ of the injected nodes (it may also include any number of non-injected nodes).
2. The designated nodes must form a single connected component. This means that for any two nodes in your subset, it must be possible to travel between them using only available links that connect two designated nodes.

When you designate a subset of nodes, any available link that connects two designated nodes becomes "active". Links that connect a designated node to a non-designated node, or two non-designated nodes, remain inactive. 

Each link has a specific activation cost. The total cost of your designated processing zone is the sum of the activation costs of all active links. Find the minimum possible total cost to form a valid processing zone.

## Input

The first line contains three integers $R$, $S$, and $P$. 
The total number of nodes $R$ satisfies $1 \le R \le 200,000$. 
The number of links $S$ is exactly $R - 1$. 
The number of injected nodes $P$ satisfies $1 \le P \le R$.

The second line contains $P$ distinct integers: the identifiers of the injected nodes.

Each of the next $S$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le R$, $u \neq v$). This represents a bidirectional link between node $u$ and node $v$ with an activation cost $w$ ($1 \le w \le 1,000,000$). 

The links provided in the input are guaranteed to connect all $R$ nodes with zero redundancy: activating all links allows a signal to pass between any two nodes in the core, but if any single link were permanently removed, it would be impossible to route signals between certain pairs of nodes.

## Output

Print a single integer: the minimum total activation cost of a valid designated subset of nodes.

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