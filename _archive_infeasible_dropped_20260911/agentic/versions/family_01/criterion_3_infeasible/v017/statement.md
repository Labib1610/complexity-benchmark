# Problem C — Interference Certificate

Time limit: 2 s   Memory limit: 256 MB

A wireless network deployment has access to exactly two non-overlapping frequency bands. You have gathered field reports detailing which pairs of access points have overlapping signal coverage and would interfere if assigned the same band. 

The current layout is known to be unworkable with only two bands. To formally certify this in the site survey report, you must identify a localized cluster of exactly three access points where every access point in the cluster interferes with both of the other two. 

Your task is to find and report this cluster. To ensure a standardized report, if multiple such three-device clusters exist, you must select the one with the smallest possible access point IDs. Specifically, minimize the smallest ID in the cluster; if there is a tie, minimize the second-smallest ID; and if still tied, minimize the third.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of access points and the number of interference reports, respectively. Access points are numbered from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$, indicating that access point $u$ and access point $v$ interfere with each other. 
It is guaranteed that the provided data contains at least one cluster of three mutually interfering access points.

## Output
Output a single line containing three integers $a$, $b$, and $c$, separated by spaces, with $a < b < c$. These must be the IDs of three mutually interfering access points, chosen according to the tie-breaking rules described above.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
