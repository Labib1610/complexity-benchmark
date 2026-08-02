# Problem A — Schedule Partitioning

Time limit: 2 s   Memory limit: 256 MB

An organization manages $n$ personnel, indexed from 1 to $n$. Every person must be assigned to exactly one of three available operational windows, labeled 1, 2, and 3. Certain pairs of personnel are incompatible and cannot be assigned to the same operational window.

Your task is to assign every person to an operational window such that no incompatible pair shares the same window, or report that no valid assignment is possible.

## Input
The first line contains two integers $n$ and $m$ — the number of personnel and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing an incompatible pair of personnel.

## Output
If no valid assignment exists, print a single line `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the assigned operational window for person $i$. If there are multiple valid assignments, output the one that is lexicographically smallest (comparing $s_1$ first, then $s_2$, and so on).

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
