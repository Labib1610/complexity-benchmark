# Problem B — Module Allocation

Time limit: 1 s   Memory limit: 256 MB

A software architecture consists of $n$ interacting modules. These modules must be distributed across the available execution environments. The environments designated for this deployment are identified by the numeric values 1 and 2. Every module must be allocated to exactly one of these environments.

During testing, it was observed that certain pairs of modules cause mutual interference. You are provided with $m$ interference logs. If two modules are listed together in a single log, they must be allocated to distinct environments to prevent failure. 

Additionally, the system guarantees the following structural properties: no single module is listed in more than $m$ interference logs, and any valid allocation will assign at most $n$ modules to environment 1.

Your task is to determine if a valid allocation exists. If multiple valid allocations exist, you must choose the one that minimizes the environment identifier assigned to module 1. If there are still multiple valid allocations, choose the one that minimizes the environment identifier for module 2, and so forth, sequentially up to module $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an interference log.

## Output
If it is impossible to distribute the modules according to the rules, output a single line NO.
Otherwise, output YES on the first line, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the allocation that satisfies the tie-breaking rule described above.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
