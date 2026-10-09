# Problem C — Shift Assignment Failure Documentation

Time limit: 2 s   Memory limit: 256 MB

The factory operates two distinct shifts: Day and Night. Every worker must be assigned to exactly one of these shifts. Due to interpersonal conflicts, certain pairs of workers cannot be assigned to the same shift.

Management has realized that a conflict-free assignment using only two shifts is impossible. Your task is to provide the required documentation for this failure. You must find a set of three workers such that every worker in this set has a conflict with both of the other two. The existence of such a group proves that two shifts are insufficient. You are guaranteed that at least one such group exists.

To ensure data integrity, the factory's database guarantees the following conditions on the conflict records:
- Self-conflicts are not permitted.
- Duplicate conflict records between the same pair of workers do not exist.
- No individual worker is involved in $n$ or more conflicts.
- The total sum of conflict involvements across all workers (counting each conflict twice, once for each worker involved) is strictly less than $n^2$.

## Input
The first line contains two integers $n$ and $m$. The number of workers $n$ is between $3$ and $2000$, inclusive. The number of conflict pairs $m$ is between $3$ and $200000$, or the maximum possible number of distinct pairs for $n$ workers, whichever is smaller.

Each of the following $m$ lines contains two integers $u$ and $v$ — the ID numbers of a pair of workers who cannot share a shift. Workers are identified by integers from $1$ to $n$.

It is guaranteed that at least one mutually incompatible group of three workers exists.

## Output
Output three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the IDs of three workers who all have conflicts with each other. If there are multiple such groups, output the one that minimizes $a$. If there is still a tie, minimize $b$, and finally minimize $c$.

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
