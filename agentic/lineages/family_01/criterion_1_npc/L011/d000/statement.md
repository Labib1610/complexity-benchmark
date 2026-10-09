# Problem A — Production Cycle Allocation

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant requires continuous operation across three daily production cycles labeled 1, 2, and 3. The plant employs $n$ technicians. Due to documented interpersonal disputes that disrupt operations, specific pairs of technicians cannot be scheduled during the same production cycle. You must allocate every technician to exactly one of the three cycles such that no two disputing technicians work at the same time, or determine that this scheduling is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of technicians and the number of documented disputes ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of technicians who have a dispute.

## Output
If no valid allocation exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1\ s_2\ \dots\ s_n$ (each in $\{1,2,3\}$), where $s_i$ is the production cycle of technician $i$. Any valid allocation is accepted.

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
