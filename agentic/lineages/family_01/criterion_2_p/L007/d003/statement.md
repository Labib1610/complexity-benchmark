# Problem B — Facility Maintenance Tiers

Time limit: 1 s   Memory limit: 256 MB

A logistics facility operates $n$ automated delivery vehicles, numbered 1 to $n$. Each vehicle must be assigned exactly one maintenance tier, which must be either 1 or 2.

The facility features $m$ shared charging bays. Each bay is utilized exclusively by a specific pair of vehicles. To prevent power grid overloads, the maintenance tiers of the two vehicles sharing any single bay must be properly staggered. Specifically, for the two vehicles sharing a charging bay, the maximum of their assigned maintenance tiers must be exactly twice the minimum of their assigned maintenance tiers.

You must determine if there is a valid assignment of maintenance tiers to all $n$ vehicles that satisfies the requirements of all $m$ charging bays. If a valid assignment exists, you must output it. In cases where multiple valid assignments satisfy all requirements, you must output the assignment that forms the lexicographically smallest sequence of tiers.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the numbers of two vehicles that share a charging bay.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each being 1 or 2), representing the lexicographically smallest valid sequence of maintenance tiers.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```