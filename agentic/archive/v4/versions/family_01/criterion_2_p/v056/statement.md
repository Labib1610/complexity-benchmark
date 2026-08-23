# Dual-Band Transceiver Configuration

Time limit: 1 s   Memory limit: 256 MB

A telecommunications facility manages $n$ transceiver units numbered $1$ through $n$. Each unit must be configured to operate on one of two available channel modes, designated as $1$ and $2$.

There are $m$ mutual interference conditions. Each condition specifies a pair of units that cannot operate on the same channel mode (that is, if one unit is set to mode $1$, the other must be set to mode $2$, and vice versa).

Determine if there exists a valid mode assignment for all $n$ units satisfying every interference condition. If no valid assignment exists, report this. If multiple valid assignments exist, choose the one that forms the lexicographically smallest sequence of assigned modes $s_1, s_2, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that transceiver $u$ and transceiver $v$ must be assigned distinct channel modes.

## Output
If no valid assignment of channel modes exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line.
On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of channel mode settings.

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
