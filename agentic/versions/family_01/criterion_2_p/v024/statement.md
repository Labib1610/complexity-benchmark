# Frequency Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

A telecommunications operator manages $n$ signal relay units, indexed from $1$ to $n$. The operator has cataloged $m$ operational interference rules; each rule specifies a pair of units that are located too close together and will cause signal corruption if operated on the same frequency channel.

Only two operational channels are available, designated as channel $1$ and channel $2$. Every relay unit must be assigned exactly one channel such that no pair of units subject to an interference rule shares the same channel.

If it is impossible to assign channels to all units without violating any interference constraints, report that no valid configuration exists. If valid channel assignments exist, the operator requires the configuration that yields the lexicographically smallest sequence of channel choices $s_1, s_2, \dots, s_n$. A sequence $A = (a_1, \dots, a_n)$ is lexicographically smaller than sequence $B = (b_1, \dots, b_n)$ if at the first position $i$ where $a_i \neq b_i$, $a_i < b_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of signal relay units and the number of interference rules.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that relay unit $u$ and relay unit $v$ interfere with each other.

## Output
If no valid channel assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid channel assignment.

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
