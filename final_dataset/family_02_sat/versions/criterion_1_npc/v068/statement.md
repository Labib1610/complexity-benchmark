# Problem A — Network Stabilization

Time limit: 2 s   Memory limit: 256 MB

## Description

A fluid distribution network is regulated by $n$ treatment facilities. Each facility must be locked into one of two operational states: dispensing an alkaline agent (denoted by `1`) or an acidic agent (denoted by `0`). 

The structural integrity of the network is monitored by $m$ remote checkpoints. Each checkpoint is programmed with exactly three condition checks. A condition check is represented by a non-zero integer $v$. The absolute value $|v|$ identifies a specific facility. The sign of $v$ indicates the required state for that facility: positive means it must dispense the alkaline agent (`1`), and negative means it must dispense the acidic agent (`0`).

A checkpoint registers a critical failure if and only if the network's configuration violates all three of its condition checks simultaneously. As long as a minimum of one condition check per checkpoint aligns with the actual facility states, the network remains stable. Note that a single checkpoint might check the same facility multiple times.

Determine whether there exists a global configuration for all $n$ facilities that keeps every single checkpoint stable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero integers $l_1, l_2, l_3$, with $|l_i| \le n$. These represent the three condition checks for a single checkpoint.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each `0` or `1`), where $s_i$ is the state of facility $i$. Any valid configuration is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```
