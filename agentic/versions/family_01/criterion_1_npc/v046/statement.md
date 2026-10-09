# Problem A — Plant Roster Allocation

Time limit: 2 s   Memory limit: 256 MB

A continuous-process chemical plant divides its 24-hour operation into three distinct time blocks: Morning (1), Swing (2), and Night (3). The facility employs $n$ technicians, and each technician must be assigned to exactly one of these time blocks. 

The plant's incident database flags specific pairs of technicians who cannot work together due to previous safety incidents. A roster is only valid if no two flagged technicians are assigned to the same time block. 

Your task is to generate a valid roster for the facility or determine that no such roster is possible.

## Input
The first line contains two integers $n$ and $m$ — the number of technicians and the number of flagged pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of flagged technicians.

## Output
If no valid roster can be formed, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the time block assigned to technician $i$. Any valid roster is accepted.

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
