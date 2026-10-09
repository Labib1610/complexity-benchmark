# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory administration is planning the shift schedule for $n$ employees. Each employee must be assigned a state of either shift 1 or shift 2, resulting in a massive state space of $2^n$ potential overall schedules. The administration must evaluate this space to find a configuration that complies with a provided list of $m$ strict operational constraints.

Each of the $m$ constraints specifies two employees. To prevent resource contention, any valid schedule must be configured such that the two employees mentioned in a constraint never share the same shift state. 

You need to determine whether any of the $2^n$ possible schedules satisfy all $m$ constraints simultaneously. If at least one valid schedule exists, you must output the lexicographically smallest valid schedule. If the entire state space contains no valid schedule, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a constraint between employee $u$ and employee $v$.

## Output
If no schedule among the $2^n$ possibilities satisfies all constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid schedule.

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
