# Environment Allocation

Time limit: 2 s
Memory limit: 256 MB

A system administrator is trying to partition $n$ software modules (numbered 1 through $n$) into two isolated virtual environments. The system's compatibility registry contains $m$ records of module pairs. If both modules from a record are placed in the same environment, they will trigger a critical system panic.

The administrator needs to formally justify provisioning a third environment by demonstrating that a two-environment deployment is impossible. You must provide a minimal configuration that proves this: a collection of three distinct modules where the registry contains a conflict record for every combination of two modules drawn from this collection. Because of this mutual incompatibility, any attempt to divide these three modules between two environments will always force at least one recorded pair to share an environment.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, representing a pair of modules that cannot share an environment. 
It is guaranteed that the registry contains at least one such collection of three modules.

## Output
Output the three integer identifiers of your chosen collection on a single line, ordered from lowest to highest. 
If more than one such collection exists, evaluate them by their sorted identifiers. Choose the collection that minimizes the first (lowest) identifier. If there is a tie, choose the one that minimizes the second (middle) identifier. If a tie still remains, minimize the third (highest) identifier.

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```