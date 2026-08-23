# Problem B — Orbital Relays

Time limit: 1 s   Memory limit: 256 MB

A communications network consists of $n$ orbital relays, numbered 1 through $n$. Each relay must be assigned a frequency band, which is strictly restricted to either band 1 or band 2.

The network contains $m$ interference zones. Each zone is a region where the signals of a specific pair of relays overlap. To avoid signal degradation, the product of the assigned band numbers of any two relays that overlap in a zone must be exactly 2.

Determine a frequency band assignment for all $n$ relays that satisfies this rule for every interference zone. If no such assignment is possible, report the failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of relays whose signals overlap in an interference zone.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid assignment.

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