# Environment Allocation

Time limit: 2 s
Memory limit: 256 MB

A system administrator is trying to deploy $n$ software modules (numbered 1 through $n$) across two isolated virtual environments. The system's compatibility registry contains $m$ records of module pairs that will cause a critical system panic if installed in the same environment.

The administrator suspects it is impossible to deploy all modules using only two environments. To formally justify the creation of a third environment, you must output a minimal proof of this impossibility. You need to find a set of three distinct modules such that every possible pair among these three is registered as a conflict. This exact configuration ensures that no matter how you distribute these three modules across two environments, at least one conflicting pair will end up together.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of modules that conflict with each other. 
It is guaranteed that at least one such configuration of three modules exists.

## Output
Print the three integer identifiers of these modules on one line, sorted in ascending order. 
If there are multiple valid configurations, output the one that is lexicographically smallest (smallest first integer; resolving ties by the second integer, then the third).

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