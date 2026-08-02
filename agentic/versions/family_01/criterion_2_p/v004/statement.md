# Assignment Configuration

Time limit: 1 s   Memory limit: 256 MB

A facility operates across $n$ distinct personnel IDs (numbered $1$ through $n$) and must split all personnel into two operational divisions, designated $1$ and $2$. There are $m$ pairwise incompatibility constraints, each specifying that two particular individuals cannot be assigned to the same division.

With $2^n$ possible total divisional arrangements, determine if there exists at least one configuration where every incompatibility constraint is satisfied simultaneously. If one or more valid configurations exist, identify the one that is lexicographically smallest when listed as a sequence of division assignments $s_1, s_2, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing an incompatibility constraint between individual $u$ and individual $v$.

## Output
If no valid division arrangement exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1, 2\}$), representing the lexicographically smallest valid assignment sequence.

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
