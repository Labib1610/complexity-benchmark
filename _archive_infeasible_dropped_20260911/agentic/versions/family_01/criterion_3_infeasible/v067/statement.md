# Problem C — Safety Audit Report

Time limit: 2 s
Memory limit: 256 MB

A manufacturing facility operates on a standard two-shift rotation. Safety regulations mandate that certain pairs of operators cannot be assigned to the same shift due to overlapping equipment authorizations. The submitted workforce roster cannot be divided into two shifts without violating these regulations. To file an incident report, you must isolate a trio of operators where each operator shares an equipment authorization overlap with the other two. This structural failure guarantees that a two-shift division is impossible. Your task is to analyze the overlap logs and identify this trio. If multiple such trios exist, the report must list the one whose operators have the lowest employee ID numbers. You must prioritize minimizing the lowest ID in the trio, then the second-lowest ID, and finally the highest ID. The logs are guaranteed to contain at least one such trio.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the total number of operators and the number of overlapping equipment authorizations, respectively. Operators are identified by integers from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that operator $u$ and operator $v$ share an equipment authorization overlap.

It is guaranteed that at least one trio of operators, where all three share overlaps with each other, exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These integers must represent the IDs of the trio of operators. The output must be the group that satisfies the incident report's ID minimization rules.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
