# Operational Shift Assignment Stage

Time limit: 2 s   Memory limit: 256 MB

As part of an automated workforce deployment pipeline, an enterprise manages duty schedules through a multi-stage workflow:
1. **Data Ingestion**: Registering personnel records and compiling records of concurrent duty restrictions.
2. **Shift Partitioning**: Distributing all $n$ personnel across three distinct operational windows (labeled 1, 2, and 3) such that no restricted pair shares the same window.
3. **Resource Allocation**: Provisioning equipment for each finalized window roster.

Your program is responsible solely for Stage 2. Given the output of Stage 1—consisting of $n$ personnel (indexed 1 to $n$) and $m$ pairwise restriction rules—you must compute a valid window assignment for every individual or report that no valid configuration exists.

To ensure consistent downstream processing in Stage 3, if multiple valid window rosters exist, you must produce the one that is lexicographically smallest (comparing the assigned window of person 1 first, then person 2, and so on).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of personnel and the number of pairwise restrictions.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that person $u$ and person $v$ cannot be assigned to the same operational window.

## Output
If no valid assignment exists, print a single line `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the assigned operational window for person $i$. If there are multiple valid assignments, output the one that is lexicographically smallest.

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
