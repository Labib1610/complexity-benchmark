# Redundant Storage Cell

Time limit: 2 s   Memory limit: 256 MB

A cloud infrastructure provider operates $n$ data vaults, identified by integers from 1 to $n$. To facilitate rapid data transfer, they have laid $m$ direct secure fiber links. Each link physically connects a specific pair of vaults.

The provider needs to establish a "redundant storage cell". A cell is formed by selecting exactly three distinct vaults. To guarantee uninterrupted data synchronization, the cell must satisfy a strict fault-tolerance requirement: if any single vault within the cell is taken offline for maintenance, the remaining two active vaults must be directly connected by a secure fiber link.

System logs indicate that at least one valid cell configuration is possible. Your objective is to process the fiber link records and identify one such cell.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of vaults connected by a secure fiber link.
It is guaranteed that at least one redundant storage cell can be formed.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the vaults in the cell. Output the lexicographically smallest such set (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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