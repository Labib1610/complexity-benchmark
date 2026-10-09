# Problem A — Factory Zoning

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant is establishing safety protocols for its $n$ employees. Every employee must be assigned a zone code $z_i$, which must be an integer such that $0 < z_i < 4$.

The plant's safety guidelines specify $m$ pairs of employees who have overlapping equipment requirements. If two such employees are assigned identically valued zone codes, a resource conflict will occur. Thus, for each specified pair, the two employees must receive strictly distinct zone codes.

Determine an assignment of zone codes for all $n$ employees that prevents any resource conflicts, or report that the guidelines cannot be fulfilled.

## Input
The first line contains two integers $n$ and $m$ — the number of employees and the number of pairs with overlapping requirements ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating that employee $u$ and employee $v$ have overlapping equipment requirements.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $z_1, z_2, \dots, z_n$ (where each $z_i$ is an integer such that $0 < z_i < 4$), where $z_i$ is the zone code of employee $i$. Any valid sequence of zone codes is accepted.

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
