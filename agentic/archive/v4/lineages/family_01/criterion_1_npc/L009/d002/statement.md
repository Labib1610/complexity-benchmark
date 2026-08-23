# Parallel Track Routing Assignment

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility routes $n$ work items, numbered 1 through $n$, into three available processing lines labeled 1, 2, and 3. Every item $i$ must be assigned to exactly one line $s_i \in \{1, 2, 3\}$.

There are $m$ cross-talk constraints. Each constraint specifies a pair of distinct items $u$ and $v$. To prevent interference, any pair $(u, v)$ subject to a constraint must be assigned to different processing lines (that is, $s_u \neq s_v$).

Determine whether a valid assignment exists for all $n$ items satisfying all $m$ cross-talk constraints. If so, find the valid assignment that produces the lexicographically smallest sequence $s_1, s_2, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of items and the number of cross-talk constraints, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a cross-talk constraint between item $u$ and item $v$.

## Output
If no valid line assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line.
On the second line, print $n$ integers $s_1\ s_2\ \dots\ s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the assigned line for each item $i$.
If multiple valid assignments exist, output the lexicographically smallest sequence.

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