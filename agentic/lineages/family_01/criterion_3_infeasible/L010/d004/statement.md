# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory management has a log of incompatibility reports. Each report identifies a pair of workers who cannot share a shift. To prove that their current two-shift system is doomed to fail, management wants to find a specific pattern in the log. Your job is not to schedule the workers, but to search the log to certify this impossibility.

Your task is to identify a "deadlock". If we treat each report as a set containing two workers, a deadlock is formed by choosing exactly three distinct reports from the log such that their symmetric difference is the empty set. (The symmetric difference of a collection of sets consists of all elements that appear in an odd number of those sets).

Because each report contains exactly two workers, finding three distinct reports with an empty symmetric difference provides an undeniable certificate that two shifts cannot suffice. Finding this configuration might seem daunting given the sheer number of possible three-report combinations to check.

It is guaranteed that the log contains at least one such deadlock. You must output the IDs of the workers who appear in the chosen reports of the deadlock. (Because the symmetric difference is empty and the reports are distinct pairs, there will always be exactly three such workers in a deadlock).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a report naming two incompatible workers. All reports in the log represent distinct pairs.
It is guaranteed that at least one deadlock exists in the given reports.

## Output
Print three integers $a$, $b$, $c$ on one line with $a < b < c$ representing the three workers who appear in the deadlock's reports. Output the lexicographically smallest such group of workers (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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