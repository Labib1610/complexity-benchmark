# Problem B — Operational Windows

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility tracks a workforce of $n$ individuals, numbered 1 through $n$. The facility's safety protocols include a registry of $m$ incompatible pairs among the workforce. During a standard production cycle, exactly two operational windows are available, designated as window 1 and window 2. A roster configuration consists of a sequence of $n$ values, each being either 1 or 2, representing the assigned operational window for each respective individual. The safety guidelines mandate that for every pair recorded in the registry, the two individuals involved must correspond to different values in the roster configuration.

Your task is to construct such a roster configuration. If the safety guidelines cannot be satisfied under these conditions, you must report this failure. Should there be more than one configuration that meets all the mandates, you must output the sequence that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of personnel and the number of incompatible pairs.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that person $u$ and person $v$ are recorded in the registry as an incompatible pair.

## Output
If no roster configuration can satisfy the safety mandates, output a single line containing `NO`.
Otherwise, output a line containing `YES`. On the following line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the allocated window for each person. This sequence must be the lexicographically smallest among all valid configurations.

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
