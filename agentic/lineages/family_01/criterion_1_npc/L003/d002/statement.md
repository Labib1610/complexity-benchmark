# Facility Automation Control: Module Execution Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description
A central controller manages $n$ processing modules numbered from $1$ to $n$. Each module must be assigned to operate in one of three available execution phases, indexed as 1, 2, or 3.

Certain pairs of modules cause bus contention if they operate in the exact same execution phase simultaneously. You are given a list of $m$ pairs of mutually incompatible modules. An assignment of phases to modules is valid if no incompatible pair shares the same phase index.

To maintain system stability and deterministic startup order, the controller requires the lexicographically smallest sequence of assigned phases $s_1, s_2, \dots, s_n$. If it is impossible to assign phases 1, 2, or 3 to all modules without causing bus contention, the system cannot initialize.

Determine if a valid phase assignment exists. If so, output `YES` along with the lexicographically smallest phase sequence. Otherwise, report `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of modules and the number of contention constraints.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that module $u$ and module $v$ cannot share the same execution phase.

## Output
If no valid phase configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ where $s_i \in \{1, 2, 3\}$ represents the phase assigned to module $i$. If multiple valid assignments exist, output the one that is lexicographically smallest.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```