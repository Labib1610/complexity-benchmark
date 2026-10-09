# Problem A — Linker Module: Address Assignment

Time limit: 5 s
Memory limit: 256 MB

## Description
The compilation of a decentralized smart contract involves a four-stage pipeline: Lexical Analysis, Address Generation, Jump Optimization, and Deployment. You are responsible for implementing the Address Generation stage.

In the first stage, the Lexical Analyzer identifies $n$ distinct state variables (labeled $1$ through $n$) and extracts $m$ data dependencies between them. Each dependency indicates that two specific variables interact during execution. 

Your module (Stage 2) receives this parsed data and must assign each of the $n$ variables to a distinct memory sector. The available memory sectors are numbered sequentially from $1$ to $n$. Every variable must be placed in exactly one sector, and every sector must contain exactly one variable. 

In Stage 3, the Jump Optimizer calculates the routing overhead. The protocol dictates that the routing cost between any two interacting variables is strictly the absolute difference between their assigned memory sector numbers. The total routing overhead for the contract is the sum of these costs across all $m$ dependencies identified in Stage 1. 

Finally, in Stage 4, the Deployment Engine will reject the contract if the total routing overhead exceeds a strict protocol budget $B$. 

Your task is to determine if there is a valid sector assignment for the variables that allows the contract to pass Stage 4. If such an assignment exists, you must provide it so the pipeline can proceed. Otherwise, you must halt the pipeline by reporting a failure.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, representing a data dependency between variable $u$ and variable $v$.

## Output
If a sector assignment exists that keeps the total routing overhead at or below $B$, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer is the memory sector (from $1$ to $n$) assigned to variable $i$. If multiple valid assignments exist, any sequence that satisfies the budget is acceptable.
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
