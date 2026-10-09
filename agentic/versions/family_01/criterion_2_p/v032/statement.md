# Problem B — Workforce Scheduling

Time limit: 1 s
Memory limit: 256 MB

A manufacturing plant is organizing its workforce of $n$ employees into two distinct time slots, denoted as 1 and 2. Every employee must be allocated exactly one of these two slots. The space of all potential allocations is massive, totaling $2^n$ possible combinations.

However, the allocations are bounded by $m$ operational constraints. Each constraint specifies that two particular employees cannot be allocated the same time slot. 

Your task is to evaluate the $2^n$ potential allocations and determine if there exists at least one configuration that satisfies all $m$ constraints simultaneously. If no such configuration can be found among all possibilities, you must report this. If valid configurations do exist, you must identify the optimal one. An allocation is considered optimal if its sequence of time slots $s_1, s_2, \dots, s_n$ is the smallest possible in dictionary order (i.e., comparing the time slot of employee 1 first, then employee 2, and so on).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of employees and the number of operational constraints.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a constraint between employee $u$ and employee $v$.

## Output
If there is no valid allocation out of the $2^n$ combinations, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the optimal valid allocation.

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
