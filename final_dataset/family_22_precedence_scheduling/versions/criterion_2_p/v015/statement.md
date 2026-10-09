# Problem B — Migration Deployment Sequence

Time limit: 2 s
Memory limit: 256 MB

## Description
You are configuring a deployment pipeline for $n$ database migration scripts. Because the deployment uses a single database connection, the scripts must execute strictly one at a time in a linear sequence. 

Certain scripts rely on schema changes introduced by others, meaning a script cannot execute until all the scripts it relies on have already executed. You are given $m$ reliance rules, each dictating that a specific script must execute before another specific script. 

You must determine a complete execution sequence of all $n$ scripts that honors every reliance rule. If the rules contradict one another, no such sequence exists.

## Input
The first line contains two integers $n$ and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that script $a$ must execute before script $b$.

## Output
Print `YES` followed by a space-separated permutation of the integers $1$ to $n$ representing a valid execution sequence. If no such sequence is possible, print `NO`.

## Example

### Input
```
4 5
1 2
1 3
2 4
3 4
1 4
```

### Output
```
YES
1 2 3 4
```
