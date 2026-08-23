# Problem B — Heterodyne Array Configuration

Time limit: 1 s   Memory limit: 256 MB

A radio telescope array contains $n$ local oscillators, numbered 1 to $n$. Each oscillator must be tuned to a frequency multiplier of either 1 or 2.

The array's signal processing relies on $m$ heterodyne correlators. Each correlator receives the multiplier signals from two specific oscillators. For the correlator to correctly downconvert the astronomical signal, the mathematical product of the two multipliers it receives must be exactly 2.

You must determine if there is a valid tuning configuration for all $n$ oscillators that satisfies all correlator requirements. If a valid configuration exists, you must output it. In cases where multiple configurations satisfy all requirements, you must output the configuration that forms the lexicographically smallest sequence of multipliers.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of two oscillators connected to a correlator.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each being 1 or 2), representing the lexicographically smallest valid sequence of multipliers.

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