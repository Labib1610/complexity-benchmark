# Problem B — System Mode Allocation

Time limit: 1 s   Memory limit: 256 MB

A system contains $n$ numbered units, labeled from $1$ to $n$. Each unit must be configured into one of two operational states, labeled $1$ or $2$.

Because there are $2^n$ total ways to set the states across all units, finding a viable configuration requires satisfying $m$ mutual interference conditions. Each condition lists two units that are forbidden from sharing the same operational state; that is, if one unit is set to state $1$, the other must be set to state $2$, and vice versa.

Determine if there exists a valid assignment of states to all $n$ units such that no interference condition is violated. If one or more valid assignments exist, output the one that produces the lexicographically smallest sequence of state values $(s_1, s_2, \dots, s_n)$. Otherwise, indicate that no valid assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that units $u$ and $v$ cannot be assigned the same operational state.

## Output
If no valid state assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ (where each $s_i \in \{1, 2\}$) representing the lexicographically smallest valid assignment.

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
