# Problem A — System Stabilization

Time limit: 2 s   Memory limit: 256 MB

A diagnostic system consists of $n$ processing modules. Each module must be programmed with a state value chosen from $\{1, 2, 3\}$.

The system contains $m$ bidirectional monitoring links, each connecting a specific pair of modules. A monitoring link actively transmits an error flag if and only if the two modules it connects are programmed with the exact same state value. To achieve system stability, every module must be assigned a state value such that absolutely no error flags are transmitted across any link.

Determine whether a stable configuration exists. If it does, find the valid assignment of state values that is lexicographically smallest when listed from module 1 to module $n$.

## Input
The first line provides two integers $n$ and $m$ — the number of modules and the number of monitoring links ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, specifying a monitoring link between module $u$ and module $v$.

## Output
If no stable configuration is possible, print a single line containing `NO`.
If a stable configuration exists, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each $s_i \in \{1, 2, 3\}$), representing the state value of each module $i$. If there are multiple stable configurations, output the one that is lexicographically smallest.

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
