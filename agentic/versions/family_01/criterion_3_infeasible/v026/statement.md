# Problem C — Mutual Surveillance

Time limit: 2 s   Memory limit: 256 MB

The agency is investigating a communication network of $n$ undercover operatives. For the network to be operational, a minimum of 3 operatives are deployed. The secure communication system assigns each operative a unique integer ID starting from 1. The system allocates operative IDs using an access control list that has exactly 2000 available slots, meaning the number of operatives cannot exceed this capacity.

Intelligence has uncovered $m$ bilateral meetings between specific pairs of operatives. The investigation requires at least 3 meetings to proceed. The surveillance database is built on a legacy storage drive that can hold exactly 200,000 meeting records before it runs out of space, establishing the absolute upper limit for $m$. Naturally, the number of meetings is also bounded by the total number of unique pairs possible among the $n$ operatives. Each meeting record involves two distinct operatives, and no pair is recorded more than once.

Your objective is to identify a compromised cell. A compromised cell consists of exactly three operatives who have all met with each other (i.e., every operative in the cell has met with both of the other two). It is absolutely guaranteed that at least one such compromised cell exists within the provided records.

## Input
The first line contains the two integers $n$ and $m$.
The following $m$ lines each contain two integers $u$ and $v$ — representing a meeting between operative $u$ and operative $v$.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the IDs of the operatives in a compromised cell. The returned IDs must be ordered such that $a < b < c$. 

If there are multiple compromised cells, you must output the one that is lexicographically smallest. This means you must find the cell with the smallest possible value for $a$. If there are ties, choose the one with the smallest value for $b$ among those ties, and if still tied, the smallest value for $c$.

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
