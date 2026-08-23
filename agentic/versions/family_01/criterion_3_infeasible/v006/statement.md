# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory still has only two shifts, 1 and 2, but the roster is known to be
hopeless. Your job is not to schedule — it is to certify the impossibility. It is
guaranteed that the conflict graph contains at least one set of three workers who
pairwise conflict. Any such set proves two shifts cannot suffice. Output one such set.

## Input
The first line contains two integers, the factory's headcount $n$ and the number of reported conflicts $m$. The headcount is always at least 3, and never exceeds the building's maximum capacity of exactly 2000 workers. The number of conflicts $m$ is at least 3, and is capped by the smaller of two limits: the total number of possible pairs among the $n$ workers, and the administrative system limit of 200,000.

Each of the next $m$ lines contains two integers $u$ and $v$ — a conflicting pair.
It is guaranteed that at least one such triple exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs
$a$–$b$, $a$–$c$, $b$–$c$ are conflicts. Output the lexicographically smallest such triple
(smallest $a$; ties by smallest $b$; then smallest $c$).

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
