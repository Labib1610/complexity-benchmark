# Problem A — Factory Roster Optimization

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates continuous production across three distinct time slots, labeled $1$, $2$, and $3$. The plant employs $n$ individual operators, identified by integer IDs from $1$ to $n$. Certain pairs of operators have documented schedule incompatibilities and cannot be assigned to the same time slot.

Your goal is to determine whether it is possible to assign every operator to exactly one time slot such that all of the following conditions are met:
1. Every operator $i \in \{1, \dots, n\}$ is assigned to precisely one slot $s_i \in \{1, 2, 3\}$.
2. For every recorded incompatibility between operator $u$ and operator $v$, their assigned slots must differ ($s_u \neq s_v$).
3. The sum of operator counts assigned across all three time slots equals $n$.
4. Any pair of operators without a recorded incompatibility may be placed either in the same time slot or in different time slots, provided condition 2 is nowhere violated.

If one or more valid roster configurations exist, select the configuration that is lexicographically smallest. That is, prioritize minimizing $s_1$; if there are ties, prioritize minimizing $s_2$, and so on up to $s_n$. If no configuration satisfies all constraints, indicate that scheduling is impossible.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), indicating the total number of operators and the number of incompatible pairs, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing an incompatibility between operator $u$ and operator $v$. No incompatible pair appears more than once in the input.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$, where $s_i \in \{1, 2, 3\}$ denotes the time slot assigned to operator $i$, forming the lexicographically smallest valid assignment.

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
