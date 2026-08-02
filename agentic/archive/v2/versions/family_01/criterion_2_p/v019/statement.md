# Relay Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

A network consists of $n$ relay devices numbered $1$ through $n$. Each device must be configured to operate on one of two available frequency bands, labeled $1$ and $2$.

There are $m$ mutual interference conditions. Each condition specifies a pair of devices that cannot be assigned the same frequency band.

Determine if there is a valid frequency configuration for all $n$ devices. If no such configuration exists, report this. If multiple valid configurations exist, choose the one that forms the lexicographically smallest sequence of frequencies $s_1, s_2, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of devices that must not share a frequency band.

## Output
If no valid frequency configuration exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid configuration.

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
