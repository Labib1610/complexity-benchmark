# Facility Shift Allocation

Time limit: 1 s   Memory limit: 256 MB

A laboratory needs to assign $n$ personnel members, identified by integers from $1$ to $n$, to one of two operational modes: Mode 1 or Mode 2.

Certain pairs of personnel experience signal interference if placed in the same operational mode. You are given a list of $m$ such mutually exclusive pairs.

Determine whether it is possible to assign every person to either Mode 1 or Mode 2 such that no two personnel in a mutually exclusive pair share the same mode. If a valid assignment exists, find the sequence of mode selections $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest. If no valid assignment exists, report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of personnel and the number of interference constraints, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that personnel member $u$ and personnel member $v$ cannot be assigned to the same mode.

## Output
If no valid mode assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
