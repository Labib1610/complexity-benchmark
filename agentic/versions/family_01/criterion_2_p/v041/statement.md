# Problem B — Load Balancing

Time limit: 1 s
Memory limit: 256 MB

A distributed network consists of $n$ processing units. You must assign each unit a load setting, which must be either 1 or 2.

The network has $m$ synchronization links. Each link connects a specific pair of processing units. To maintain system stability, every pair of units connected by a synchronization link must have a combined load setting (the sum of their individual load settings) exactly equal to 3.

Determine a valid assignment of load settings for all $n$ units, or determine that no such assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of processing units connected by a synchronization link.

## Output
If no stable assignment exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each either 1 or 2), representing the lexicographically smallest valid sequence of load settings.

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
