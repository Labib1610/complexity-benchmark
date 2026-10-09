# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A factory employs $n$ workers and operates two shifts, labeled 1 and 2. There are $2^n$ possible ways to assign the workers to these shifts. 

You are provided with a list of $m$ incompatible worker pairs. You must search the space of all $2^n$ possible shift assignments to determine if there is a configuration where no two incompatible workers are assigned to the same shift. If such an assignment exists, you must output the lexicographically smallest one. Otherwise, report that no valid configuration exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair.

## Output
If no valid configuration exists among the $2^n$ possibilities, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), the lexicographically smallest valid assignment.

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
