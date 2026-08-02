# Channel Band Allocation Protocol

Time limit: 2 s   Memory limit: 256 MB

In an automated signal processing pipeline, a cluster of $n$ broadcast units (indexed $1$ through $n$) must be assigned to operational channels. There are exactly three available channel bands, identified by the integers $1$, $2$, and $3$.

Certain pairs of broadcast units experience mutual interference and are prohibited from being assigned to the same channel band. Every unit must receive exactly one channel assignment such that no two interfering units share a channel band.

When a valid channel allocation exists, the system requires the assignment sequence $s_1, s_2, \dots, s_n$ that is lexicographically smallest. That is, if multiple valid assignments satisfy all interference constraints, the system prefers the one with the smallest value at $s_1$; if there is a tie, the smallest value at $s_2$, and so forth. If no assignment can satisfy every constraint, the allocation process fails.

Determine if a valid channel allocation exists, and if so, output the lexicographically smallest allocation sequence.

## Input
The first line of input contains two integers $n$ and $m$ — the total number of broadcast units and the number of interfering pairs. The total count of units $n$ is at least $1$ and does not exceed the hardware limit of $40$. The count of interfering pairs $m$ is non-negative and does not exceed the total number of distinct pairs of units, $\frac{n(n-1)}{2}$.

Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that unit $u$ and unit $v$ interfere with each other. No interfering pair is listed more than once.

## Output
If no valid channel assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ ($s_i \in \{1, 2, 3\}$), representing the channel assigned to each unit $1$ through $n$. If there are multiple valid solutions, print the lexicographically smallest sequence.

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
