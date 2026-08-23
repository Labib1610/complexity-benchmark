# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory administration must assign each of its $n$ workers to one of two operational shifts, labeled 1 and 2. A complete schedule can be represented as a sequence of $n$ shift choices, meaning there are $2^n$ possible configurations to consider for the upcoming week.

However, a configuration is only valid if it satisfies a set of $m$ strict separation constraints. Each constraint specifies two workers who have a history of disputes; a valid configuration must never place both workers in the same shift.

Your objective is to search this space to find a valid configuration. Because there may be multiple such configurations, the administration requires the optimal one—specifically, the valid configuration that is lexicographically smallest when written as a sequence of $n$ shift labels. If the constraint system is so restrictive that absolutely no valid configuration exists in the entire $2^n$ space, you must report this impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of workers and the number of separation constraints, respectively. 
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) — a pair of workers who cannot share the same shift.

## Output
If no valid configuration exists among all possibilities, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1,2\}$), representing the lexicographically smallest valid configuration.

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
