# Problem A — The Tri-Position Lock

Time limit: 2 s
Memory limit: 256 MB

A mechanical vault is secured by a system of $n$ dials (numbered 1 through $n$). To disengage the lock, each dial must be set to one of three possible calibration values: 1, 2, or 3.

The internal machinery includes $m$ rigid crossbars, each of which connects a specific pair of dials. The crossbars act as physical constraints: if any two dials connected by a crossbar are set to the exact same calibration value, the crossbar will bind and permanently jam the vault. You must find a configuration for all $n$ dials such that no crossbars bind.

If no such configuration exists, you must indicate that the vault cannot be opened. If multiple valid configurations exist, the mechanism requires you to enter the one that is lexicographically smallest. (Configuration $A$ is lexicographically smaller than configuration $B$ if, at the lowest dial index where they differ, $A$ has a lower calibration value than $B$).

## Input
The first line contains two integers $n$ and $m$ — the number of dials and the number of crossbars (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n(n−1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, representing the identifiers of two dials that are connected by a crossbar.

## Output
If the vault cannot be opened without jamming, output a single line with `NO`.
If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the calibration value for each dial $i$. This sequence must be the lexicographically smallest configuration that avoids jamming.

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