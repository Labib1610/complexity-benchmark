# Hardware Bus Allocation Optimization

Time limit: 1 s   Memory limit: 256 MB

A high-performance computing system consists of $n$ processing modules, numbered $1$ through $n$. Each module must be assigned to operate on one of two independent data buses, designated as Bus 1 or Bus 2.

There are $m$ hardware conflict constraints. Each constraint specifies a pair of modules that share a direct high-speed interconnect and therefore cannot be assigned to the same data bus under any circumstances.

Determine whether it is possible to assign every processing module to either Bus 1 or Bus 2 such that all $m$ conflict constraints are simultaneously satisfied.

If one or more valid bus assignments exist, output the assignment that is lexicographically smallest. Comparing two sequences of bus assignments $(s_1, s_2, \dots, s_n)$ and $(t_1, t_2, \dots, t_n)$, sequence $s$ is smaller than sequence $t$ if at the first position $i$ where $s_i \neq t_i$, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of modules and the number of pairwise conflict constraints, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$), indicating that module $u$ and module $v$ cannot be assigned to the same bus.

## Output
If no valid bus assignment exists that satisfies all constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid configuration.

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
