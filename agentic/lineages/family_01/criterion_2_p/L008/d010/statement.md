# Problem B — Anti-Glare Arrays

Time limit: 1 s
Memory limit: 256 MB

An optical instrument contains $n$ crystal lenses. Each lens must be assigned a polarization mode, which must be an integer value of either $1$ or $2$.

The instrument is equipped with $m$ calibration tubes, each routing data between a pair of lenses. The instrument's diagnostic system validates the configuration by evaluating the total stability of the system.

For a calibration tube connecting lens $u$ and lens $v$, its local stability index is calculated using the formula $3 c_u + 3 c_v - 2 c_u c_v$, where $c_u$ and $c_v$ are the assigned polarization modes of the two connected lenses.

To successfully filter out glare, there must exist some valid assignment of polarization modes to all $n$ lenses such that the total stability index (the sum of the local stability indices across all $m$ calibration tubes) is exactly $5m$.

Determine an assignment of polarization modes for all $n$ lenses that makes such a configuration possible, or report that the hardware configuration is flawed.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the two lenses connected by that calibration tube.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES`, followed by a second line with $n$ integers $c_1 \dots c_n$ (each in $\{1,2\}$). This sequence must represent the valid assignment. If multiple valid assignments exist, output the lexicographically smallest sequence.

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