# Workforce Pipeline: Shift Allocation Stage

Time limit: 2 s   Memory limit: 256 MB

A corporate personnel management engine coordinates shift assignments for employees across three designated daily time slots, denoted by integer codes 1, 2, and 3.

You are given $n$ workers, identified by integer IDs from 1 to $n$, and a list of $m$ pairwise operational incompatibility constraints. An incompatibility between worker $u$ and worker $v$ means they cannot be active during the same operational shift.

To validate compliance, the system evaluates assigned shift codes $s_1, s_2, \dots, s_n$ against two compliance criteria:
1. Every worker $i$ must receive an integer shift code $s_i \in \{1, 2, 3\}$.
2. For each incompatible pair of workers $(u, v)$, the product of their assigned shift codes $s_u \cdot s_v$ must belong to the permitted product set \{2, 3, 6\}.

If one or more valid shift assignments exist, you must output the one that is lexicographically smallest when viewed as the sequence $(s_1, s_2, \dots, s_n)$. If no assignment satisfies all conditions, report that allocation is impossible.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of workers and the number of incompatible pairs.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating an operational incompatibility between worker $u$ and worker $v$.

## Output
If no valid shift assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the shift assigned to each worker $1 \dots n$. Output the lexicographically smallest sequence among all valid assignments.

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
