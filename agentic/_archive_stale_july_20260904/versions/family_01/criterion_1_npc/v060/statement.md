# Problem A — Asset Portfolio Allocation

Time limit: 2 s
Memory limit: 256 MB

A wealth management firm is structuring a new portfolio consisting of $n$ distinct financial assets. To distribute risk, every asset must be allocated to exactly one of three available investment vehicles, designated as Fund 1, Fund 2, and Fund 3.

Due to strict antitrust regulations and sector exposure limits, certain pairs of assets cannot be held within the same fund. If two such restricted assets are placed together, the firm will face compliance violations. You must distribute all $n$ assets among the three funds such that no compliance violations occur.

The firm's automated auditing software requires the allocation to be deterministic. Specifically, among all valid allocations, the system mandates the one where the sequence of fund numbers assigned to assets $1, 2, \dots, n$ is lexicographically smallest. This means the system prioritizes placing asset 1 into the lowest-numbered fund possible, then asset 2 into the lowest-numbered fund possible, and so forth, while still maintaining complete regulatory compliance.

If it is impossible to allocate the assets without triggering a violation, the portfolio proposal must be rejected.

## Input
The first line provides two integers $n$ and $m$ — the total number of assets and the number of regulatory restrictions ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$ — a pair of assets that are prohibited from being allocated to the same fund.

## Output
If no compliant allocation strategy exists, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, provide a sequence of $n$ integers $f_1, f_2, \dots, f_n$ (where each $f_i \in \{1, 2, 3\}$), representing the fund assigned to each asset $i$. This sequence must be the lexicographically smallest valid allocation.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
