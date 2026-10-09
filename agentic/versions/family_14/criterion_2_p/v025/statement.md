# Resonance of the Core Monoliths

Time limit: 2 s
Memory limit: 256 MB

## Description

You are tasked with restoring a network of $n$ ancient monoliths, numbered $1$ to $n$. Certain pairs of monoliths can be linked by a resonance channel. Stabilizing a channel requires a specific amount of energy.

There are $t$ "core" monoliths that must be brought online. To function, all core monoliths must be able to communicate with each other. This communication can happen directly through a stabilized channel, or indirectly by routing through a sequence of stabilized channels (which may pass through non-core monoliths).

You are given the layout of the $m$ possible resonance channels. The network was built with the following architectural properties:
- The total number of possible channels $m$ is exactly $n - 1$.
- It is possible to route a signal between any two monoliths in the network using some sequence of channels.
- The maximum number of channels directly connected to any single monolith is at most $n - 1$.
- The total energy required to stabilize every single channel in the network combined is at most $2 \times 10^{11}$.

Find the minimum total energy required to stabilize a set of channels such that all $t$ core monoliths are interconnected.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200,000$, $m = n - 1$).
The second line contains $t$ distinct integers: the identifiers of the core monoliths.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \ne v$, $1 \le w \le 1,000,000$): a possible resonance channel between monoliths $u$ and $v$ requiring $w$ energy to stabilize.

## Output

Print a single integer: the minimum total energy needed to link all core monoliths.

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

## Note

In Example 1, the core monoliths 1 and 4 can only communicate by routing through monoliths 2 and 3. Therefore, all three channels must be stabilized, costing 5 + 1 + 2 = 8 energy. 
In Example 2, there is only one core monolith, so no channels need to be stabilized.
