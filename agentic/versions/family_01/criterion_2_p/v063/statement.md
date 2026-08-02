# Frequency Channel Assignment

Time limit: 1 s   Memory limit: 256 MB

A wireless communications system manages $n$ signal units numbered $1$ through $n$. There are $m$ recorded operational restrictions. Each restriction identifies a specific pair of units that are located near each other and must not be configured to use the same frequency setting.

Only two frequency settings are available, labeled $1$ and $2$. Every signal unit must be assigned exactly one frequency setting ($1$ or $2$) such that for every operational restriction, the two units in that restriction receive different settings.

Your task is to decide whether a valid assignment exists for all $n$ units. If no assignment satisfies all restrictions, report that no valid configuration exists. If one or more valid configurations exist, choose the configuration that forms the lexicographically smallest sequence of settings $s_1, s_2, \dots, s_n$.

A sequence $A = (a_1, a_2, \dots, a_n)$ is lexicographically smaller than sequence $B = (b_1, b_2, \dots, b_n)$ if at the smallest position $i$ ($1 \le i \le n$) where $a_i \neq b_i$, $a_i < b_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of signal units and the number of operational restrictions.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), specifying that unit $u$ and unit $v$ cannot share the same frequency setting.

## Output
If no valid setting assignment exists, print a single line containing `NO`.
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
