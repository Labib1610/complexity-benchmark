# Problem B — Machine Modes

Time limit: 1 s   Memory limit: 256 MB

A manufacturing process relies on $n$ machines. You must assign each machine a calibration factor of either 1 or 2. 

The system has $m$ critical links between specific pairs of machines. To maintain stability, the calibration factors of the two machines in any critical link must multiply to exactly 2. 

Determine a valid calibration factor for each machine so that all critical links are stable, or report if this is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a critical link between machine $u$ and machine $v$.

## Output
If no stable assignment exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each either 1 or 2). This sequence must be the lexicographically smallest valid assignment.

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