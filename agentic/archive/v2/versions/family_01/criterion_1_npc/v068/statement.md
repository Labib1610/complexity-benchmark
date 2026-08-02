# Signal Mode Allocation

Time limit: 2 s   Memory limit: 256 MB

A telecommunication system manages $n$ devices, indexed from $1$ to $n$. Every device must be configured to run in one of three available operating modes: mode $1$, mode $2$, or mode $3$.

Due to physical constraints, specified pairs of devices conflict with each other. If two devices conflict, they are forbidden from using the same operating mode.

Your task is to determine whether it is possible to assign an operating mode to every device such that no two conflicting devices share a mode. If a valid configuration exists, find the one that forms the lexicographically smallest sequence of assigned modes $s_1, s_2, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40, 0 \le m \le n(n-1)/2$) — the number of devices and the number of conflicting pairs, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ — indicating that device $u$ and device $v$ form a conflicting pair.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the operating mode assigned to device $i$. If there are multiple valid assignments, output the sequence that is lexicographically smallest.

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
