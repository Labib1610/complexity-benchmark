# Problem A — Operational Segments

Time limit: 2 s
Memory limit: 256 MB

A factory divides its daily operations into work segments. Each of its $n$ workers must be allocated to exactly one work segment. The available segments are identified by the codes 1, 2, and 3.

Due to equipment limitations, certain pairs of workers have mutual interference. If two workers have mutual interference, they are prohibited from being allocated to the same work segment.

Determine an allocation of work segments for all $n$ workers such that no two interfering workers share a segment. If no such allocation is possible, report that it cannot be achieved.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of workers that have mutual interference.

## Output
If no valid allocation can be found, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each chosen from the values 1, 2, or 3), where $s_i$ represents the work segment allocated to worker $i$. Any valid allocation will be accepted.

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
