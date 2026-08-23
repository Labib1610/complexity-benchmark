# Problem B — Orbital Relays

Time limit: 1 s   Memory limit: 256 MB

A communications network consists of $n$ orbital relays, numbered 1 through $n$. You must provision each relay with exactly one of two available hardware configurations, designated by the integers 1 and 2.

The network includes $m$ interference zones, each representing a spatial region where the broadcasts of two specific relays intersect. To ensure safe operation, the configurations of intersecting relays must be strictly regulated according to a compatibility matrix. Specifically, if two relays share an interference zone and are provisioned with configurations $x$ and $y$, the ordered pair $(x, y)$ must be exactly one of the following approved patterns: (1, 2) or (2, 1).

Find a valid configuration for all $n$ relays such that the compatibility requirement is met across all interference zones. If the network cannot be safely configured, you must report this.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of relays and the number of interference zones, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that the broadcasts of relay $u$ and relay $v$ intersect in a zone.

## Output
If it is impossible to provision the network safely, output a single line containing NO.
If a valid provisioning exists, output YES on the first line. On the second line, output $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest sequence of configurations that satisfies all requirements.

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