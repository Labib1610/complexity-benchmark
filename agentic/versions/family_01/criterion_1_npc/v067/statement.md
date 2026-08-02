# Shift Assignment Coordination

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ individuals, identified by integer labels from $1$ through $n$. Operations at the facility are divided into three distinct operational shifts, indexed as $1$, $2$, and $3$.

Certain pairs of individuals have mutual incompatibilities. A collection of $m$ distinct incompatibility conditions is given, where each condition specifies two individuals who cannot be scheduled in the same operational shift.

A valid schedule assigns each individual $i$ (for $1 \le i \le n$) to a single shift $s_i \in \{1, 2, 3\}$ such that no incompatibility condition is violated. The configuration of a schedule is represented by the sequence of choices $(s_1, s_2, \dots, s_n)$.

Your task is to determine whether a valid schedule exists. If one or more valid schedules exist, you must output the one that is lexicographically smallest. Otherwise, you must indicate that no valid schedule can be formed.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of individuals and the number of mutual exclusion restrictions, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a pair of individuals who cannot share the same operational shift.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 s_2 \dots s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the assigned operational shift for each individual from $1$ to $n$. Output the lexicographically smallest valid sequence if multiple valid assignments exist.

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
