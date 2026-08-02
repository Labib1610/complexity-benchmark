# Workforce Scheduling Optimization: Phase 2

Time limit: 1 s   Memory limit: 256 MB

In a workforce management pipeline, $n$ personnel members must each be assigned to one of two operational duty periods, labeled 1 and 2. 

Certain pairs of personnel members have direct operational conflicts. A list of $m$ conflicting pairs is provided.

An assignment of duty periods $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) is considered valid if it satisfies the following rules:
1. Direct Conflict Rule: If personnel $u$ and personnel $v$ are specified as a conflicting pair, then $s_u \neq s_v$.
2. Cyclic Consistency Rule: For any sequence of personnel members $v_1, v_2, \dots, v_k$ ($k \ge 4$, $k$ is even) forming a closed loop of direct conflicts ($v_1$ conflicts with $v_2$, $v_2$ conflicts with $v_3$, \dots, and $v_k$ conflicts with $v_1$), the assigned duty periods along the loop must strictly alternate between 1 and 2 (meaning $s_{v_1} \neq s_{v_2}, s_{v_2} \neq s_{v_3}, \dots, s_{v_k} \neq s_{v_1}$).

If one or more valid assignments exist, select the assignment that is lexicographically smallest. That is, comparing sequence $s_1, s_2, \dots, s_n$ with another valid sequence $t_1, t_2, \dots, t_n$, select $s$ if at the first index $i$ where $s_i \neq t_i$, we have $s_i < t_i$.

If no valid assignment can satisfy all conditions, output `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) representing a conflicting pair of personnel members.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
