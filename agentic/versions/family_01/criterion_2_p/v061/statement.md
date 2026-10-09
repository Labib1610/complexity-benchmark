# Problem B — Day and Night

Time limit: 1 s
Memory limit: 256 MB

The factory operates continuously and requires every employee to be assigned to a shift, which is coded as either 1 (Day) or 2 (Night).

To ensure continuous coverage, the operations manager has specified $m$ operational links between specific pairs of employees. For every linked pair, the absolute difference between their assigned shift codes must be exactly 1.

You need to determine if it is possible to assign a shift code to all $n$ employees such that all operational links are satisfied. If multiple valid assignments exist, you must find the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$. The headcount $n$ is at least 1 and restricted to a maximum building capacity of 200,000. The number of operational links $m$ is at least 0 and at most the system limit of 200,000.
Each of the next $m$ lines contains two integers $u$ and $v$ — representing an operational link between employee $u$ and employee $v$.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

## Example 1
### Input
```
4 4
1 2
2 3
3 4
1 4
```
### Output
```
YES
1 2 1 2
```

## Example 2
### Input
```
3 3
1 2
1 3
2 3
```
### Output
```
NO
```
