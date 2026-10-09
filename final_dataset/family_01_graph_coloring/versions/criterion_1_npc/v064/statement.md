# Problem A — Security Ring Allocation

Time limit: 2 s   Memory limit: 256 MB

You are tasked with deploying $n$ background processes (numbered 1 through $n$) on a computing cluster. To execute, every process requires an assignment to one of three available security rings, denoted by the integers 1, 2, and 3.

The system's shared memory introduces $m$ concurrency restrictions. Each restriction is defined by a pair of processes that interact with the same memory region. To avoid data corruption, whenever two processes share a memory region, their assigned security rings must be distinct from one another.

Determine if a complete assignment of security rings exists that satisfies all concurrency restrictions.

## Input
The first line contains two integers $n$ and $m$ — the number of processes and the number of concurrency restrictions ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$, representing a pair of processes that share a memory region.

## Output
If there is no valid assignment, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ ($1 \le s_i \le 3$), where $s_i$ is the security ring assigned to process $i$. Any valid assignment is accepted.

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
