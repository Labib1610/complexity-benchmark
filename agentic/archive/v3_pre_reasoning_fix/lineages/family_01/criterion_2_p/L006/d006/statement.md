# Problem B — Fusion Containment

Time limit: 1 s   Memory limit: 256 MB

You are configuring a dual-polarity magnetic containment field for an experimental fusion reactor. The reactor contains $n$ plasma emitters, numbered 1 to $n$. Every emitter must be calibrated to exactly one of two polarity modes: mode 1 or mode 2.

The physical geometry of the reactor results in $m$ thermal conduits. Each conduit bridges a specific pair of emitters. To maintain magnetic equilibrium, any two emitters bridged by a conduit must be calibrated to opposite modes: exactly one emitter must be set to mode 1, and the other must be set to mode 2.

Your task is to determine if there is a valid mode calibration for all $n$ emitters that maintains equilibrium across all thermal conduits. If multiple valid calibrations are possible, the initialization firmware requires the configuration whose sequence of mode assignments is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of plasma emitters and the number of thermal conduits, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ indicating that emitter $u$ and emitter $v$ are bridged by a thermal conduit.

## Output
If no valid calibration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of mode assignments.

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