# Problem B — Team Partitioning

Time limit: 1 s   Memory limit: 256 MB

A research facility needs to divide $n$ researchers, numbered 1 through $n$, into two distinct groups, labeled 1 and 2. Certain pairs of researchers cannot work in the same group due to equipment interference. You are given $m$ such incompatible pairs.

Assign every researcher to group 1 or group 2 such that no two researchers in an incompatible pair belong to the same group, or report if no such assignment exists. If multiple valid assignments exist, output the one that produces the lexicographically smallest sequence of group labels $(s_1, s_2, \dots, s_n)$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing an incompatible pair of researchers.

## Output
If no valid group assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid group assignment.

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
