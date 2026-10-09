# Problem B — Frequency Calibration

Time limit: 1 s
Memory limit: 256 MB

An industrial facility manages a network of $n$ automated machines. Each machine must be configured to use one of two specific operational modes, which are designated by the values 1 and 2.

The facility's monitoring system has flagged $m$ adjacency pairs. Each pair indicates two machines that are physically close enough to risk signal overlap. To guarantee safe operation, the system enforces a strict neighborhood interference protocol.

For any given machine, let $k$ be the number of adjacency pairs that include it. The protocol requires that the sum of the configured modes of its partner machines in these $k$ pairs must perfectly balance the given machine's own mode:
- If the given machine is configured to mode 1, the sum of the modes of its partner machines must be exactly $2k$.
- If the given machine is configured to mode 2, the sum of the modes of its partner machines must be exactly $k$.

Your task is to determine a mode configuration for all $n$ machines that satisfies this protocol for every machine, or determine that no such configuration is possible.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ — a pair of machines listed in an adjacency pair.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid configuration.

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