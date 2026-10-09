# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The laboratory still has only two storage rooms, 1 and 2, but the inventory segregation is known to be hopeless. Your job is not to assign rooms — it is to certify the impossibility. It is guaranteed that the reaction logs contain at least one set of three distinct chemicals where, for any pair chosen from this set, they are documented to react with each other. Any such set proves two rooms cannot suffice. Output one such set.

## Input
The first line contains two integers $n$ and $m$. The integer $n$ represents the number of chemicals (identified by integers from $1$ to $n$). The laboratory requires a minimum test size of $3$ chemicals, and its physical storage capacity limits it to a maximum of $2000$ chemicals.
The integer $m$ represents the total number of documented reacting pairs. This value is at least $3$, and is capped at the minimum of two upper bounds: the theoretical maximum number of distinct pairs among the $n$ chemicals (which is $n(n-1)/2$), and the strict database limit of $2 \cdot 10^5$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$) — a distinct reacting pair of chemicals. It is guaranteed that at least one such set of three chemicals exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that these three chemicals form a set where any pair reacts with each other. Output the lexicographically smallest such sequence (smallest $a$; ties by smallest $b$; then smallest $c$).

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