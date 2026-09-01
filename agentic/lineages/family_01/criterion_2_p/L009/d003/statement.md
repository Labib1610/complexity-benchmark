# Problem B — Signal Balancing

Time limit: 1 s
Memory limit: 256 MB

You are configuring $n$ signal transmitters. Each transmitter must be assigned a power level of either 1 or 2.

The network contains $m$ receivers. Each receiver listens to exactly two specific transmitters. To decode the transmission correctly, each receiver must detect a combined total power level of exactly 3 from the two transmitters it listens to. 

You must assign a power level to each of the $n$ transmitters so that all $m$ receivers detect a combined power level of exactly 3. If no such configuration is possible, you must report it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two transmitters that a single receiver listens to.

## Output
If no valid power level assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $p_1, \dots, p_n$ (each $p_i \in \{1, 2\}$), where $p_i$ is the power level assigned to transmitter $i$. If there are multiple valid assignments, output the one that is lexicographically smallest.

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