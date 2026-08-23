# Planetary Core Assembly

Time limit: 2 s   Memory limit: 256 MB

A mechanical engineering team is evaluating $n$ distinct gear designs, labeled with integer IDs from 1 to $n$. Through extensive prototyping, they have confirmed $m$ specific meshing compatibilities, each indicating that two particular gears can run together continuously without jamming.

The engineers need to construct a "planetary core". A planetary core is an assembly consisting of exactly three distinct gears. To operate without seizing, the assembly must satisfy a strict structural condition: no matter which of the three gears is temporarily disengaged from the core, the remaining two gears must be a pair that has a confirmed meshing compatibility.

Physical constraints guarantee that at least one valid planetary core can be constructed. Your task is to process the compatibility records and identify one such assembly.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of gears that have a confirmed meshing compatibility.
It is guaranteed that at least one planetary core exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the gears in the planetary core. Output the lexicographically smallest such set (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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