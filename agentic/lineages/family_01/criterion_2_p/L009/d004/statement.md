# Problem B — Restricted Equation System

Time limit: 1 s   Memory limit: 256 MB

You are analyzing a system of $m$ equations over $n$ variables $x_1, x_2, \dots, x_n$. 
Due to domain constraints, every variable must be assigned an integer value from the restricted set $\{1, 2\}$. 

Each equation in the system involves exactly two variables (which may be the same variable repeated) and states that their sum must be exactly 3. 

Your task is to determine whether there is an assignment of values to all $n$ variables that satisfies all $m$ equations simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing the indices of the variables in an equation of the form $x_u + x_v = 3$.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $x_1, \dots, x_n$. If there are multiple valid assignments, choose the assignment that minimizes $x_1$. If there is still a tie, minimize $x_2$ among the remaining valid assignments, and continue this process sequentially up to $x_n$.

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