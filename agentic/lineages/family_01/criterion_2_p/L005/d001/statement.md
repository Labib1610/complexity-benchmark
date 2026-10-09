# Problem B — Frequency Calibration

Time limit: 1 s
Memory limit: 256 MB

An industrial plant operates a system of $n$ robotic units. Each unit must be calibrated to operate on one of two available frequency bands, labeled 1 and 2.

The plant's safety system contains $m$ proximity records. Each record identifies two units that operate close to one another. To prevent signal interference, the calibration must satisfy a strict safety rule: for any pair of units listed in a proximity record, the sum of their assigned frequency bands must evaluate to exactly 3.

You must assign a frequency band to each of the $n$ units such that every proximity record satisfies this safety rule, or determine that no such assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of units listed in a proximity record.

## Output
If no valid calibration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid calibration.

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