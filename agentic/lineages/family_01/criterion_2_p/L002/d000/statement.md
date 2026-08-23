# Problem B — Shift Scheduling

Time limit: 1 s   Memory limit: 256 MB

A hospital assigns $n$ nurses to two daily shifts, labeled 1 and 2. Because certain nurses share a single specialized medical device, there are $m$ pairs of nurses who cannot work during the same shift. Assign each nurse a shift so that no such pair shares a shift, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of nurses who share a device.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), the lexicographically smallest valid assignment.

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
