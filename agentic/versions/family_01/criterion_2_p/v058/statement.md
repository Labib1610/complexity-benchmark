# Dual Frequency Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

In a radio network, $n$ transmitter units, numbered sequentially from $1$ to $n$, must each be assigned one of two available operational settings, labeled $1$ and $2$.

There are $m$ designated pairs of units that experience mutual interference. The operational rule requires that two units in any such pair must not be assigned the same operational setting.

Your goal is to determine whether a valid assignment of settings to all $n$ units exists under this rule. If at least one valid assignment exists, output `YES` followed by the setting sequence $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest. That is, if there are multiple valid sequences, select the one that minimizes $s_i$ at the smallest index $i$ where two valid sequences differ. If no valid assignment can satisfy the operational rule for every interference pair, output `NO`.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5, 0 \le m \le 2\cdot 10^5$), representing the number of units and the number of interfering pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that unit $u$ and unit $v$ interfere with each other.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment sequence.

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
