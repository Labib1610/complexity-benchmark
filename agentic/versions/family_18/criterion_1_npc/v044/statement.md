# Problem A — Pipeline Stage Alignment

Time limit: 5 s
Memory limit: 256 MB

## Description
A decentralized smart contract utilizes a linear execution pipeline. The contract consists of $n$ distinct state variables, labeled $1$ through $n$, which must be assigned to $n$ sequentially numbered pipeline stages (from $1$ to $n$). Every variable must be assigned to exactly one stage, and every stage must hold exactly one variable.

The lexical analyzer has extracted $m$ data dependencies. Each dependency dictates that two specific variables must exchange data during execution. 

Because the pipeline is perfectly 1-dimensional and the stages are uniformly spaced, the routing delay between any two interacting variables placed at stage $x$ and stage $y$ is governed by the L1 distance, exactly $|x - y|$. The total routing delay of the contract is the sum of these L1 distances across all $m$ dependencies. 

The deployment engine enforces a strict total delay budget of $B$. Because the cost metric is a simple absolute difference on a 1D grid, the layout is highly regular. Strategies such as placing variables with the highest number of dependencies near the median position, or sorting them by their interaction frequency, are often considered to minimize the total sum. 

Your module must process the given dependencies and determine if there is any valid assignment of variables to stages that keeps the total routing delay at or below $B$. If such an assignment exists, you must output it so the compilation can proceed. Otherwise, you must halt the pipeline by reporting a failure.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, representing a data dependency between variable $u$ and variable $v$.

## Output
If there is an assignment of variables to stages $1$ through $n$ such that the total routing delay is at most $B$, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer is the stage (from $1$ to $n$) assigned to variable $i$. If multiple valid assignments exist, any sequence that satisfies the budget is acceptable.
Otherwise, print `NO`.

## Example
### Input
```
5 4 4
1 3
3 5
5 2
2 4
```

### Output
```
YES
1 4 2 5 3
```
