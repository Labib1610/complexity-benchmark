# Problem B — Calibration Sequence

Time limit: 1 s   Memory limit: 256 MB

A precision manufacturing machine has $n$ adjustable actuators, numbered 1 to $n$. Each actuator must be calibrated to a setting of either 1 or 2.

The machine's structural integrity depends on $m$ mechanical linkages. Each linkage connects two specific actuators. To maintain equilibrium, the sum of the settings of the two actuators connected by any linkage must be exactly 3.

You must determine if there is a valid configuration for all $n$ actuators that satisfies all equilibrium conditions. If a valid configuration exists, you must output it. In cases where multiple configurations satisfy all conditions, you must output the configuration that forms the lexicographically smallest sequence of settings.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of two actuators connected by a linkage.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each being 1 or 2), representing the lexicographically smallest valid calibration sequence.

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