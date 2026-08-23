# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

The factory currently operates using only two shifts, Shift 1 and Shift 2, but the latest HR roster of interpersonal disputes is known to be fundamentally incompatible with a two-shift system. Your job is not to attempt to schedule the workers — it is to extract a definitive proof of this failure.

It is guaranteed that within the workforce, there exists at least one trio of employees where every individual has a logged dispute with both of the other two members of the trio. Any such trio proves that two shifts cannot possibly suffice, as no two members of the trio can share a shift without a dispute. You must identify one such trio.

## Input
The first line contains two integers: the workforce size $n$ and the number of logged disputes $m$.
The workforce size $n$ is bounded below by the exact number of individuals required to form a failing trio, and never exceeds the building's maximum fire-code capacity of 2000 workers.
The number of disputes $m$ is at least the number of mutual disputes required to form a single such trio. It is capped by the smaller of two limits: the total number of unique pairs that could possibly be formed from the $n$ workers, and the HR administrative system's limit of 200,000.

Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of workers who have a dispute. Workers are identified by numbers starting from 1 up to $n$.
It is guaranteed that at least one such trio of mutually disputing workers exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are logged disputes. Output the lexicographically smallest such combination (the one with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

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
