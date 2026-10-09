# Problem B — Anti-Glare Arrays

Time limit: 1 s   Memory limit: 256 MB

An optical instrument contains $n$ crystal lenses. Each lens must be calibrated to one of two polarization axes, labeled 1 and 2.

The instrument features $m$ calibration tubes. Each tube routes light directly between two specific lenses. To successfully filter out glare, for every tube, its two connected lenses must be calibrated such that one is set to axis 1 and the other is set to axis 2.

Determine a calibration for all $n$ lenses that satisfies this requirement for all $m$ tubes, or report that the hardware configuration is flawed.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two lenses connected by that calibration tube.

## Output
If no valid calibration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $c_1 \dots c_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid calibration assignment.

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