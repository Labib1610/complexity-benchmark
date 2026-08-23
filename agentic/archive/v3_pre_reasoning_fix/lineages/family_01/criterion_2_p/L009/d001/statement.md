# Value Assignment

Time limit: 1 s   Memory limit: 256 MB

You are given a system of $n$ integer variables $x_1, x_2, \dots, x_n$. Each variable must be assigned a value of either 1 or 2.

You are also provided with a list of $m$ equations. Each equation is specified by two indices $u$ and $v$, and imposes the requirement that $x_u + x_v = 3$.

Your task is to determine whether there exists an assignment of values to all $n$ variables such that every equation is satisfied. 

If a valid assignment exists, you must provide it. Because there may be multiple valid assignments, you must output the lexicographically smallest sequence of values. A sequence of values $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first index $i$ where they differ, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of variables and the number of equations.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the indices of the variables for the equation $x_u + x_v = 3$.

## Output
If there is no way to assign the values 1 and 2 to all variables such that all $m$ equations are satisfied, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $x_1 \dots x_n$ (each being 1 or 2), representing the lexicographically smallest valid assignment.

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