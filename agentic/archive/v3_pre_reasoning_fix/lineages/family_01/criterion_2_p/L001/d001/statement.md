# Orbital Array Calibration

Time limit: 1 s   Memory limit: 256 MB

An orbital observatory consists of $n$ mirror segments, numbered 1 to $n$. Each segment must be locked into one of two calibration modes, designated as mode 1 and mode 2.

The observatory's chassis introduces structural vibrations. There are $m$ specific pairs of segments that are mechanically coupled in a way that amplifies these vibrations. To actively cancel the resonance, any two mechanically coupled segments must be locked into different calibration modes.

Determine if it is possible to assign a calibration mode to every segment such that all resonance is canceled. If there are multiple valid configurations, the system requires the configuration that is lexicographically smallest when the modes of segments 1 through $n$ are written as a sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that mirror segments $u$ and $v$ are mechanically coupled.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \ldots, c_n$ (where each $c_i \in \{1, 2\}$) representing the lexicographically smallest valid calibration mode sequence.

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