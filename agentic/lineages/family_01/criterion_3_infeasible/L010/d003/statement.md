# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory management has a log of incompatibility reports. They want to find a specific pattern in the log that proves their current two-shift system is doomed to fail. Your job is not to schedule the workers, but to search the log to certify this impossibility.

Your task is to identify a "deadlock". A deadlock is formed by choosing exactly three reports from the log that satisfy a specific frequency condition: if you tally how many times each worker ID appears across your chosen three reports, exactly three workers will have a tally of exactly 2, and all other workers will have a tally of 0. 

Such a configuration provides an undeniable certificate that two shifts cannot suffice. Finding this configuration might seem daunting given the sheer number of possible three-report combinations to check.

It is guaranteed that the log contains at least one such deadlock. You must output the IDs of the three workers whose tally is 2 in this deadlock.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a report naming two incompatible workers.
It is guaranteed that at least one deadlock exists in the given reports.

## Output
Print three integers $a$, $b$, $c$ on one line with $a < b < c$ representing the three workers who each have a tally of 2 in the deadlock. Output the lexicographically smallest such group of workers (smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```