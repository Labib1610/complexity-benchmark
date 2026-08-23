# Problem B — Facility Access

Time limit: 1 s
Memory limit: 256 MB

The facility administration must issue each of its $n$ workers an access code. Every worker must be assigned a code of either 1 or 2. 

A complete assignment is only valid if it satisfies $m$ safety requirements. Each requirement identifies two workers who operate interlinked machinery. To ensure proper load balancing, the sum of the access codes assigned to these two workers must equal exactly 3. 

Your objective is to determine a valid assignment for all $n$ workers. Because multiple valid assignments might exist, you must find the one that is lexicographically smallest when the assigned codes are listed in order from worker 1 to worker $n$. If it is impossible to satisfy all safety requirements simultaneously, you must report that no such assignment exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of workers and the number of safety requirements. 
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a pair of workers whose assigned access codes must sum to 3.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1,2\}$), representing the lexicographically smallest valid sequence of access codes.

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
