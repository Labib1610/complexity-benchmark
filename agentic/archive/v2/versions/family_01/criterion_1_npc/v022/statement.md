# Hardware Bus Allocation

Time limit: 2 s   Memory limit: 256 MB

A high-frequency compute system distributes processing tasks across $n$ active computing cores, indexed from $1$ to $n$. Each core must be mapped to one of three isolated hardware buses, designated $1$, $2$, and $3$.

Due to shared memory channels, certain pairs of cores experience bus contention if assigned to the same bus. Thus, any pair of cores subject to contention must be assigned to different buses. 

Because lower bus indices are physically closer to the memory controller and yield lower latency, preference is given to lower-indexed bus assignments. If a valid configuration exists, you must find the one that produces the lexicographically smallest sequence of bus assignments $(s_1, s_2, \dots, s_n)$ (comparing $s_1$ first, then $s_2$, and so forth). Otherwise, report that no valid configuration is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of cores and the number of contention rules.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that core $u$ and core $v$ cannot share the same hardware bus.

## Output
If no valid bus assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the bus assigned to each core $i$, corresponding to the lexicographically smallest valid assignment.

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
