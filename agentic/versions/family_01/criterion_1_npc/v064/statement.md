# Problem A — Frequency Allocation

Time limit: 2 s   Memory limit: 256 MB

A deployment of $n$ wireless access points requires channel configuration. You must assign each access point exactly one of three available non-overlapping frequency bands, designated 1, 2, and 3. Due to their physical placement, certain pairs of access points have overlapping signal ranges. To prevent packet collisions, any two access points with overlapping ranges must be assigned different frequency bands.

The central controller auto-generates the configuration files by evaluating the sequence of band assignments for access points 1 to $n$. To ensure predictable behavior, the controller requires the sequence of assignments to be the lexicographically smallest valid sequence (comparing the band of access point 1 first, then access point 2, and so on).

Determine if a valid frequency assignment exists, and if so, provide the required configuration sequence.

## Input
The first line contains two integers $n$ and $m$ — the number of access points and the number of overlapping signal pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The access points are numbered from 1 to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that access point $u$ and access point $v$ have overlapping signal ranges.

## Output
If it is impossible to assign the frequency bands without packet collisions, output NO on a single line.
Otherwise, output YES on the first line. On the second line, output $n$ integers $b_1, b_2, \dots, b_n$ (where each $b_i \in \{1, 2, 3\}$), representing the frequency band assigned to access point $i$. This sequence must be the lexicographically smallest valid assignment.

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
