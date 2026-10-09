# Market Analyst Predictions

Time limit: 1 s   Memory limit: 256 MB

## Description

A financial firm is reviewing the performance of a portfolio containing $n$ distinct assets. For the upcoming quarter, each asset must be assigned exactly one rating: "buy" (represented by `1`) or "sell" (represented by `0`).

An analyst has submitted $m$ forecast reports. Each report specifies two potential outcomes for the portfolio. An outcome is represented by a non-zero integer $x$: 
- If $x > 0$, the outcome expects asset $x$ to receive a "buy" rating. 
- If $x < 0$, the outcome expects asset $|x|$ to receive a "sell" rating.

A final rating contradicts an outcome if it assigns "sell" when a "buy" was expected, or "buy" when a "sell" was expected. The firm's evaluation policy states that a forecast report is considered valid unless the final ratings contradict both of its potential outcomes simultaneously. 

Your task is to determine whether it is possible to assign a single rating to each of the $n$ assets such that all $m$ forecast reports are valid. If such an assignment exists, you must provide one. Otherwise, report that no such rating assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$, where $|l_i| \le n$. These represent the two potential outcomes for a single forecast report.

## Output
If there is no way to assign ratings to all assets such that every forecast report is valid, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $r_1$ $r_2$ $\dots$ $r_n$ (each being `0` or `1`), representing the rating assigned to each asset (where $r_i$ corresponds to asset $i$).

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid assignments may exist; any one is accepted. The same asset index may appear multiple times across different forecast reports, or even within the same report.
