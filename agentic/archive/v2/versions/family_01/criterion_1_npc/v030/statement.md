# Operational Slot Allocation

Time limit: 2 s   Memory limit: 256 MB

A facility operates across three sequential time blocks designated as $1$, $2$, and $3$. There are $n$ individuals numbered from $1$ to $n$. A set of $m$ mutual exclusion restrictions is specified between pairs of individuals. If two individuals are linked by a restriction, they cannot be assigned to the same time block.

Every individual must be assigned to exactly one time block such that no mutual exclusion restriction is violated. If at least one valid assignment exists, you must find the one that yields the lexicographically smallest sequence $(s_1, s_2, \dots, s_n)$, where $s_i \in \{1, 2, 3\}$ represents the time block assigned to individual $i$. If no valid assignment exists, report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of individuals and the number of mutual exclusion restrictions, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a pair of individuals who cannot share the same time block.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 s_2 \dots s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the assigned time block for each individual from $1$ to $n$. Output the lexicographically smallest valid sequence if multiple valid assignments exist.

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
