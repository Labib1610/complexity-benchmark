# Problem B — System State Validation

Time limit: 2 s   Memory limit: 256 MB

## Description
A large-scale infrastructure consists of $2q$ distinct nodes, labeled sequentially from $1$ to $2q$. 

You are provided with a registry of $t$ candidate operational modules. Your task is to explore the configuration space of these modules to identify a valid activation state. Because any subset of the $t$ modules could theoretically be activated, there are $2^t$ possible configurations to evaluate. 

A configuration is defined as a valid activation state if and only if it achieves an exact, non-overlapping partition of the infrastructure: every single node from $1$ to $2q$ must be incorporated into exactly one activated module. Leaving a node out is not permitted, and having a node participate in multiple activated modules will inevitably cause a system conflict. 

In this specific architecture, each candidate module connects exactly two nodes. Furthermore, every module in the registry pairs one node from the primary tier (labels $1 \dots q$) with one node from the secondary tier (labels $q+1 \dots 2q$). Unlisted node combinations are impossible to activate.

You must determine whether the configuration space contains at least one valid activation state. If a stable subset of modules exists that perfectly partitions all $2q$ nodes, you must output it. Otherwise, report that no such configuration is possible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$). The system has $2q$ nodes in total, and $t$ is the number of candidate modules in the registry.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting a candidate module that links node $a$ and node $b$.

## Output
If a valid activation state exists among the subsets, print `YES` on the first line. Then, output $q$ lines, each containing the two integers of an activated module from your chosen state. If no valid subset exists, print `NO`.

## Example

### Input
```
3 5
1 4
1 5
2 5
3 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```
