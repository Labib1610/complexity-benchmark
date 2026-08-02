# Operational Mode Assignment

Time limit: 1 s   Memory limit: 256 MB

A processing center consists of $n$ modules, numbered from $1$ to $n$, alongside $m$ conflict conditions specified between pairs of modules. Every module must be assigned to run under either Mode 1 or Mode 2. A conflict condition involving two modules prohibits both of them from being configured in the same operational mode.

Determine if there exists an assignment of modes to all modules such that no conflict condition is violated. If multiple valid assignments exist, choose the one that minimizes the sequence of assigned modes $s_1, s_2, \dots, s_n$ lexicographically, where $s_i \in \{1, 2\}$ denotes the mode assigned to module $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of modules and the number of conflict conditions.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a conflict condition between module $u$ and module $v$.

## Output
If no valid mode assignment exists, print `NO` on a single line.
Otherwise, print `YES` on the first line, and print $n$ space-separated integers $s_1, s_2, \dots, s_n$ on the second line ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid mode assignment.

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
