# Database Replication Consistency

Time limit: 1 s
Memory limit: 256 MB

## Description
A distributed system contains $n$ databases. Each database must be assigned exactly one replication setting: synchronous (represented by 1) or asynchronous (represented by 0).

The system continuously runs $m$ consistency checks. Each check evaluates a specific pair of database settings. A check will trigger a system-wide alert if and only if neither of its two evaluated settings is currently active in the system. 

Determine whether there is an overall assignment for all $n$ databases that triggers zero alerts.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of databases and the number of consistency checks.

Each of the next $m$ lines contains two non-zero integers $v_1$ and $v_2$ ($1 \le |v_i| \le n$). 
An integer $v_i > 0$ refers to the setting where database $v_i$ is synchronous. 
An integer $v_i < 0$ refers to the setting where database $|v_i|$ is asynchronous. 
Each line defines the two settings evaluated by a single consistency check.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (each in $\{0, 1\}$) forming any assignment that avoids all alerts, where $c_i$ is the setting of database $i$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid assignments may exist; any one is accepted. The same database may be evaluated by multiple checks, and a single check may evaluate the same database twice.
