# Automated Line Allocation

Time limit: 1 s   Memory limit: 256 MB

A logistics facility processes $n$ items, indexed $1$ through $n$, using two independent processing lines labeled 1 and 2. Due to physical constraints, certain pairs of items interfere with each other and cannot be routed onto the same processing line. You are given $m$ such mutually incompatible pairs.

Determine whether every item can be assigned to line 1 or line 2 so that no incompatible pair shares the same processing line. If a valid assignment exists, output the lexicographically smallest assignment $s_1, s_2, \dots, s_n$ where each $s_i \in \{1, 2\}$. Otherwise, report that no assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), denoting an incompatible pair of items.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid line assignment.

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
