# Personnel Sector Allocation

Time limit: 1 s   Memory limit: 256 MB

A facility manages a workforce of $n$ individuals, indexed from $1$ to $n$. To maintain smooth operations, every individual must be assigned to work in one of two available facility zones, identified as Zone 1 and Zone 2.

Certain pairs of workers are known to have severe operational friction. For safety and productivity, two individuals who form a friction pair cannot be assigned to the same zone.

Your task is to determine whether a valid assignment of all $n$ workers to these two zones exists. If it is possible, output the assignment that produces the lexicographically smallest sequence of zone choices $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2\}$ denotes the zone assigned to individual $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of workers and the number of friction pairs, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that worker $u$ and worker $v$ cannot be assigned to the same zone.

## Output
If no valid zone assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid zone assignment.

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
