# Problem B — Operational Windows

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility must schedule a workforce of $n$ individuals, numbered 1 through $n$. A complete roster configuration requires making a discrete choice for every individual, creating a massive search space of potential schedules. Specifically, each person must be assigned an operational window, represented by an integer. Since the facility operates exactly two windows—designated 1 and 2—there are $2^n$ possible configuration sequences to consider.

To avoid production hazards, a configuration is only valid if it satisfies a strict system of $m$ separation constraints. The facility maintains a registry of incompatible pairs. For every pair $(u, v)$ recorded in this registry, any configuration where individual $u$ and individual $v$ are assigned the identical operational window is strictly prohibited. You must determine if there exists a sequence in the $2^n$ search space that satisfies all $m$ constraints simultaneously.

If the safety guidelines cannot be satisfied by any configuration, you must report this failure. Should multiple configurations meet all the mandates, you must output the sequence that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of personnel and the number of separation constraints.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that person $u$ and person $v$ are an incompatible pair.

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
