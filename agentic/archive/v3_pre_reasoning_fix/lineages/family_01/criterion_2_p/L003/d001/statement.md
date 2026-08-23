# Problem B — Voltage Bridging

Time limit: 1 s   Memory limit: 256 MB

A manufacturing process involves $n$ machines. Each machine must be supplied with an operating voltage of either 1 or 2. There are $m$ bridging circuits. Each bridging circuit connects a specific pair of machines and requires an absolute voltage difference of exactly 1 between its two endpoints to function properly.

Determine a valid voltage for each machine so that all bridging circuits are satisfied, or report if this cannot be done.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of machines connected by a bridging circuit.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1, 2}), representing the valid voltage assignment. If there are multiple valid assignments, choose the one that minimizes the voltage of machine 1. If ties remain, minimize the voltage of machine 2, and continue this sequential minimization up to machine $n$.

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