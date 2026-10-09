# Diophantine Feasibility

Time limit: 1 s   Memory limit: 256 MB

You are analyzing a system of linear constraints over a discrete set of variables. The model consists of a state vector $X = (x_1, x_2, \dots, x_n)$ in an $n$-dimensional space. 

Every variable is subject to the strict domain bound $x_i \in \{1, 2\}$. Consequently, the global configuration space contains exactly $2^n$ potential state vectors.

The system is restricted by a set of $m$ equations. Each equation is defined by a pair of variable indices $(u, v)$ and specifies that the sum of these two variables must be exactly 3. 

Your objective is to evaluate the system and find a feasible state vector $X$ that satisfies all $m$ equations simultaneously. Because multiple feasible state vectors may exist in the space, you must output the lexicographically smallest valid vector. If the system of equations has no solution within the specified domain, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing the constraint $x_u + x_v = 3$.

## Output
If there is no state vector satisfying all equations, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $x_1, x_2, \dots, x_n$ (each in $\{1, 2\}$), representing the lexicographically smallest valid state vector.

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
