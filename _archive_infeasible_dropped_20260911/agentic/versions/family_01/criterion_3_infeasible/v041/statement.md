# Problem C — Flawed Roster

Time limit: 2 s
Memory limit: 256 MB

The production facility is restricted to allocating its personnel to exactly two shifts. However, management has realized that this allocation is unworkable. You must provide concrete evidence of this failure. 

You are given pairs of personnel who cannot be placed on the same shift due to documented conflicts. The provided records are guaranteed to contain at least one trio of individuals such that each of the three has a documented conflict with both of the other two. Pointing out such a trio demonstrates that two shifts are inadequate. Your task is to identify one such trio.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of personnel and the number of documented conflicts, respectively. Personnel are numbered from 1 to n.
Each of the next m lines contains two integers u and v — a pair of individuals who have a documented conflict.
It is guaranteed that at least one trio of individuals with mutual conflicts exists.

## Output
Print three space-separated integers a b c on one line with a < b < c such that a and b have a conflict, a and c have a conflict, and b and c have a conflict. Output the lexicographically smallest such trio (the one with the smallest a; in case of ties, the smallest b; and then the smallest c).

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
