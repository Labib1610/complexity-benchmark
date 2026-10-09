# Problem C — Interference Certificate

Time limit: 2 s   Memory limit: 256 MB

A wireless network deployment has access to exactly two non-overlapping frequency bands. Field surveys have produced a list of access point pairs that have overlapping signal coverage. If two access points have overlapping coverage, they cannot operate on the same frequency band.

The current configuration cannot be successfully deployed using only the two available bands. To document this failure in the site survey report, you are required to isolate a specific formation: a group of three distinct access points where the first overlaps with the second, the second overlaps with the third, and the third overlaps with the first. Because each pair within these three devices requires different bands, they cannot be accommodated by only two.

Your task is to find such a group of three access points. If there are multiple qualifying groups, you must select the one whose access points have the smallest possible IDs. To compare two groups, list the three IDs of each group in increasing order. The preferred group is the one with the smaller first ID. If the first IDs are identical, prefer the group with the smaller second ID, and if those are also identical, prefer the one with the smaller third ID.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of access points and the number of overlap reports, respectively. Access points are numbered from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$, indicating that access point $u$ and access point $v$ have overlapping signal coverage. 
It is guaranteed that the provided data contains at least one group of three access points satisfying the condition described above.

## Output
Output a single line containing three integers $a$, $b$, and $c$, separated by spaces, with $a < b < c$. These must be the IDs of the three access points in the chosen group, selected according to the tie-breaking rules.

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
