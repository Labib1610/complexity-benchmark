# Problem B — Horological Strata

Time limit: 1 s   Memory limit: 256 MB

A master watchmaker is designing a complex mechanical timepiece consisting of $n$ distinct gears. The chassis of the watch has two mounting planes, plane 1 and plane 2. Each gear must be installed on either plane 1 or plane 2.

The design specifies $m$ pairs of gears that overlap in their two-dimensional projection. To ensure these gears mesh correctly without binding, the watchmaker's specification dictates that for every overlapping pair, the product of their assigned plane numbers must be exactly 2.

You must determine a valid plane assignment for each of the $n$ gears that satisfies all overlap constraints, or report that the timepiece cannot be assembled as designed.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of gears that overlap.

## Output
If no valid plane assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $t_1, \dots, t_n$ (each $t_i \in \{1, 2\}$), where $t_i$ is the plane assigned to gear $i$. If there are multiple valid assignments, output the one that is lexicographically smallest.

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