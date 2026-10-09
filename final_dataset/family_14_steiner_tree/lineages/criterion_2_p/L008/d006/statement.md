# Architectural Core Cluster

Time limit: 2 s   Memory limit: 256 MB

## Description

An industrial facility contains $R$ logic components, interconnected by $S$ bidirectional data integrations. 
A recent directive mandates that $P$ specific components must be isolated into a unified operational cluster.

You must select a subset of the $R$ components to form this cluster. The selected subset must satisfy:
1. It contains all $P$ of the mandated components (it may also contain any number of other components).
2. The selected components must be fully contiguous. That is, for any two components in the cluster, they must be able to communicate using only integrations that connect two components which are both in the cluster.

Whenever two components that share a physical integration are both selected for the cluster, that integration is "internalized" and requires a configuration cost. Integrations where at least one endpoint is not in the cluster remain external and cost nothing.

The facility's architecture ensures that information between any two components flows through exactly one unique sequence of integrations. Because of this exact uniqueness of communication pathways, minimizing the total configuration cost of the internalized integrations is identical to identifying the minimum-cost contiguous integration network encompassing the mandates.

Your objective is to determine the minimum possible total configuration cost to establish a valid operational cluster.

## Input

The first line contains three integers $R$, $S$, and $P$. 
The total number of components $R$ satisfies $1 \le R \le 200,000$. 
The number of integrations $S$ is exactly equal to $R - 1$. 
The number of mandated components $P$ satisfies $1 \le P \le R$.

The second line contains $P$ distinct integers: the identifiers of the mandated components.

Each of the following $S$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le R$, $u \neq v$). This indicates a bidirectional integration between component $u$ and component $v$ with a configuration cost of $w$ ($1 \le w \le 1,000,000$). 

## Output

Output a single integer representing the minimum total configuration cost of a valid component cluster.

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