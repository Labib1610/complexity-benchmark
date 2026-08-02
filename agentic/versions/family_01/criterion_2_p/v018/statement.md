# Shift Allocation Schedule

Time limit: 1 s   Memory limit: 256 MB

There are $n$ individuals labeled from $1$ to $n$ and $m$ pairs of individuals who cannot work together. The work day is divided into two distinct operating blocks, labeled 1 and 2. Every individual must be assigned to perform their duties in exactly one block, subject to the condition that no incompatible pair works in the same block.

Your task is to determine whether it is possible to assign every individual to a block without violating any restriction. If possible, output the valid block sequence $s_1, s_2, \dots, s_n$ (where $s_i \in \{1, 2\}$) that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing an incompatible pair.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$ representing the lexicographically smallest valid assignment.

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
