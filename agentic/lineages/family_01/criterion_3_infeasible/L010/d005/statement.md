# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory management has a log of incompatibility reports. Each report identifies a pair of workers who cannot share a shift. To prove that their current two-shift system is doomed to fail, management wants to find a specific pattern in the log. Your job is not to schedule the workers, but to search the log to certify this impossibility.

Your task is to identify a "deadlock". A deadlock is formed by a subset of exactly three distinct reports from the log such that no worker is mentioned an odd number of times within the subset. Finding this configuration provides an undeniable certificate that two shifts cannot suffice.

It is guaranteed that the log contains at least one such deadlock. You must output the IDs of the workers who appear in the chosen reports of the deadlock.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a report naming two incompatible workers. All reports in the log represent distinct pairs.
It is guaranteed that at least one deadlock exists in the given reports.

## Output
Print the IDs of the workers who appear in the deadlock's reports on one line, sorted in ascending order. (Due to the parity constraint and the subset size, any valid deadlock will contain exactly three distinct workers, yielding three integers $a < b < c$). If there are multiple valid deadlocks, output the one that produces the lexicographically smallest sequence $(a, b, c)$.

## Example 1
### Input
4 5
1 2
1 3
2 3
2 4
3 4
### Output
1 2 3

## Example 2
### Input
5 6
1 2
1 4
2 4
3 4
3 5
4 5
### Output
1 2 4